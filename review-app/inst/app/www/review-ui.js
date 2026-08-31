(function () {
  "use strict";

  var RECOVERY_SCHEMA_VERSION = 1;
  var RECOVERY_PREFIX = "gmd-review-draft:v1:";
  var RECOVERY_TTL_MS = 30 * 24 * 60 * 60 * 1000;
  var RECOVERY_DEBOUNCE_MS = 250;
  var TAB_ID_KEY = "gmd-review-draft:tab-id";
  var HEX_40 = /^[0-9a-f]{40}$/;
  var HEX_64 = /^[0-9a-f]{64}$/;

  function createDraftRecovery(options) {
    var storage = options.storage;
    var tabStorage = options.tabStorage;
    var cryptoApi = options.crypto;
    var textEncoder = options.textEncoder;
    var setTimer = options.setTimeout;
    var clearTimer = options.clearTimeout;
    var now = options.now;
    var onChange = options.onChange || function () {};
    var onError = options.onError || function () {};
    var pending = new Map();
    var tabId = loadTabId();

    function randomTabId() {
      if (cryptoApi && typeof cryptoApi.randomUUID === "function") {
        return cryptoApi.randomUUID();
      }
      if (cryptoApi && typeof cryptoApi.getRandomValues === "function") {
        var bytes = new Uint8Array(16);
        cryptoApi.getRandomValues(bytes);
        return Array.prototype.map.call(bytes, function (byte) {
          return byte.toString(16).padStart(2, "0");
        }).join("");
      }
      return String(Date.now()) + "-" + Math.random().toString(36).slice(2);
    }

    function loadTabId() {
      // opener tabs can clone sessionStorage, so rotate on every document load.
      var generated = randomTabId();
      try {
        tabStorage.setItem(TAB_ID_KEY, generated);
      } catch (error) {
        // The in-memory ID still isolates this document when storage is blocked.
      }
      return generated;
    }

    function validContext(context) {
      return Boolean(
        context && typeof context.editable === "boolean" &&
        context.schemaVersion === RECOVERY_SCHEMA_VERSION &&
        HEX_64.test(context.lookupKey || "") &&
        HEX_64.test(context.contextKey || "") &&
        HEX_40.test(context.sourceCommit || "") &&
        HEX_40.test(context.sourceBlobSha || "") &&
        HEX_64.test(context.baseBodySha256 || "") &&
        HEX_40.test(context.baseRecordBlobSha || "")
      );
    }

    function storageKey(context, entryTabId) {
      if (!validContext(context)) return null;
      return RECOVERY_PREFIX + [
        context.lookupKey,
        context.contextKey,
        entryTabId || tabId
      ].join(":");
    }

    function parseStorageKey(key) {
      if (typeof key !== "string" || key.indexOf(RECOVERY_PREFIX) !== 0) {
        return null;
      }
      var parts = key.slice(RECOVERY_PREFIX.length).split(":");
      if (parts.length !== 3 || !HEX_64.test(parts[0]) ||
          !HEX_64.test(parts[1]) || !parts[2] || parts[2].length > 128) {
        return null;
      }
      return {
        lookupKey: parts[0],
        contextKey: parts[1],
        tabId: parts[2]
      };
    }

    function validRecord(record, keyParts) {
      return Boolean(
        record && record.recovery_schema_version === RECOVERY_SCHEMA_VERSION &&
        typeof record.markdown_body === "string" &&
        HEX_64.test(record.base_body_sha256 || "") &&
        HEX_40.test(record.base_record_blob_sha || "") &&
        HEX_40.test(record.source_commit || "") &&
        HEX_40.test(record.source_blob_sha || "") &&
        typeof record.saved_at === "string" &&
        Number.isFinite(Date.parse(record.saved_at)) &&
        typeof record.tab_id === "string" && record.tab_id.length <= 128 &&
        keyParts && record.tab_id === keyParts.tabId
      );
    }

    function allStorageKeys() {
      var keys = [];
      try {
        for (var index = 0; index < storage.length; index += 1) {
          keys.push(storage.key(index));
        }
      } catch (error) {
        onError(error);
      }
      return keys.filter(function (key) {
        return typeof key === "string" && key.indexOf(RECOVERY_PREFIX) === 0;
      });
    }

    function removeStored(key) {
      try {
        storage.removeItem(key);
        return true;
      } catch (error) {
        onError(error);
        return false;
      }
    }

    function readEntry(key) {
      var parts = parseStorageKey(key);
      if (!parts) return null;
      try {
        var raw = storage.getItem(key);
        if (raw === null) return null;
        var record = JSON.parse(raw);
        if (!validRecord(record, parts)) return null;
        return { key: key, keyParts: parts, record: record };
      } catch (error) {
        onError(error);
        return null;
      }
    }

    function cleanupExpired() {
      var currentTime = now().getTime();
      var removed = 0;
      allStorageKeys().forEach(function (key) {
        var entry = readEntry(key);
        if (!entry || currentTime - Date.parse(entry.record.saved_at) >=
            RECOVERY_TTL_MS) {
          if (removeStored(key)) removed += 1;
        }
      });
      if (removed) onChange();
      return removed;
    }

    function flushKey(key) {
      var item = pending.get(key);
      if (!item) return false;
      if (item.timer !== null) clearTimer(item.timer);
      try {
        var serialized = JSON.stringify(item.record);
        storage.setItem(key, serialized);
        if (storage.getItem(key) !== serialized) {
          throw new Error("Browser recovery write could not be verified");
        }
        pending.delete(key);
        onChange();
        return true;
      } catch (error) {
        item.timer = null;
        pending.set(key, item);
        onError(error);
        return false;
      }
    }

    function capture(context, markdownBody) {
      if (!validContext(context) || !context.editable ||
          typeof markdownBody !== "string") {
        return null;
      }
      var key = storageKey(context);
      var previous = pending.get(key);
      if (previous && previous.timer !== null) clearTimer(previous.timer);
      var record = {
        recovery_schema_version: RECOVERY_SCHEMA_VERSION,
        markdown_body: markdownBody,
        base_body_sha256: context.baseBodySha256,
        base_record_blob_sha: context.baseRecordBlobSha,
        source_commit: context.sourceCommit,
        source_blob_sha: context.sourceBlobSha,
        saved_at: now().toISOString(),
        tab_id: tabId
      };
      var timer = setTimer(function () {
        flushKey(key);
      }, RECOVERY_DEBOUNCE_MS);
      pending.set(key, { record: record, timer: timer });
      return key;
    }

    function flushAll() {
      return Array.from(pending.keys()).map(flushKey).every(Boolean);
    }

    function entries(context) {
      if (!validContext(context)) return [];
      cleanupExpired();
      return allStorageKeys().map(readEntry).filter(function (entry) {
        return entry && entry.keyParts.lookupKey === context.lookupKey;
      }).sort(function (left, right) {
        return Date.parse(right.record.saved_at) -
          Date.parse(left.record.saved_at);
      });
    }

    function classify(entry, context) {
      if (!validContext(context)) {
        return { restorable: false, reason: "Recovery context is unavailable." };
      }
      return recoveryCompatibility(entry, context);
    }

    function discard(key) {
      var item = pending.get(key);
      if (item && item.timer !== null) clearTimer(item.timer);
      pending.delete(key);
      var removed = removeStored(key);
      if (removed) onChange();
      return removed;
    }

    function sha256(text) {
      if (!cryptoApi || !cryptoApi.subtle || !textEncoder) {
        return Promise.resolve(null);
      }
      return cryptoApi.subtle.digest(
        "SHA-256",
        textEncoder.encode(text)
      ).then(function (buffer) {
        return Array.prototype.map.call(new Uint8Array(buffer), function (byte) {
          return byte.toString(16).padStart(2, "0");
        }).join("");
      });
    }

    function acknowledge(message) {
      if (!message || !HEX_64.test(message.context_key || "") ||
          !HEX_64.test(message.saved_body_sha256 || "")) {
        return Promise.resolve(0);
      }
      Array.from(pending.keys()).forEach(function (key) {
        var parts = parseStorageKey(key);
        if (parts && parts.contextKey === message.context_key &&
            parts.tabId === tabId) {
          flushKey(key);
        }
      });
      var candidates = allStorageKeys().map(readEntry).filter(function (entry) {
        return entry && entry.keyParts.contextKey === message.context_key &&
          entry.keyParts.tabId === tabId;
      });
      return Promise.all(candidates.map(function (entry) {
        return sha256(entry.record.markdown_body).then(function (digest) {
          if (digest !== message.saved_body_sha256) return 0;
          if (pending.has(entry.key)) return 0;
          var current = readEntry(entry.key);
          if (!current || JSON.stringify(current.record) !==
              JSON.stringify(entry.record)) {
            return 0;
          }
          if (!removeStored(entry.key)) return 0;
          onChange();
          return 1;
        });
      })).then(function (counts) {
        return counts.reduce(function (total, count) {
          return total + count;
        }, 0);
      });
    }

    return {
      acknowledge: acknowledge,
      capture: capture,
      classify: classify,
      cleanupExpired: cleanupExpired,
      discard: discard,
      entries: entries,
      flushAll: flushAll,
      flushKey: flushKey,
      hasPending: function (key) { return pending.has(key); },
      parseStorageKey: parseStorageKey,
      sha256: sha256,
      storageKey: storageKey,
      tabId: tabId
    };
  }

  function recoveryCompatibility(entry, context) {
    if (!entry || !context) {
      return { restorable: false, reason: "Recovery context is unavailable." };
    }
    if (entry.record.source_commit !== context.sourceCommit) {
      return { restorable: false, reason: "The source revision changed." };
    }
    if (entry.record.source_blob_sha !== context.sourceBlobSha) {
      return { restorable: false, reason: "The source blob changed." };
    }
    if (entry.record.base_body_sha256 !== context.baseBodySha256) {
      return { restorable: false, reason: "The persisted Markdown changed." };
    }
    if (entry.record.base_record_blob_sha !== context.baseRecordBlobSha) {
      return { restorable: false, reason: "The persisted review record changed." };
    }
    if (entry.keyParts.contextKey !== context.contextKey) {
      return { restorable: false, reason: "The artifact enrollment changed." };
    }
    if (!context.editable) {
      return { restorable: false, reason: "The artifact is no longer editable." };
    }
    return { restorable: true, reason: null };
  }

  function registerDraftInputCapture(documentObject, controller, readContext) {
    var handler = function (event) {
      var context = readContext();
      var target = event.target;
      if (!context || !context.editable || !target ||
          target.id !== context.editorId || typeof target.value !== "string") {
        return;
      }
      controller.capture(context, target.value);
    };
    documentObject.addEventListener("input", handler, true);
    return handler;
  }

  function restoreEntry(entry, context, textarea, EventConstructor) {
    if (!entry || !context || !textarea) return false;
    if (!recoveryCompatibility(entry, context).restorable) return false;
    textarea.value = entry.record.markdown_body;
    textarea.dispatchEvent(new EventConstructor("input", { bubbles: true }));
    return true;
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = {
      createDraftRecovery: createDraftRecovery,
      registerDraftInputCapture: registerDraftInputCapture,
      restoreEntry: restoreEntry,
      constants: {
        prefix: RECOVERY_PREFIX,
        schemaVersion: RECOVERY_SCHEMA_VERSION,
        ttlMs: RECOVERY_TTL_MS
      }
    };
  }

  if (typeof window === "undefined" || typeof document === "undefined") return;

  var dirty = false;
  var shinyHandlersRegistered = false;
  var recoveryRefreshPending = false;
  var recoveryStorageUnavailable = false;

  function unavailableStorage() {
    return {
      get length() { return 0; },
      getItem: function () { return null; },
      key: function () { return null; },
      removeItem: function () {},
      setItem: function () {
        throw new Error("Browser storage is unavailable");
      }
    };
  }

  function browserStorage(name) {
    try {
      return window[name] || unavailableStorage();
    } catch (error) {
      return unavailableStorage();
    }
  }

  var recoveryController = createDraftRecovery({
    storage: browserStorage("localStorage"),
    tabStorage: browserStorage("sessionStorage"),
    crypto: window.crypto,
    textEncoder: window.TextEncoder ? new window.TextEncoder() : null,
    setTimeout: window.setTimeout.bind(window),
    clearTimeout: window.clearTimeout.bind(window),
    now: function () { return new Date(); },
    onChange: scheduleRecoveryRefresh,
    onError: showRecoveryStorageError
  });

  function reviewRoot() {
    return document.querySelector(".review-app");
  }

  function setDirty(nextDirty) {
    dirty = Boolean(nextDirty);
    var root = reviewRoot();
    if (root) {
      root.dataset.dirty = dirty ? "true" : "false";
    }
  }

  function activeRecoveryPanel() {
    return document.querySelector(".draft-recovery-panel");
  }

  function readRecoveryContext() {
    var panel = activeRecoveryPanel();
    if (!panel) return null;
    return {
      editable: panel.dataset.recoveryEditable === "true",
      schemaVersion: Number(panel.dataset.recoverySchemaVersion),
      lookupKey: panel.dataset.recoveryLookupKey,
      contextKey: panel.dataset.recoveryContextKey,
      sourceCommit: panel.dataset.recoverySourceCommit,
      sourceBlobSha: panel.dataset.recoverySourceBlobSha,
      baseBodySha256: panel.dataset.recoveryBaseBodySha256,
      baseRecordBlobSha: panel.dataset.recoveryBaseRecordBlobSha,
      editorId: panel.dataset.recoveryEditorId
    };
  }

  function scheduleRecoveryRefresh() {
    if (recoveryRefreshPending) return;
    recoveryRefreshPending = true;
    window.requestAnimationFrame(function () {
      recoveryRefreshPending = false;
      refreshRecoveryPanel();
    });
  }

  function showRecoveryStorageError() {
    recoveryStorageUnavailable = true;
    var panel = activeRecoveryPanel();
    if (!panel) return;
    panel.hidden = false;
    panel.classList.add("recovery-error");
    var status = panel.querySelector(".draft-recovery-status");
    if (status) {
      status.textContent =
        "Browser recovery storage is unavailable. Save or export before leaving.";
    }
  }

  function selectedRecoveryEntry(panel, context) {
    var select = panel.querySelector(".draft-recovery-select");
    var selectedKey = select ? select.value : "";
    var entries = recoveryController.entries(context);
    return entries.find(function (entry) {
      return entry.key === selectedKey;
    }) || entries[0] || null;
  }

  function clearSelect(select) {
    while (select.firstChild) select.removeChild(select.firstChild);
  }

  function refreshRecoveryPanel() {
    var panel = activeRecoveryPanel();
    var context = readRecoveryContext();
    if (!panel || !context) return;
    var select = panel.querySelector(".draft-recovery-select");
    var restore = panel.querySelector(".draft-recovery-restore");
    var discard = panel.querySelector(".draft-recovery-discard");
    var copy = panel.querySelector(".draft-recovery-copy-button");
    var exportButton = panel.querySelector(".draft-recovery-export");
    var status = panel.querySelector(".draft-recovery-status");
    if (recoveryStorageUnavailable) {
      panel.hidden = false;
      panel.classList.add("recovery-error");
      select.hidden = true;
      restore.hidden = true;
      discard.hidden = true;
      copy.hidden = true;
      exportButton.hidden = false;
      status.textContent =
        "Browser recovery storage is unavailable. Save or export before leaving.";
      return;
    }
    var entries = recoveryController.entries(context);
    if (!entries.length) {
      panel.hidden = true;
      if (select) clearSelect(select);
      return;
    }

    var previousKey = select ? select.value : "";
    clearSelect(select);
    entries.forEach(function (entry) {
      var option = document.createElement("option");
      var location = entry.record.tab_id === recoveryController.tabId ?
        "this tab" : "another tab";
      option.value = entry.key;
      option.textContent = new Date(entry.record.saved_at).toLocaleString() +
        " (" + location + ")";
      select.appendChild(option);
    });
    if (entries.some(function (entry) { return entry.key === previousKey; })) {
      select.value = previousKey;
    }

    var entry = selectedRecoveryEntry(panel, context);
    var classification = recoveryController.classify(entry, context);
    var textarea = document.getElementById(context.editorId);
    var alreadyShown = textarea &&
      textarea.value === entry.record.markdown_body;
    panel.hidden = false;
    select.hidden = false;
    discard.hidden = false;
    copy.hidden = false;
    exportButton.hidden = false;
    panel.classList.toggle("recovery-stale", !classification.restorable);
    panel.classList.remove("recovery-error");
    restore.hidden = !classification.restorable || alreadyShown;
    if (!classification.restorable) {
      status.textContent = "A stale browser draft is available. " +
        classification.reason + " Copy or export it for manual comparison.";
    } else if (alreadyShown) {
      status.textContent = "Browser recovery is active for the text in this editor.";
    } else {
      status.textContent =
        "A matching browser draft is available. Restore it or discard it.";
    }
  }

  function activateTab(button) {
    var root = button.closest(".content-workspace");
    if (!root) return;
    var target = button.getAttribute("data-review-tab");
    root.querySelectorAll(".workspace-tab").forEach(function (tab) {
      var active = tab === button;
      tab.classList.toggle("active", active);
      tab.setAttribute("aria-selected", active ? "true" : "false");
      tab.setAttribute("tabindex", active ? "0" : "-1");
    });
    root.querySelectorAll(".workspace-panel").forEach(function (panel) {
      panel.classList.toggle(
        "active",
        panel.classList.contains(target + "-panel")
      );
    });
  }

  function prepareQueueRows() {
    document.querySelectorAll(".review-queue-table tbody tr").forEach(function (row) {
      if (!row.hasAttribute("tabindex")) row.setAttribute("tabindex", "0");
      if (!row.hasAttribute("aria-label")) {
        var artifact = row.querySelector("td:nth-child(2)");
        row.setAttribute(
          "aria-label",
          "Open artifact " + (artifact ? artifact.textContent.trim() : "")
        );
      }
    });
  }

  function focusModal() {
    window.setTimeout(function () {
      var modal = document.querySelector(".modal.show");
      if (!modal) return;
      var title = modal.querySelector(".modal-title");
      if (title) {
        title.setAttribute("tabindex", "-1");
        title.focus();
      }
    }, 60);
  }

  function registerShinyHandlers() {
    if (shinyHandlersRegistered || !window.Shiny) return;
    shinyHandlersRegistered = true;

    Shiny.addCustomMessageHandler("review-dirty-state", function (message) {
      setDirty(message.dirty);
    });

    Shiny.addCustomMessageHandler("review-draft-saved", function (message) {
      recoveryController.acknowledge(message).then(scheduleRecoveryRefresh);
    });

    Shiny.addCustomMessageHandler("review-toggle-button", function (message) {
      var button = document.getElementById(message.id);
      if (!button) return;
      button.disabled = Boolean(message.disabled);
      button.setAttribute("aria-busy", message.disabled ? "true" : "false");
    });

    Shiny.addCustomMessageHandler("review-focus-help", focusModal);
  }

  function copyRecovery(entry, panel) {
    var status = panel.querySelector(".draft-recovery-status");
    if (!navigator.clipboard || !navigator.clipboard.writeText) {
      status.textContent = "Clipboard access is unavailable. Use Export instead.";
      return;
    }
    navigator.clipboard.writeText(entry.record.markdown_body).then(function () {
      status.textContent = "The selected Markdown draft was copied.";
    }, function () {
      status.textContent = "The browser did not permit clipboard access.";
    });
  }

  function exportRecovery(entry) {
    var blob = new Blob(
      [entry.record.markdown_body],
      { type: "text/markdown;charset=utf-8" }
    );
    var link = document.createElement("a");
    var url = URL.createObjectURL(blob);
    link.href = url;
    link.download = "review-draft-recovery.md";
    link.click();
    window.setTimeout(function () { URL.revokeObjectURL(url); }, 0);
  }

  function handleRecoveryClick(event) {
    var button = event.target.closest(
      ".draft-recovery-restore, .draft-recovery-discard, " +
      ".draft-recovery-copy-button, .draft-recovery-export"
    );
    if (!button) return false;
    var panel = button.closest(".draft-recovery-panel");
    var context = readRecoveryContext();
    var entry = selectedRecoveryEntry(panel, context);
    event.preventDefault();
    if (!entry) {
      if (button.classList.contains("draft-recovery-export")) {
        var currentEditor = document.getElementById(context.editorId);
        if (currentEditor) {
          exportRecovery({ record: { markdown_body: currentEditor.value } });
        }
      }
      return true;
    }
    if (button.classList.contains("draft-recovery-restore")) {
      var textarea = document.getElementById(context.editorId);
      restoreEntry(entry, context, textarea, window.Event);
    } else if (button.classList.contains("draft-recovery-discard")) {
      recoveryController.discard(entry.key);
    } else if (button.classList.contains("draft-recovery-copy-button")) {
      copyRecovery(entry, panel);
    } else if (button.classList.contains("draft-recovery-export")) {
      exportRecovery(entry);
    }
    scheduleRecoveryRefresh();
    return true;
  }

  function nodeContainsRecoverySurface(node) {
    if (!node || node.nodeType !== 1) return false;
    if (node.matches(".draft-recovery-panel, .editor-panel textarea")) return true;
    return Boolean(node.querySelector(
      ".draft-recovery-panel, .editor-panel textarea"
    ));
  }

  document.addEventListener("DOMContentLoaded", function () {
    var root = reviewRoot();
    if (root) root.classList.add("js-enabled");
    registerShinyHandlers();
    registerDraftInputCapture(document, recoveryController, readRecoveryContext);

    document.addEventListener("click", function (event) {
      if (handleRecoveryClick(event)) return;
      var tab = event.target.closest(".workspace-tab");
      if (tab) activateTab(tab);

      var guarded = event.target.closest(".dirty-navigation-guard");
      if (guarded && dirty) {
        if (!recoveryController.flushAll()) {
          showRecoveryStorageError();
          window.alert(
            "Browser recovery is unavailable. Save or export before leaving."
          );
          event.preventDefault();
          event.stopImmediatePropagation();
          return;
        }
        var leave = window.confirm(
          "You have unsaved changes. Leave this artifact? " +
          "Any available browser recovery will remain local."
        );
        if (!leave) {
          event.preventDefault();
          event.stopImmediatePropagation();
        } else {
          recoveryController.flushAll();
          setDirty(false);
        }
      }
    }, true);

    document.addEventListener("change", function (event) {
      if (event.target.closest(".draft-recovery-select")) {
        refreshRecoveryPanel();
      }
    });

    document.addEventListener("keydown", function (event) {
      var tab = event.target.closest(".workspace-tab");
      if (tab && (event.key === "ArrowLeft" || event.key === "ArrowRight")) {
        var tabs = Array.prototype.slice.call(
          tab.parentElement.querySelectorAll(".workspace-tab")
        );
        var index = tabs.indexOf(tab);
        var offset = event.key === "ArrowRight" ? 1 : -1;
        var next = tabs[(index + offset + tabs.length) % tabs.length];
        activateTab(next);
        next.focus();
        event.preventDefault();
      }

      var row = event.target.closest(".review-queue-table tbody tr");
      if (row && (event.key === "Enter" || event.key === " ")) {
        row.click();
        event.preventDefault();
      }
    });

    window.addEventListener("beforeunload", function (event) {
      recoveryController.flushAll();
      if (!dirty) return;
      event.preventDefault();
      event.returnValue = "";
    });

    window.addEventListener("pagehide", function () {
      recoveryController.flushAll();
    });

    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "hidden") {
        recoveryController.flushAll();
      }
    });

    window.addEventListener("storage", function (event) {
      if (event.key && event.key.indexOf(RECOVERY_PREFIX) === 0) {
        scheduleRecoveryRefresh();
      }
    });

    var queuePending = false;
    var queueObserver = new MutationObserver(function () {
      if (queuePending) return;
      queuePending = true;
      window.requestAnimationFrame(function () {
        queuePending = false;
        prepareQueueRows();
      });
    });
    var queueTarget = document.querySelector(".review-queue-table") || document.body;
    queueObserver.observe(queueTarget, { childList: true, subtree: true });

    var recoveryObserver = new MutationObserver(function (mutations) {
      var changed = mutations.some(function (mutation) {
        return Array.prototype.some.call(
          mutation.addedNodes,
          nodeContainsRecoverySurface
        );
      });
      if (changed) scheduleRecoveryRefresh();
    });
    recoveryObserver.observe(document.body, { childList: true, subtree: true });
    recoveryController.cleanupExpired();
    prepareQueueRows();
    scheduleRecoveryRefresh();
  });

  document.addEventListener("shiny:connected", registerShinyHandlers);
  window.setTimeout(registerShinyHandlers, 0);
})();
