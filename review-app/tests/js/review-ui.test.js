"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");
const { webcrypto } = require("node:crypto");
const {
  constants,
  createDraftRecovery,
  registerDraftInputCapture,
  restoreEntry
} = require("../../inst/app/www/review-ui.js");

class MemoryStorage {
  constructor() {
    this.values = new Map();
    this.failWrites = false;
  }

  get length() {
    return this.values.size;
  }

  getItem(key) {
    return this.values.has(key) ? this.values.get(key) : null;
  }

  key(index) {
    return Array.from(this.values.keys())[index] || null;
  }

  removeItem(key) {
    this.values.delete(key);
  }

  setItem(key, value) {
    if (this.failWrites) throw new Error("storage unavailable");
    this.values.set(key, String(value));
  }
}

function fixedHex(character, length) {
  return character.repeat(length);
}

function recoveryContext(overrides = {}) {
  return {
    editable: true,
    schemaVersion: constants.schemaVersion,
    lookupKey: fixedHex("a", 64),
    contextKey: fixedHex("b", 64),
    sourceCommit: fixedHex("c", 40),
    sourceBlobSha: fixedHex("d", 40),
    baseBodySha256: fixedHex("e", 64),
    baseRecordBlobSha: fixedHex("f", 40),
    editorId: "detail-editor_body",
    ...overrides
  };
}

function fakeTimers() {
  let nextId = 0;
  const callbacks = new Map();
  return {
    clearTimeout(id) {
      callbacks.delete(id);
    },
    runAll() {
      const pending = Array.from(callbacks.values());
      callbacks.clear();
      pending.forEach((callback) => callback());
    },
    setTimeout(callback) {
      nextId += 1;
      callbacks.set(nextId, callback);
      return nextId;
    }
  };
}

function newController({
  storage = new MemoryStorage(),
  tabStorage = new MemoryStorage(),
  date = new Date("2026-08-31T12:00:00Z"),
  crypto = webcrypto,
  onError = () => {}
} = {}) {
  const timers = fakeTimers();
  const controller = createDraftRecovery({
    storage,
    tabStorage,
    crypto,
    textEncoder: new TextEncoder(),
    setTimeout: timers.setTimeout,
    clearTimeout: timers.clearTimeout,
    now: () => new Date(date),
    onError
  });
  return { controller, storage, tabStorage, timers };
}

function fakeClassList(initial = []) {
  const values = new Set(initial);
  return {
    add(value) { values.add(value); },
    contains(value) { return values.has(value); },
    remove(value) { values.delete(value); },
    toggle(value, enabled) {
      if (enabled) values.add(value);
      else values.delete(value);
    }
  };
}

function loadBrowserRuntime() {
  const sourcePath = path.resolve(__dirname, "../../inst/app/www/review-ui.js");
  const source = fs.readFileSync(sourcePath, "utf8");
  const localStorage = new MemoryStorage();
  const sessionStorage = new MemoryStorage();
  const documentListeners = new Map();
  const windowListeners = new Map();
  const shinyHandlers = new Map();
  const timers = fakeTimers();
  let panel = null;
  let textarea = null;
  let inputEvents = 0;
  let confirmCalls = 0;
  let alertCalls = 0;
  let confirmResult = false;
  let currentBlob = null;
  const clipboardWrites = [];
  const downloads = [];
  const root = { classList: fakeClassList(), dataset: {} };
  const body = {
    nodeType: 1,
    matches() { return false; },
    querySelector() { return null; }
  };

  function addListener(collection, type, handler, capture = false) {
    const listeners = collection.get(type) || [];
    listeners.push({ handler, capture: capture === true });
    collection.set(type, listeners);
  }

  function dispatch(collection, type, event) {
    const listeners = collection.get(type) || [];
    listeners.filter((item) => item.capture).forEach((item) => item.handler(event));
    listeners.filter((item) => !item.capture).forEach((item) => item.handler(event));
  }

  class BrowserEvent {
    constructor(type, options = {}) {
      this.type = type;
      this.bubbles = Boolean(options.bubbles);
      this.target = null;
    }
  }

  class Observer {
    constructor(callback) {
      this.callback = callback;
    }

    observe() {}
  }

  const documentObject = {
    body,
    visibilityState: "visible",
    addEventListener(type, handler, capture) {
      addListener(documentListeners, type, handler, capture);
    },
    createElement(type) {
      if (type === "option") return { value: "", textContent: "" };
      return {
        click() {
          downloads.push({
            blob: currentBlob,
            download: this.download,
            href: this.href
          });
        },
        classList: fakeClassList()
      };
    },
    getElementById(id) {
      return textarea && textarea.id === id ? textarea : null;
    },
    querySelector(selector) {
      if (selector === ".review-app") return root;
      if (selector === ".draft-recovery-panel") return panel;
      return null;
    },
    querySelectorAll() { return []; }
  };

  const windowObject = {
    Blob,
    Event: BrowserEvent,
    Shiny: {
      addCustomMessageHandler(name, handler) {
        shinyHandlers.set(name, handler);
      }
    },
    TextEncoder,
    alert() { alertCalls += 1; },
    clearTimeout: timers.clearTimeout,
    confirm() {
      confirmCalls += 1;
      return confirmResult;
    },
    crypto: webcrypto,
    localStorage,
    requestAnimationFrame(callback) { callback(); },
    sessionStorage,
    setTimeout: timers.setTimeout,
    addEventListener(type, handler, capture) {
      addListener(windowListeners, type, handler, capture);
    }
  };

  const sandbox = {
    Blob,
    MutationObserver: Observer,
    Shiny: windowObject.Shiny,
    TextEncoder,
    URL: {
      createObjectURL(blob) {
        currentBlob = blob;
        return "blob:fixture";
      },
      revokeObjectURL() {}
    },
    console,
    document: documentObject,
    module: { exports: {} },
    navigator: {
      clipboard: {
        writeText(value) {
          clipboardWrites.push(value);
          return Promise.resolve();
        }
      }
    },
    window: windowObject
  };
  vm.runInNewContext(source, sandbox, { filename: "review-ui.js" });
  dispatch(documentListeners, "DOMContentLoaded", { target: documentObject });

  function makeButton(className) {
    const button = {
      classList: fakeClassList([className]),
      hidden: false,
      closest(selector) {
        if (selector === ".draft-recovery-panel") return panel;
        if (selector.includes("." + className)) return button;
        return null;
      }
    };
    return button;
  }

  function setContext(context, editorValue = "Persisted body") {
    const select = {
      children: [],
      hidden: false,
      value: "",
      get firstChild() { return this.children[0] || null; },
      appendChild(option) {
        this.children.push(option);
        if (!this.value) this.value = option.value;
      },
      removeChild(option) {
        this.children.splice(this.children.indexOf(option), 1);
        if (!this.children.length) this.value = "";
      }
    };
    const controls = {
      copy: makeButton("draft-recovery-copy-button"),
      discard: makeButton("draft-recovery-discard"),
      export: makeButton("draft-recovery-export"),
      restore: makeButton("draft-recovery-restore"),
      select,
      status: { textContent: "" }
    };
    panel = {
      classList: fakeClassList(["draft-recovery-panel"]),
      dataset: {
        recoveryBaseBodySha256: context.baseBodySha256,
        recoveryBaseRecordBlobSha: context.baseRecordBlobSha,
        recoveryContextKey: context.contextKey,
        recoveryEditable: context.editable ? "true" : "false",
        recoveryEditorId: context.editorId,
        recoveryLookupKey: context.lookupKey,
        recoverySchemaVersion: String(context.schemaVersion),
        recoverySourceBlobSha: context.sourceBlobSha,
        recoverySourceCommit: context.sourceCommit
      },
      hidden: true,
      querySelector(selector) {
        const mapping = {
          ".draft-recovery-copy-button": controls.copy,
          ".draft-recovery-discard": controls.discard,
          ".draft-recovery-export": controls.export,
          ".draft-recovery-restore": controls.restore,
          ".draft-recovery-select": controls.select,
          ".draft-recovery-status": controls.status
        };
        return mapping[selector] || null;
      }
    };
    textarea = {
      id: context.editorId,
      innerHTML: "unchanged",
      value: editorValue,
      dispatchEvent(event) {
        inputEvents += 1;
        event.target = textarea;
        dispatch(documentListeners, event.type, event);
      }
    };
    return controls;
  }

  function click(target) {
    const event = {
      target,
      prevented: false,
      stopped: false,
      preventDefault() { this.prevented = true; },
      stopImmediatePropagation() { this.stopped = true; }
    };
    dispatch(documentListeners, "click", event);
    return event;
  }

  return {
    click,
    dispatchDocument(type, event) { dispatch(documentListeners, type, event); },
    dispatchWindow(type, event) { dispatch(windowListeners, type, event); },
    get alertCalls() { return alertCalls; },
    clipboardWrites,
    get confirmCalls() { return confirmCalls; },
    downloads,
    get inputEvents() { return inputEvents; },
    get panel() { return panel; },
    get textarea() { return textarea; },
    localStorage,
    setConfirmResult(value) { confirmResult = value; },
    setContext,
    shinyHandlers,
    windowObject
  };
}

test("editor input is captured before a Shiny bubble listener receives it", () => {
  const setup = newController();
  const context = recoveryContext();
  const listeners = [];
  const fakeDocument = {
    addEventListener(type, handler, capture) {
      listeners.push({ type, handler, capture });
    }
  };
  let pendingAtShinyListener = false;
  listeners.push({
    type: "input",
    capture: false,
    handler() {
      pendingAtShinyListener = setup.controller.hasPending(
        setup.controller.storageKey(context)
      );
    }
  });
  registerDraftInputCapture(fakeDocument, setup.controller, () => context);
  const recoveryListener = listeners.find((item) => item.handler !==
    listeners[0].handler);
  assert.equal(recoveryListener.capture, true);

  const event = {
    target: { id: context.editorId, value: "captured locally" }
  };
  listeners.filter((item) => item.capture).forEach((item) => item.handler(event));
  listeners.filter((item) => !item.capture).forEach((item) => item.handler(event));

  assert.equal(pendingAtShinyListener, true);
});

test("Unicode Markdown survives a storage reload byte-safely", async () => {
  const storage = new MemoryStorage();
  const tabStorage = new MemoryStorage();
  const first = newController({ storage, tabStorage });
  const context = recoveryContext();
  const markdown = "Cafe\u0301, \u6f22\u5b57, and \ud83c\udf0d\n";
  first.controller.capture(context, markdown);
  first.controller.flushAll();

  const reloaded = newController({ storage, tabStorage });
  const entries = reloaded.controller.entries(context);
  assert.equal(entries.length, 1);
  assert.equal(entries[0].record.markdown_body, markdown);
  assert.equal(
    await reloaded.controller.sha256(entries[0].record.markdown_body),
    "d37b78ea323749637c92f79fe0519a85f8fed187476ba8021c62f5cfc7c2c036"
  );
  assert.equal(await first.controller.acknowledge({
    context_key: context.contextKey,
    saved_body_sha256:
      "d37b78ea323749637c92f79fe0519a85f8fed187476ba8021c62f5cfc7c2c036"
  }), 1);
  assert.equal(storage.length, 0);
});

test("stored values contain only the recovery contract fields", () => {
  const setup = newController();
  const context = recoveryContext();
  setup.controller.capture(context, "Markdown body only");
  setup.controller.flushAll();
  const record = setup.controller.entries(context)[0].record;

  assert.deepEqual(Object.keys(record).sort(), [
    "base_body_sha256",
    "base_record_blob_sha",
    "markdown_body",
    "recovery_schema_version",
    "saved_at",
    "source_blob_sha",
    "source_commit",
    "tab_id"
  ]);
  assert.equal(JSON.stringify(record).includes("repository"), false);
  assert.equal(JSON.stringify(record).includes("actor"), false);
  assert.equal(JSON.stringify(record).includes("---"), false);
});

test("restore requires an explicit action and writes only textarea value", () => {
  const setup = newController();
  const context = recoveryContext();
  setup.controller.capture(context, "<img src=x onerror=alert(1)>\n# Draft");
  setup.controller.flushAll();
  const entry = setup.controller.entries(context)[0];
  let inputEvents = 0;
  const textarea = {
    value: "Persisted body",
    innerHTML: "unchanged",
    dispatchEvent(event) {
      if (event.type === "input") inputEvents += 1;
    }
  };

  assert.equal(textarea.value, "Persisted body");
  assert.equal(inputEvents, 0);
  assert.equal(restoreEntry(entry, context, textarea, Event), true);
  assert.equal(textarea.value, entry.record.markdown_body);
  assert.equal(textarea.innerHTML, "unchanged");
  assert.equal(inputEvents, 1);
});

test("discard removes only the selected recovery entry", () => {
  const storage = new MemoryStorage();
  const first = newController({ storage, tabStorage: new MemoryStorage() });
  const second = newController({ storage, tabStorage: new MemoryStorage() });
  const context = recoveryContext();
  first.controller.capture(context, "first tab");
  first.controller.flushAll();
  second.controller.capture(context, "second tab");
  second.controller.flushAll();
  const entries = first.controller.entries(context);

  assert.equal(entries.length, 2);
  first.controller.discard(entries[0].key);
  const remaining = first.controller.entries(context);
  assert.equal(remaining.length, 1);
  assert.notEqual(remaining[0].key, entries[0].key);
});

test("a matching successful save clears only the matching body", async () => {
  const setup = newController();
  const context = recoveryContext();
  setup.controller.capture(context, "saved body");
  setup.controller.flushAll();
  const savedBodySha256 = await setup.controller.sha256("saved body");

  const cleared = await setup.controller.acknowledge({
    context_key: context.contextKey,
    saved_body_sha256: savedBodySha256
  });
  assert.equal(cleared, 1);
  assert.equal(setup.controller.entries(context).length, 0);
});

test("a failed or mismatched save preserves recovery", async () => {
  const setup = newController();
  const context = recoveryContext();
  setup.controller.capture(context, "unsaved body");
  setup.controller.flushAll();

  assert.equal(setup.controller.entries(context).length, 1);
  await setup.controller.acknowledge({
    context_key: context.contextKey,
    saved_body_sha256: await setup.controller.sha256("different body")
  });
  assert.equal(setup.controller.entries(context).length, 1);
});

test("a delayed acknowledgement cannot clear another artifact", async () => {
  const setup = newController();
  const artifactA = recoveryContext();
  const artifactB = recoveryContext({
    lookupKey: fixedHex("1", 64),
    contextKey: fixedHex("2", 64)
  });
  setup.controller.capture(artifactA, "artifact A");
  setup.controller.capture(artifactB, "artifact B");
  setup.controller.flushAll();

  await setup.controller.acknowledge({
    context_key: artifactA.contextKey,
    saved_body_sha256: await setup.controller.sha256("artifact A")
  });
  assert.equal(setup.controller.entries(artifactA).length, 0);
  assert.equal(setup.controller.entries(artifactB).length, 1);
});

test("a delayed acknowledgement cannot clear a newer same-artifact edit", async () => {
  let resolveDigest;
  const delayedCrypto = {
    randomUUID: webcrypto.randomUUID.bind(webcrypto),
    subtle: {
      digest(algorithm, bytes) {
        return new Promise((resolve) => {
          resolveDigest = () => webcrypto.subtle.digest(algorithm, bytes)
            .then(resolve);
        });
      }
    }
  };
  const setup = newController({ crypto: delayedCrypto });
  const context = recoveryContext();
  setup.controller.capture(context, "saved A");
  setup.controller.flushAll();
  const savedBodySha256 = await createDraftRecovery({
    storage: new MemoryStorage(),
    tabStorage: new MemoryStorage(),
    crypto: webcrypto,
    textEncoder: new TextEncoder(),
    setTimeout: setTimeout,
    clearTimeout: clearTimeout,
    now: () => new Date()
  }).sha256("saved A");
  const acknowledgement = setup.controller.acknowledge({
    context_key: context.contextKey,
    saved_body_sha256: savedBodySha256
  });
  setup.controller.capture(context, "newer B");
  resolveDigest();

  assert.equal(await acknowledgement, 0);
  assert.equal(
    setup.controller.hasPending(setup.controller.storageKey(context)),
    true
  );
  setup.controller.flushAll();
  assert.equal(
    setup.controller.entries(context)[0].record.markdown_body,
    "newer B"
  );
});

test("opaque lookup scope isolates actor, repository, branch, queue, and artifact", () => {
  const setup = newController();
  const original = recoveryContext();
  const isolated = recoveryContext({
    lookupKey: fixedHex("1", 64),
    contextKey: fixedHex("2", 64)
  });
  setup.controller.capture(original, "scoped body");
  setup.controller.flushAll();

  assert.equal(setup.controller.entries(original).length, 1);
  assert.equal(setup.controller.entries(isolated).length, 0);
});

test("source revision mismatch blocks direct restore", () => {
  const setup = newController();
  const original = recoveryContext();
  setup.controller.capture(original, "draft");
  setup.controller.flushAll();
  const entry = setup.controller.entries(original)[0];
  const changed = recoveryContext({
    contextKey: fixedHex("1", 64),
    sourceCommit: fixedHex("2", 40)
  });

  assert.deepEqual(setup.controller.classify(entry, changed), {
    restorable: false,
    reason: "The source revision changed."
  });
});

test("source blob mismatch blocks direct restore", () => {
  const setup = newController();
  const original = recoveryContext();
  setup.controller.capture(original, "draft");
  setup.controller.flushAll();
  const entry = setup.controller.entries(original)[0];
  const changed = recoveryContext({
    contextKey: fixedHex("1", 64),
    sourceBlobSha: fixedHex("2", 40)
  });

  assert.equal(setup.controller.classify(entry, changed).restorable, false);
  assert.equal(
    setup.controller.classify(entry, changed).reason,
    "The source blob changed."
  );
});

test("persisted body mismatch blocks direct restore", () => {
  const setup = newController();
  const original = recoveryContext();
  setup.controller.capture(original, "draft");
  setup.controller.flushAll();
  const entry = setup.controller.entries(original)[0];
  const changed = recoveryContext({
    contextKey: fixedHex("1", 64),
    baseBodySha256: fixedHex("2", 64)
  });

  assert.equal(setup.controller.classify(entry, changed).restorable, false);
  assert.equal(
    setup.controller.classify(entry, changed).reason,
    "The persisted Markdown changed."
  );
});

test("enrollment context mismatch blocks direct restore", () => {
  const setup = newController();
  const original = recoveryContext();
  setup.controller.capture(original, "draft");
  setup.controller.flushAll();
  const entry = setup.controller.entries(original)[0];
  const changed = recoveryContext({ contextKey: fixedHex("1", 64) });

  assert.equal(setup.controller.classify(entry, changed).restorable, false);
  assert.equal(
    setup.controller.classify(entry, changed).reason,
    "The artifact enrollment changed."
  );
});

test("every context mismatch blocks the direct restore path", () => {
  const setup = newController();
  const original = recoveryContext();
  setup.controller.capture(original, "draft");
  setup.controller.flushAll();
  const entry = setup.controller.entries(original)[0];
  const variants = [
    recoveryContext({ sourceCommit: fixedHex("1", 40) }),
    recoveryContext({ sourceBlobSha: fixedHex("1", 40) }),
    recoveryContext({ baseBodySha256: fixedHex("1", 64) }),
    recoveryContext({ baseRecordBlobSha: fixedHex("1", 40) }),
    recoveryContext({ contextKey: fixedHex("1", 64) }),
    recoveryContext({ editable: false })
  ];

  variants.forEach((context) => {
    let inputEvents = 0;
    const textarea = {
      value: "persisted",
      dispatchEvent() { inputEvents += 1; }
    };
    assert.equal(restoreEntry(entry, context, textarea, Event), false);
    assert.equal(textarea.value, "persisted");
    assert.equal(inputEvents, 0);
  });
});

test("entries expire at the exact 30-day boundary", () => {
  const currentDate = new Date("2026-08-31T12:00:00Z");
  const thirtyDaysMs = 30 * 24 * 60 * 60 * 1000;
  assert.equal(constants.ttlMs, thirtyDaysMs);
  const context = recoveryContext();
  const retainedStorage = new MemoryStorage();
  const retained = newController({
    storage: retainedStorage,
    date: new Date(currentDate.getTime() - thirtyDaysMs + 1)
  });
  retained.controller.capture(context, "retained draft");
  retained.controller.flushAll();
  const retainedCurrent = newController({ storage: retainedStorage, date: currentDate });
  assert.equal(retainedCurrent.controller.entries(context).length, 1);

  const expiredStorage = new MemoryStorage();
  const expired = newController({
    storage: expiredStorage,
    date: new Date(currentDate.getTime() - thirtyDaysMs)
  });
  expired.controller.capture(context, "expired draft");
  expired.controller.flushAll();
  const expiredCurrent = newController({ storage: expiredStorage, date: currentDate });
  assert.equal(expiredCurrent.controller.entries(context).length, 0);
  assert.equal(expiredStorage.length, 0);
});

test("read-only contexts cannot create active recovery state", () => {
  const setup = newController();
  const context = recoveryContext({ editable: false });
  const key = setup.controller.capture(context, "must not persist");

  assert.equal(key, null);
  setup.controller.flushAll();
  assert.equal(setup.storage.length, 0);
});

test("read-only contexts can list stale drafts without restoring them", () => {
  const setup = newController();
  const editable = recoveryContext();
  setup.controller.capture(editable, "draft to export");
  setup.controller.flushAll();
  const readOnly = recoveryContext({ editable: false });

  const entries = setup.controller.entries(readOnly);
  assert.equal(entries.length, 1);
  assert.equal(setup.controller.classify(entries[0], readOnly).restorable, false);
  assert.equal(entries[0].record.markdown_body, "draft to export");
});

test("failed storage flush preserves pending recovery", () => {
  const setup = newController();
  const context = recoveryContext();
  setup.storage.failWrites = true;
  const key = setup.controller.capture(context, "pending after failure");

  assert.equal(setup.controller.flushAll(), false);
  assert.equal(setup.controller.hasPending(key), true);
  assert.equal(setup.storage.length, 0);
});

test("two tabs preserve separate drafts for the same context", () => {
  const storage = new MemoryStorage();
  const first = newController({ storage, tabStorage: new MemoryStorage() });
  const second = newController({ storage, tabStorage: new MemoryStorage() });
  const context = recoveryContext();
  first.controller.capture(context, "first tab body");
  second.controller.capture(context, "second tab body");
  first.controller.flushAll();
  second.controller.flushAll();

  const entries = first.controller.entries(context);
  assert.equal(entries.length, 2);
  assert.deepEqual(
    new Set(entries.map((entry) => entry.record.markdown_body)),
    new Set(["first tab body", "second tab body"])
  );
  assert.notEqual(entries[0].record.tab_id, entries[1].record.tab_id);
});

test("one tab save acknowledgement does not clear another tab", async () => {
  const storage = new MemoryStorage();
  const first = newController({ storage, tabStorage: new MemoryStorage() });
  const second = newController({ storage, tabStorage: new MemoryStorage() });
  const context = recoveryContext();
  first.controller.capture(context, "same body");
  second.controller.capture(context, "same body");
  first.controller.flushAll();
  second.controller.flushAll();

  await first.controller.acknowledge({
    context_key: context.contextKey,
    saved_body_sha256: await first.controller.sha256("same body")
  });
  const remaining = second.controller.entries(context);
  assert.equal(remaining.length, 1);
  assert.equal(remaining[0].record.tab_id, second.controller.tabId);
});

test("a duplicated tab rotates the cloned sessionStorage identifier", () => {
  const storage = new MemoryStorage();
  const clonedTabStorage = new MemoryStorage();
  clonedTabStorage.setItem("gmd-review-draft:tab-id", "cloned-tab-id");
  const first = newController({ storage, tabStorage: clonedTabStorage });
  const second = newController({ storage, tabStorage: clonedTabStorage });
  const context = recoveryContext();
  first.controller.capture(context, "first duplicated tab");
  second.controller.capture(context, "second duplicated tab");
  first.controller.flushAll();
  second.controller.flushAll();

  assert.notEqual(first.controller.tabId, second.controller.tabId);
  assert.equal(first.controller.entries(context).length, 2);
});

test("browser runtime requires explicit restore and wires discard and dirty guards", () => {
  const runtime = loadBrowserRuntime();
  const context = recoveryContext();
  const controls = runtime.setContext(context);
  assert.deepEqual(
    Array.from(runtime.shinyHandlers.keys()).sort(),
    [
      "review-dirty-state",
      "review-draft-saved",
      "review-focus-help",
      "review-toggle-button"
    ]
  );

  runtime.textarea.value = "Recovered <script>text</script>";
  runtime.textarea.dispatchEvent(new runtime.windowObject.Event("input", {
    bubbles: true
  }));
  runtime.dispatchWindow("pagehide", {});
  runtime.textarea.value = "Persisted body";
  runtime.dispatchWindow("storage", {
    key: Array.from(runtime.localStorage.values.keys())[0]
  });
  assert.equal(runtime.textarea.value, "Persisted body");
  assert.equal(controls.restore.hidden, false);

  runtime.click(controls.restore);
  assert.equal(runtime.textarea.value, "Recovered <script>text</script>");
  assert.equal(runtime.textarea.innerHTML, "unchanged");
  assert.equal(runtime.inputEvents >= 2, true);
  runtime.click(controls.discard);
  assert.equal(runtime.localStorage.length, 0);

  runtime.shinyHandlers.get("review-dirty-state")({ dirty: true });
  const guarded = {
    closest(selector) {
      return selector === ".dirty-navigation-guard" ? guarded : null;
    }
  };
  const navigation = runtime.click(guarded);
  assert.equal(runtime.confirmCalls, 1);
  assert.equal(navigation.prevented, true);
  assert.equal(navigation.stopped, true);

  const dirtyUnload = {
    prevented: false,
    preventDefault() { this.prevented = true; },
    returnValue: null
  };
  runtime.dispatchWindow("beforeunload", dirtyUnload);
  assert.equal(dirtyUnload.prevented, true);
  assert.equal(dirtyUnload.returnValue, "");

  runtime.setConfirmResult(true);
  const confirmedNavigation = runtime.click(guarded);
  assert.equal(runtime.confirmCalls, 2);
  assert.equal(confirmedNavigation.prevented, false);
  assert.equal(confirmedNavigation.stopped, false);

  const cleanNavigation = runtime.click(guarded);
  assert.equal(runtime.confirmCalls, 2);
  assert.equal(cleanNavigation.prevented, false);

  const cleanUnload = {
    prevented: false,
    preventDefault() { this.prevented = true; },
    returnValue: null
  };
  runtime.dispatchWindow("beforeunload", cleanUnload);
  assert.equal(cleanUnload.prevented, false);
  assert.equal(cleanUnload.returnValue, null);
});

test("browser save acknowledgement handler clears only a matching entry", async () => {
  const runtime = loadBrowserRuntime();
  const context = recoveryContext();
  runtime.setContext(context);
  runtime.textarea.value = "acknowledged body";
  runtime.textarea.dispatchEvent(new runtime.windowObject.Event("input", {
    bubbles: true
  }));
  runtime.dispatchWindow("pagehide", {});
  const handler = runtime.shinyHandlers.get("review-draft-saved");

  handler({
    context_key: context.contextKey,
    saved_body_sha256: fixedHex("0", 64)
  });
  await new Promise((resolve) => setImmediate(resolve));
  assert.equal(runtime.localStorage.length, 1);

  const digest = await webcrypto.subtle.digest(
    "SHA-256",
    new TextEncoder().encode("acknowledged body")
  );
  const savedBodySha256 = Array.from(new Uint8Array(digest), (byte) =>
    byte.toString(16).padStart(2, "0")).join("");
  handler({
    context_key: context.contextKey,
    saved_body_sha256: savedBodySha256
  });
  await new Promise((resolve) => setTimeout(resolve, 20));
  assert.equal(runtime.localStorage.length, 0);
});

test("stale browser controls copy and export exact Markdown", async () => {
  const runtime = loadBrowserRuntime();
  const editable = recoveryContext();
  runtime.setContext(editable);
  runtime.textarea.value = "stale <b>Markdown</b>";
  runtime.textarea.dispatchEvent(new runtime.windowObject.Event("input", {
    bubbles: true
  }));
  runtime.dispatchWindow("pagehide", {});
  const controls = runtime.setContext(
    recoveryContext({ editable: false }),
    "Persisted body"
  );
  runtime.dispatchWindow("storage", {
    key: Array.from(runtime.localStorage.values.keys())[0]
  });

  assert.equal(controls.restore.hidden, true);
  runtime.click(controls.copy);
  assert.deepEqual(runtime.clipboardWrites, ["stale <b>Markdown</b>"]);
  runtime.click(controls.export);
  assert.equal(runtime.downloads.length, 1);
  assert.equal(runtime.downloads[0].download, "review-draft-recovery.md");
  assert.equal(
    await runtime.downloads[0].blob.text(),
    "stale <b>Markdown</b>"
  );
});

test("browser runtime blocks navigation when recovery storage fails", async () => {
  const runtime = loadBrowserRuntime();
  const context = recoveryContext();
  const controls = runtime.setContext(context);
  runtime.localStorage.failWrites = true;
  runtime.textarea.value = "cannot persist";
  runtime.textarea.dispatchEvent(new runtime.windowObject.Event("input", {
    bubbles: true
  }));
  runtime.dispatchWindow("pagehide", {});
  runtime.shinyHandlers.get("review-dirty-state")({ dirty: true });
  const guarded = {
    closest(selector) {
      return selector === ".dirty-navigation-guard" ? guarded : null;
    }
  };

  const navigation = runtime.click(guarded);
  assert.equal(navigation.prevented, true);
  assert.equal(navigation.stopped, true);
  assert.equal(runtime.alertCalls, 1);
  assert.equal(runtime.confirmCalls, 0);
  assert.equal(runtime.panel.hidden, false);
  runtime.click(controls.export);
  assert.equal(runtime.downloads.length, 1);
  assert.equal(await runtime.downloads[0].blob.text(), "cannot persist");
});
