(function () {
  "use strict";

  var dirty = false;
  var shinyHandlersRegistered = false;

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

    Shiny.addCustomMessageHandler("review-toggle-button", function (message) {
      var button = document.getElementById(message.id);
      if (!button) return;
      button.disabled = Boolean(message.disabled);
      button.setAttribute("aria-busy", message.disabled ? "true" : "false");
    });

    Shiny.addCustomMessageHandler("review-focus-help", focusModal);
  }

  document.addEventListener("DOMContentLoaded", function () {
    var root = reviewRoot();
    if (root) root.classList.add("js-enabled");
    registerShinyHandlers();

    document.addEventListener("click", function (event) {
      var tab = event.target.closest(".workspace-tab");
      if (tab) activateTab(tab);

      var guarded = event.target.closest(".dirty-navigation-guard");
      if (guarded && dirty) {
        var leave = window.confirm(
          "You have unsaved changes. Leave this artifact and discard them?"
        );
        if (!leave) {
          event.preventDefault();
          event.stopImmediatePropagation();
        } else {
          setDirty(false);
        }
      }
    }, true);

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
      if (!dirty) return;
      event.preventDefault();
      event.returnValue = "";
    });

    var observerPending = false;
    var observer = new MutationObserver(function () {
      if (observerPending) return;
      observerPending = true;
      requestAnimationFrame(function () {
        observerPending = false;
        prepareQueueRows();
      });
    });
    var queueTarget = document.querySelector(".review-queue-table") || document.body;
    observer.observe(queueTarget, { childList: true, subtree: true });
    prepareQueueRows();
  });

  document.addEventListener("shiny:connected", registerShinyHandlers);
  window.setTimeout(registerShinyHandlers, 0);
})();
