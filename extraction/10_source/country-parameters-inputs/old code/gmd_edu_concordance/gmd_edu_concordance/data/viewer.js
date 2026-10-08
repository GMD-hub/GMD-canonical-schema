(function () {
  "use strict";
  var MODE = window.__MODE__ || "embed";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var esc = function (s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  };

  /* ---------- state ----------
     `source` says where the data on screen came from, and `reload` is the
     function that goes back to that same place and reads it again. A viewer
     you cannot re-read is a screenshot. */
  var state = { iso: null, domain: null, tab: "view" };
  var who = "";
  try { who = localStorage.getItem("gmdcv-who") || ""; } catch (e) {}
  var source = { kind: MODE, label: "", root: "", reload: null };
  var countries = {};
  var isoList = [];
  var artefacts = {};   // iso3 -> [{name, rel, size, read()}]

  var DOM_ORDER = ["education", "water", "sanitation"];
  var DOM_LABEL = { education: "Education", water: "Water", sanitation: "Sanitation" };
  var DOM_SYS = { education: "System 8", water: "System 9", sanitation: "System 9" };

  function ingest(bundles) {
    countries = {};
    (bundles || []).forEach(function (b) {
      if (!b || !b.country) return;
      var k = b.country.iso3 || "??";
      (countries[k] = countries[k] || { iso3: k, name: b.country.name, doms: {} })
        .doms[b.domain] = b;
    });
    isoList = Object.keys(countries).sort();
  }

  function verdictPill(v, counts) {
    var cls = v === "blocked" ? "er" : v === "awaiting_review" ? "wa" : "";
    var txt = v === "blocked" ? "blocked"
      : v === "awaiting_review" ? counts.WARN + " to review" : "clean";
    return '<span class="pill ' + cls + '">' + esc(txt) + "</span>";
  }

  function stat(n, t) {
    return '<div class="stat"><div class="n">' + esc(n) + '</div><div class="t">' + esc(t) + "</div></div>";
  }
  function kv(k, v) {
    return '<div class="kv"><span class="k">' + esc(k) + '</span><span class="v">' + v + "</span></div>";
  }

  /* ---------- loaders ---------- */
  function jget(url) {
    return fetch(url, { cache: "no-store" }).then(function (r) {
      if (!r.ok) throw new Error(r.status + " " + r.statusText);
      return r.json();
    });
  }

  /* server mode: every request re-reads the folder on disk */
  var serverScan = null;

  /* `dir` is the country folder. "" means every folder under the root, which
     is what you want when comparing countries; null means "whatever was open
     last, else the first one". */
  function loadServer(dir) {
    return jget("/api/scan").then(function (sc) {
      serverScan = sc;
      var list = sc.countries || [];
      if (!list.length) throw new Error("no view bundles under " + sc.root);
      var all = dir === "";
      var pick = null;
      if (!all) {
        list.forEach(function (c) { if (c.dir === dir || c.iso3 === dir) pick = c; });
        pick = pick || list[0];
      }
      var q = all ? "" : pick.dir;
      return jget("/api/bundles?dir=" + encodeURIComponent(q))
        .then(function (bundles) {
          ingest(bundles);
          artefacts = {};
          (all ? list : [pick]).forEach(function (c) {
            artefacts[c.iso3] = (c.files || []).map(function (f) {
              return {
                name: f.name, rel: f.rel, size: f.size,
                read: function () {
                  return jget("/api/raw?rel=" + encodeURIComponent(f.rel))
                    .then(function (d) { return d.text; });
                }
              };
            });
          });
          source = {
            kind: "server", root: sc.root,
            label: all ? "all folders" : (pick.dir || "."),
            folders: list, current: q,
            reload: function () { return loadServer(q); }
          };
        });
    });
  }

  /* folder mode: the browser reads the files the user chose */
  function readAsText(file) {
    return new Promise(function (res, rej) {
      var fr = new FileReader();
      fr.onload = function () { res(fr.result); };
      fr.onerror = function () { rej(fr.error); };
      fr.readAsText(file);
    });
  }

  function loadFiles(fileList, label, reload) {
    var files = Array.prototype.slice.call(fileList || []);
    var views = files.filter(function (f) { return /_view\.json$/.test(f.name); });
    if (!views.length) {
      return Promise.reject(new Error(
        "that folder holds no *_view.json files. Pick a country folder such " +
        "as out/IND, or the out/ folder above it."));
    }
    return Promise.all(views.map(function (f) {
      return readAsText(f).then(function (t) {
        var b = JSON.parse(t);
        b._file = f.name;
        return b;
      });
    })).then(function (bundles) {
      ingest(bundles);
      artefacts = {};
      isoList.forEach(function (iso) {
        artefacts[iso] = files.filter(function (f) {
          return /\.(json|ya?ml|csv|txt|md)$/i.test(f.name) &&
            f.name.indexOf(iso) === 0;
        }).map(function (f) {
          return {
            name: f.name, rel: f.webkitRelativePath || f.name, size: f.size,
            read: function () { return readAsText(f); }
          };
        });
      });
      source = { kind: "folder", label: label, root: "", reload: reload };
    });
  }

  /* Chromium keeps the directory handle, so "reload" really re-reads disk */
  function loadHandle(handle) {
    var files = [];
    function walk(dir, prefix) {
      var out = [];
      return (async function () {
        for await (var entry of dir.values()) {
          if (entry.kind === "file") {
            var f = await entry.getFile();
            f.__rel = prefix + entry.name;
            out.push(f);
          } else if (entry.kind === "directory") {
            out = out.concat(await walk(entry, prefix + entry.name + "/"));
          }
        }
        return out;
      })();
    }
    return walk(handle, "").then(function (fs) {
      files = fs;
      return loadFiles(files, handle.name,
                       function () { return loadHandle(handle); });
    });
  }

  function pickFolder() {
    if (window.showDirectoryPicker) {
      return window.showDirectoryPicker({ mode: "read" })
        .then(loadHandle)
        .catch(function (e) {
          if (e && e.name === "AbortError") return null;
          return fallbackPick();
        });
    }
    return fallbackPick();
  }

  function fallbackPick() {
    return new Promise(function (res) {
      var inp = document.createElement("input");
      inp.type = "file";
      inp.multiple = true;
      inp.webkitdirectory = true;
      inp.onchange = function () {
        var name = "selected folder";
        if (inp.files.length && inp.files[0].webkitRelativePath) {
          name = inp.files[0].webkitRelativePath.split("/")[0];
        }
        res(loadFiles(inp.files, name, null));
      };
      inp.click();
    });
  }

  /* ---------- education ---------- */
  function eduView(b) {
    var eras = b.eras || [], rows = b.rows || [], L = b.ladder || [];
    var byLvl = {};
    rows.forEach(function (r) { (byLvl[r.isced] = byLvl[r.isced] || []).push(r); });

    var h = "";
    h += '<div class="card"><h2><span>' + esc(b.country.name) + " education instructions</span>" +
      '<span class="sub">' + esc(b.frame) + " · " + esc(b.version) + "</span>" +
      verdictPill(b.verdict, b.counts) +
      '<span class="spacer"></span><span class="sub mono">' + esc(b.fingerprint) + "</span></h2>";

    if (b.coverage && b.coverage.gap_before) {
      h += '<div class="note">' + esc(b.country.name) + " is documented for one school year (" +
        esc(b.source.reference_year) + "), so this version is the <b>latest era</b>. " +
        "Cohorts who left school before " + esc(b.coverage.gap_before) +
        " have no rule here and are escalated, never defaulted into the current curriculum. " +
        "The era is chosen from the year a person was last in school, not the survey year.</div>";
    }

    h += '<div class="stats">' +
      stat(b.structure.cycle || "—", "structure") +
      stat(b.structure.ladder_grades || "—", "grades") +
      stat(rows.length, "programmes") +
      stat(b.source.reference_year || "—", "school year") +
      stat((b.language && b.language.rows_with_national_text) || 0, "with national text") +
      "</div>";

    var reg = b.registry || {};
    var known = (reg.eras || []);
    h += '<div class="lbl">Schooling era' +
      (known.length > 1
        ? "s on file for this country — every row below belongs to one of them"
        : " — every row below is valid only inside it") + "</div>" +
      '<div class="eras">';
    if (known.length > 1) {
      known.forEach(function (e) {
        var mine = String(e.era) === String(b.source.reference_year);
        h += '<div class="era' + (mine ? " on" : "") + '"><h3>' +
          esc(e.era) + (mine ? ' <span class="pill ac">this file</span>' : "") +
          "</h3>" +
          '<div class="yr">' + esc(e.from) + " – " + esc(e.to) + "</div>" +
          "<p>" + esc(e.version) + " · " + esc(e.status) + "</p>" +
          '<p style="margin-top:6px;color:var(--tx-3)">' +
          esc(e.to_inferred || "") + "</p>" +
          (e.gap_before ? '<p style="margin-top:4px;color:var(--t-wa)">' +
            "cohorts before " + esc(e.gap_before) + " have no era</p>" : "") +
          "</div>";
      });
    } else {
      eras.forEach(function (e) {
        h += '<div class="era on"><h3>' + esc(e.label || "ISCED 2011 mapping") +
          (e.latest ? ' <span class="pill ac">latest</span>' : "") + "</h3>" +
          '<div class="yr">' + esc(e.from) + " – " + esc(e.to) + "</div>" +
          "<p>" + esc(e.description || "") + "</p>" +
          (e.from_evidence ? '<p style="margin-top:6px;color:var(--tx-3)">' +
            esc(e.from_evidence) + "</p>" : "") +
          "</div>";
      });
    }
    h += "</div>";

    h += '<div class="lbl">Programmes — grades and years derived from theoretical entrance age + duration</div>';
    h += '<div class="scroll"><table class="tbl"><thead><tr>' +
      "<th>National programme</th><th>Grades</th><th>Years in level</th>" +
      "<th>ISCED level</th><th>Cycle completed at</th><th>Years of education</th>" +
      "<th>→ GMD educ_highest</th><th>→ attainment</th></tr></thead><tbody>";
    rows.forEach(function (r) {
      var nat = r.programme_national && r.programme_national !== r.programme
        ? '<span class="nat">' + esc(r.programme_national) + "</span>" : "";
      h += "<tr>" +
        "<td><b>" + esc(r.programme) + "</b>" + nat +
        (r.orientation && r.orientation !== "na"
          ? ' <span class="tag">' + esc(r.orientation) + "</span>" : "") + "</td>" +
        '<td class="mono">' + esc(r.grades_v || "–") + "</td>" +
        '<td class="mono">' + esc(r.years_in_level_v || "–") + "</td>" +
        '<td><span class="num">' + esc(r.isced) + "</span>" + esc(r.isced_label.replace(/^ISCED \d /, "")) + "</td>" +
        "<td>" + esc(r.complete_at || "–") +
        (r.diploma_national && r.diploma_national !== r.complete_at
          ? '<span class="nat">' + esc(r.diploma_national) + "</span>" : "") + "</td>" +
        '<td class="mono">' + esc(r.years_at_completion_v || "–") + "</td>" +
        "<td><code>" + esc(r.gmd) + "</code>" + edited(b, r.programme_id, "gmd") +
        "</td>" +
        "<td>" + (r.attainment_on_completion
          ? '<code>' + esc(r.attainment_on_completion) + "</code>" +
            (r.attainment_in_progress &&
             r.attainment_in_progress !== r.attainment_on_completion
              ? '<span class="nat">part-way: ' +
                esc(r.attainment_in_progress) + "</span>" : "")
          : "—") + "</td>" +
        "</tr>";
    });
    h += "</tbody></table></div></div>";

    h += ladderCard(L);
    return h;
  }

  function ladderCard(L) {
    if (!L.length) return "";
    var h = '<div class="card"><h2><span>Derived grade ladder</span><span class="sub">' +
      "grade → ISCED level → canonical value; this is what a cohort resolves against</span></h2>" +
      '<div class="scroll"><table class="tbl"><thead><tr><th>Grade</th><th>ISCED</th>' +
      "<th>→ GMD</th><th>→ attainment if they left here</th>" +
      "<th>Ends the level</th><th>Cumulative years</th><th>Programme</th>" +
      "<th>Alternatives at this grade</th></tr></thead><tbody>";
    L.forEach(function (s) {
      h += "<tr>" +
        '<td class="mono"><b>' + s.grade + "</b></td>" +
        '<td><span class="num">' + esc(s.isced) + "</span></td>" +
        "<td><code>" + esc(s.gmd) + "</code></td>" +
        "<td><code>" + esc(s.attainment || "—") + "</code>" +
        (s.isced_a ? ' <span class="tag">ISCED-A ' + esc(s.isced_a) + "</span>" : "") +
        "</td>" +
        "<td>" + (s.completes_level ? '<span class="pill">yes</span>' : "") + "</td>" +
        '<td class="mono">' + esc(s.years_at_completion == null ? "–" : s.years_at_completion) + "</td>" +
        "<td>" + esc(s.programme) + "</td>" +
        '<td style="color:var(--tx-2)">' + esc((s.alternatives || []).join("; ")) + "</td>" +
        "</tr>";
    });
    return h + "</tbody></table></div></div>";
  }

  /* the resolver, run client-side against the same ladder the package derived */
  function resolve(b, grade, year) {
    var eras = b.eras || [], out = { grade: grade, year: year };
    if (year != null && !isNaN(year)) {
      var era = null;
      eras.forEach(function (e) { if (year >= e.from && year <= e.to) era = e; });
      if (!era) {
        var lo = Math.min.apply(null, eras.map(function (e) { return e.from; }));
        out.resolved = false;
        out.why = year + " is before " + lo + ", the earliest year this version covers. " +
          "This is escalation ED-01, not a fallback to the latest era.";
        return out;
      }
      out.era = era;
    } else if (eras.length) { out.era = eras[0]; }
    var step = (b.ladder || []).filter(function (s) { return s.grade === grade; })[0];
    if (!step) {
      var gs = (b.ladder || []).map(function (s) { return s.grade; });
      out.resolved = false;
      out.why = "grade " + grade + " is outside the ladder " +
        (gs.length ? Math.min.apply(null, gs) + "–" + Math.max.apply(null, gs) : "?") +
        " this version derives.";
      return out;
    }
    out.resolved = true; out.step = step;
    out.why = "grade " + grade + " sits in " + step.programme + "; " +
      (step.completes_level
        ? "it is the last grade of the level, so the level is completed."
        : "the level is not finished at this grade.");
    return out;
  }

  function resolverCard(b) {
    var ref = b.source.reference_year || 2020;
    var presets = [[1, ref], [6, ref], [9, ref], [12, ref], [6, ref - 30]];
    return '<div class="card"><h2><span>Cohort resolver</span><span class="sub">grade + year last in school → ISCED attainment</span></h2>' +
      '<div class="pad">' +
      '<div class="field"><label>Highest grade completed</label>' +
      '<input class="f" id="rg" type="number" value="6"></div>' +
      '<div class="field"><label>Year last in school</label>' +
      '<input class="f" id="ry" type="number" value="' + ref + '"></div>' +
      '<div class="presets">' + presets.map(function (p) {
        return '<button class="btn" data-g="' + p[0] + '" data-y="' + p[1] + '">grade ' +
          p[0] + " · " + p[1] + "</button>";
      }).join("") + "</div>" +
      '<div id="rout"></div></div></div>';
  }

  function drawResolve(b) {
    var g = parseInt($("#rg").value, 10), y = parseInt($("#ry").value, 10);
    var r = resolve(b, g, isNaN(y) ? null : y);
    var h;
    if (!r.resolved) {
      h = '<div class="result bad"><div class="kv"><span class="k">Result</span>' +
        '<span class="v"><span class="pill wa">unresolved</span></span></div>' +
        '<div class="why">' + esc(r.why) + "</div></div>";
    } else {
      var s = r.step;
      h = '<div class="result"><div class="kv"><span class="k">Result</span><span class="v">' +
        '<span class="pill">' + esc(s.attainment || s.gmd) + "</span></span></div>" +
        kv("Era in force", r.era ? r.era.label + " (" + r.era.from + "–" + r.era.to + ")" : "—") +
        kv("National programme", s.programme) +
        kv("ISCED level", s.isced_label) +
        kv("Cycle ends at", s.completes_level ? "grade " + s.grade : "grade " + s.grade + " — not the last") +
        kv("Years of education", s.years_at_completion == null ? "—" : s.years_at_completion) +
        kv("GMD educ_highest", "<code>" + esc(s.gmd) + "</code>") +
        kv("GMD attainment", "<code>" + esc(s.attainment || "—") + "</code>") +
        (s.isced_a ? kv("ISCED-A code", '<span class="mono">' + esc(s.isced_a) + "</span>") : "") +
        '<div class="why">' + esc(r.why) + "</div></div>";
    }
    $("#rout").innerHTML = h;
  }

  function kv(k, v) {
    return '<div class="kv"><span class="k">' + esc(k) + '</span><span class="v">' + v + "</span></div>";
  }
  function stat(n, t) {
    return '<div class="stat"><div class="n">' + esc(n) + '</div><div class="t">' + esc(t) + "</div></div>";
  }

  /* ---------- wash ---------- */
  function washView(b) {
    var h = "";
    h += '<div class="card"><h2><span>' + esc(b.country.name) + " " + DOM_LABEL[b.domain].toLowerCase() +
      " instructions</span>" + '<span class="sub">' + esc(b.frame) + " · " + esc(b.version) + "</span>" +
      verdictPill(b.verdict, b.counts) +
      '<span class="spacer"></span><span class="sub mono">' + esc(b.fingerprint) + "</span></h2>";

    h += '<div class="note">Improvement status is copied from the JMP master class, never asserted by the ' +
      "country. No row carries a ladder rung — the rung is derived downstream from collection time, " +
      "availability, quality and sharing, which no source-mapping row can see.</div>";

    h += '<div class="stats">' +
      stat((b.vintage && b.vintage.n_sources) || 0, "sources") +
      stat(((b.vintage || {}).from || "?") + "–" + ((b.vintage || {}).to || "?"), "vintage") +
      stat((b.rows || []).length, "national categories") +
      stat((b.classifications || []).length, "classifications") +
      stat((b.facility_types || []).length, "facility types") +
      stat(b.language || "—", "language") +
      stat((b.translation || {}).resolved_by === "formula index"
        ? "translated" : "as written", "labels") +
      "</div>";

    h += '<div class="lbl">Facility type estimates — the top of the chain, in the workbook’s own words</div>';
    h += '<table class="tbl"><thead><tr><th>Facility type</th><th>In this workbook</th>' +
      "<th>JMP classes feeding it</th></tr></thead><tbody>";
    (b.facility_types || []).forEach(function (f) {
      h += "<tr><td><b>" + esc(f.name) + "</b>" +
        (f.name_local && f.name_local !== f.name ? '<span class="nat">' + esc(f.name_local) + "</span>" : "") +
        "</td><td>" + (f.in_workbook ? '<span class="pill">yes</span>'
          : '<span class="pill wa">absent</span>') + "</td>" +
        '<td class="mono" style="color:var(--tx-2)">' + f.n_classes + "</td></tr>";
    });
    h += "</tbody></table>";

    h += '<div class="lbl">Classification → subgroup → facility type' +
      '<button class="btn" id="tgl" style="float:right;margin-top:-4px">show unused subgroups</button></div>';
    h += '<div class="tree" id="tree">' + treeHtml(b, false) + "</div>";
    h += "</div>";

    h += sourcesCard(b);
    return h;
  }

  function treeHtml(b, showUnused) {
    return (b.classifications || []).map(function (c) {
      var subs = (c.subgroups || []).filter(function (s) {
        return showUnused || (s.national_categories || []).length;
      });
      if (!subs.length && !c.n_national_categories && !showUnused) return "";
      return '<details class="grp"' + (c.n_national_categories ? " open" : "") + "><summary>" +
        esc(c.classification) +
        '<span class="tag">' + c.n_national_categories + " national</span>" +
        impPill(c.improved) +
        '<span class="spacer"></span><span class="chain">' +
        esc((c.rolls_up_to || []).join(" · ") || "—") + "</span></summary>" +
        subs.map(function (s) {
          var nats = s.national_categories || [];
          return '<div class="sg' + (nats.length ? "" : " unused") + '">' +
            '<div class="name" style="padding-left:' + (12 + s.depth * 14) + 'px">' +
            esc(s.label) + " " + impPill(s.improved) +
            (s.shared === true ? ' <span class="tag">shared</span>' :
              s.shared === false ? ' <span class="tag">private</span>' : "") +
            '<div class="chain">' + (s.gmd ? "→ " + esc(s.gmd)
              : s.spans && s.spans.length ? "spans " + esc(s.spans.join(", ")) : "—") +
            "  ·  " + esc((s.rolls_up_to || []).join(" · ") || "no facility type") + "</div></div>" +
            '<div class="nats">' + nats.map(function (n) {
              return '<span class="nat-chip">' + esc(n) + "</span>";
            }).join("") + "</div></div>";
        }).join("") + "</details>";
    }).join("");
  }

  function edited(b, id, field) {
    var e = (b._edited || {})[String(id)] || [];
    return e.indexOf(field) >= 0
      ? ' <span class="tag wa" title="edited by a reviewer">edited</span>' : "";
  }

  function impPill(v) {
    return v === true ? '<span class="pill">improved</span>'
      : v === false ? '<span class="pill gy">unimproved</span>'
        : '<span class="pill wa">unsettled</span>';
  }

  function sourcesCard(b) {
    var rows = b.rows || [];
    var h = '<div class="card"><h2><span>Sources</span><span class="sub">' +
      "one concordance per survey; the years a category spans are the vintage trail</span></h2>" +
      '<div class="scroll"><table class="tbl"><thead><tr><th>Source</th><th>Year</th>' +
      "<th>Type</th><th>Categories</th><th>Name</th></tr></thead><tbody>";
    (b.sources || []).forEach(function (s) {
      h += '<tr><td class="mono">' + esc(s.code) + "</td><td>" + esc(s.year || "") + "</td>" +
        "<td>" + esc(s.type) + "</td>" +
        '<td class="mono">' + s.n_rows + "</td>" +
        '<td style="color:var(--tx-2)">' + esc(s.name) + "</td></tr>";
    });
    h += "</tbody></table></div>";

    h += '<div class="lbl">National categories<input class="f" id="rowq" placeholder="filter…" ' +
      'style="width:200px;float:right;margin-top:-5px"></div>';
    h += '<div class="scroll"><table class="tbl"><thead><tr><th>Original denomination</th>' +
      "<th>Classification → subgroup</th><th>Facility type</th><th>→ GMD</th>" +
      "<th>Improved</th><th>Seen in</th></tr></thead><tbody id=\"rowbody\">" +
      rowsHtml(rows) + "</tbody></table></div></div>";
    return h;
  }

  function editedRow(r) {
    var b = cur();
    return edited(b, r.code, "gmd");
  }

  function rowsHtml(rows) {
    return rows.map(function (r) {
      return '<tr><td><b>' + esc(r.label) + "</b>" +
        (r.jmp_label_local && r.jmp_label_local !== r.jmp.split(">").pop().trim()
          ? '<span class="nat">' + esc(r.jmp_label_local) + "</span>" : "") + "</td>" +
        '<td style="color:var(--tx-2)">' + esc(r.classification) +
        (r.subgroup ? " › " + esc(r.subgroup) : "") + "</td>" +
        '<td class="chain">' + esc((r.rolls_up_to || []).join(" · ") || "—") + "</td>" +
        "<td>" + (r.gmd ? "<code>" + esc(r.gmd) + "</code>"
          : '<span class="pill wa">spans ' + (r.spans || []).length + "</span>") +
          editedRow(r) + "</td>" +
        "<td>" + impPill(r.improved) + "</td>" +
        '<td class="mono" style="color:var(--tx-2)">' +
        esc((r.first_seen || "?") + "–" + (r.last_seen || "?")) +
        " (" + (r.observed_in || []).length + ")</td></tr>";
    }).join("");
  }

  /* ---------- findings ---------- */
  function findingsCard(b) {
    var f = b.findings || [], order = { BLOCK: 0, WARN: 1, INFO: 2 };
    f = f.slice().sort(function (a, c) { return order[a.level] - order[c.level]; });
    var h = '<div class="card"><h2><span>Findings</span><span class="sub">rule id · level · source row</span>' +
      '<span class="spacer"></span>' +
      '<span class="pill er">' + b.counts.BLOCK + " block</span>" +
      '<span class="pill wa">' + b.counts.WARN + " warn</span>" +
      '<span class="pill gy">' + b.counts.INFO + " info</span></h2>";
    if (!f.length) return h + '<div class="empty">Nothing to report.</div></div>';
    h += '<div class="scroll">' + f.map(function (x) {
      return '<div class="fnd"><span class="lv ' + x.level + '">' + x.level + "</span>" +
        '<span class="rule">' + esc(x.rule) + "</span>" +
        '<span class="msg">' + esc(x.message) +
        (x.source_row ? ' <span class="tag">row ' + x.source_row + "</span>" : "") + "</span></div>";
    }).join("") + "</div>";
    return h + "</div>";
  }

  function provenanceCard(b) {
    var s = b.source || {};
    var h = '<div class="card"><h2>Provenance</h2><div class="pad">' +
      kv("Workbook", esc(s.file)) +
      kv("SHA-256", '<span class="mono">' + esc(s.sha256) + "…</span>") +
      kv("Profile", '<span class="mono">' + esc(s.profile) + "</span>") +
      (s.sheet ? kv("Sheet", esc(s.sheet) + " · header row " + esc(s.header_row)) : "") +
      (s.rows_read ? kv("Rows read", esc(s.rows_read)) : "") +
      (s.reference_year ? kv("School year reference", esc(s.reference_year)) : "") +
      (s.vintage ? kv("JMP release", esc(s.vintage)) : "") +
      (b.selection ? kv("Sources selected", esc(b.selection.sources)) : "") +
      (b.translation && b.translation.available
        ? kv("Workbook language", esc(b.translation.language)) +
          kv("Labels resolved by", esc(b.translation.resolved_by)) +
          kv("Phrases in its table", esc(b.translation.phrases))
        : "") +
      kv("Extracted", '<span class="mono">' + esc(s.extracted_at) + "</span>") +
      kv("Schema", '<span class="mono" style="font-size:10px">' + esc(b.schema) + "</span>") +
      kv("Version", esc(b.version)) +
      kv("Status", '<span class="pill ac">' + esc(b.status) + "</span>") +
      ((b.registry || {}).n_eras
        ? kv("Eras on file", esc(b.registry.n_eras) + " · " +
             esc(b.registry.ingests) + " ingest(s)") : "") +
      (((b._review || {}).approval || {}).approved
        ? kv("Approved by", esc(b._review.approval.by))
        : "");
    if (b.language && b.language.national_columns) {
      var nl = b.language.national_language;
      h += '<div class="why">National-language columns kept: ' +
        Object.keys(b.language.national_columns).map(function (k) {
          return esc(k) + " (" + b.language.national_columns[k].rows_with_text + ")";
        }).join(", ") +
        (nl ? ". Language inferred: " + esc([].concat(nl.value).join(", ")) : "") + "</div>";
    }
    return h + "</div></div>";
  }

  /* ---------- benchmark ---------- */
  function fmt(v) {
    return (v === null || v === undefined || v === "") ? "—"
      : (typeof v === "number" ? v.toFixed(1) : esc(v));
  }

  function benchmarkView(b) {
    var bm = b.benchmark || {};
    var per = bm.per_source || [];
    if (b.kind !== "wash" || !per.length) {
      return '<div class="card"><div class="empty">' +
        (b.kind === "wash"
          ? "No published estimates were captured for this workbook."
          : "The benchmark is a JMP artefact; an education instruction has no " +
            "published estimates to be measured against.") + "</div></div>";
    }
    var sum = bm.summary || {};
    var h = '<div class="card"><h2><span>What JMP published</span>' +
      '<span class="sub">the mapping and the number it produced, side by side' +
      '</span></h2>' +
      '<div class="note">These are JMP\u2019s own estimates, kept beside the ' +
      "instruction and never inside it \u2014 a country instruction may not " +
      "carry survey-level data. They are the benchmark a harmonization run is " +
      "asked about, not a target to reproduce exactly: JMP models and " +
      "interpolates, GMD harmonizes microdata.</div>" +
      '<div class="stats">' +
      stat(sum.sources_with_estimates + "/" + sum.sources, "sources with estimates") +
      stat(sum.categories_with_estimates || 0, "published estimates") +
      stat((sum.from || "?") + "\u2013" + (sum.to || "?"), "vintage") +
      stat(sum.has_country_ladder ? "yes" : "no", "country ladder") +
      "</div>";

    var lad = (bm.ladder || {}).rungs || [];
    if (lad.length) {
      var doms = [];
      lad[0].values.forEach(function (v) {
        var k = v.domain + " " + v.split;
        if (doms.indexOf(k) < 0) doms.push(k);
      });
      h += '<div class="lbl">Country ladder \u2014 the published headline</div>' +
        '<div class="scroll"><table class="tbl"><thead><tr><th>Rung</th>' +
        doms.map(function (d) { return "<th>" + esc(d) + "</th>"; }).join("") +
        "</tr></thead><tbody>";
      lad.forEach(function (r) {
        h += "<tr><td><b>" + esc(r.rung) + "</b></td>" +
          doms.map(function (d) {
            var hit = r.values.filter(function (v) {
              return v.domain + " " + v.split === d; })[0];
            return '<td class="mono">' + (hit ? fmt(hit.value) : "—") + "</td>";
          }).join("") + "</tr>";
      });
      h += "</tbody></table></div>";
    }

    h += '<div class="lbl">By source' +
      '<select class="btn" id="bsrc" style="float:right;margin-top:-5px">' +
      per.map(function (p, i) {
        return '<option value="' + i + '">' + esc(p.source.code) +
          " \u00b7 " + (p.n_with_estimates || 0) + " estimates</option>";
      }).join("") + "</select></div>" +
      '<div id="bbody"></div></div>';
    return h;
  }

  function benchmarkSource(b, i) {
    var p = (b.benchmark.per_source || [])[i];
    if (!p) return "";
    var h = "";
    var blocks = p.blocks || {};
    Object.keys(blocks).forEach(function (k) {
      var rows = blocks[k];
      if (!rows.length) return;
      h += '<div class="lbl">' + esc(k.replace(/_/g, " ")) + "</div>" +
        '<table class="tbl"><thead><tr><th>Label</th><th>Urban</th>' +
        "<th>Rural</th><th>Total</th></tr></thead><tbody>" +
        rows.map(function (r) {
          return "<tr><td>" + esc(r.label) +
            (r.label_local && r.label_local !== r.label
              ? '<span class="nat">' + esc(r.label_local) + "</span>" : "") +
            '</td><td class="mono">' + fmt(r.urban) +
            '</td><td class="mono">' + fmt(r.rural) +
            '</td><td class="mono">' + fmt(r.total) + "</td></tr>";
        }).join("") + "</tbody></table>";
    });
    var cats = (p.categories || []).filter(function (c) {
      return c.total !== null || c.urban !== null || c.national_label; });
    h += '<div class="lbl">Categories \u2014 mapping and estimate together</div>' +
      '<div class="scroll"><table class="tbl"><thead><tr>' +
      "<th>JMP class</th><th>National category</th><th>\u2192 GMD</th>" +
      "<th>Urban</th><th>Rural</th><th>Total</th></tr></thead><tbody>" +
      cats.map(function (c) {
        return "<tr><td>" + '<span style="padding-left:' + (c.level * 12) +
          'px">' + esc(c.jmp.split(">").pop().trim()) + "</span></td>" +
          "<td>" + (c.national_label
            ? '<b>' + esc(c.national_label) + "</b>" : "—") + "</td>" +
          "<td>" + (c.gmd ? "<code>" + esc(c.gmd) + "</code>" : "—") + "</td>" +
          '<td class="mono">' + fmt(c.urban) + "</td>" +
          '<td class="mono">' + fmt(c.rural) + "</td>" +
          '<td class="mono">' + fmt(c.total) + "</td></tr>";
      }).join("") + "</tbody></table></div>";
    return h;
  }

  /* ---------- review: edit and approve ---------- */
  function reviewView(b) {
    var rv = b._review || {};
    var ap = rv.approval;
    var patches = rv.patches || [];
    var blocked = (b.counts || {}).BLOCK > 0;
    var warns = (b.findings || []).filter(function (f) { return f.level === "WARN"; });

    var h = '<div class="card"><h2><span>Review</span><span class="sub">' +
      "edits are a patch beside the extract; approval names a person" +
      "</span></h2>";

    if (!canReview()) {
      h += '<div class="note">This page is read-only. Editing and approving ' +
        "write files, so they are available only when a folder is being " +
        "served: <code>viewer out/ --serve</code>.</div>";
    }

    if (ap && ap.approved) {
      h += '<div class="pad"><div class="result">' +
        kv("Status", '<span class="pill">approved</span>') +
        kv("By", esc(ap.by)) + kv("At", '<span class="mono">' + esc(ap.at) + "</span>") +
        kv("Version", esc(ap.version)) +
        kv("Fingerprint", '<span class="mono">' + esc(ap.fingerprint) + "</span>") +
        kv("Warnings acknowledged", (ap.acknowledged || []).length) +
        (ap.note ? '<div class="why">' + esc(ap.note) + "</div>" : "") +
        "</div>" +
        (canReview() ? '<div style="margin-top:10px">' +
          '<button class="btn" id="revokebtn">withdraw approval</button></div>'
          : "") + "</div>";
    }

    h += '<div class="lbl">Edits (' + patches.length + ")</div>";
    if (!patches.length) {
      h += '<div class="pad" style="color:var(--tx-2)">Nothing has been ' +
        "edited. The instruction is exactly what the workbook produced.</div>";
    } else {
      h += '<table class="tbl"><thead><tr><th>#</th><th>What</th><th>New value</th>' +
        "<th>Reason</th><th>By</th><th></th></tr></thead><tbody>" +
        patches.map(function (p) {
          return '<tr><td class="mono">' + p.seq + "</td>" +
            '<td class="mono">' + esc(p.target) + " \u00b7 " + esc(p.id) +
            " \u00b7 " + esc(p.field) + "</td>" +
            "<td><code>" + esc(p.value) + "</code></td>" +
            "<td>" + esc(p.reason) + "</td>" +
            '<td style="color:var(--tx-2)">' + esc(p.by) + "</td>" +
            "<td>" + (canReview()
              ? '<button class="btn" data-undo="' + p.seq + '">undo</button>'
              : "") + "</td></tr>";
        }).join("") + "</tbody></table>";
    }

    if (canReview() && !(ap && ap.approved)) {
      h += '<div class="lbl">Make an edit</div><div class="pad">' +
        '<div class="field"><label>Your name</label>' +
        '<input class="f" id="ewho" value="' + esc(who) + '"></div>' +
        '<div class="field"><label>Row</label>' +
        '<select class="f" id="etarget">' + editableRows(b) + "</select></div>" +
        '<div class="field"><label>Field</label>' +
        '<select class="f" id="efield">' +
        (b.kind === "education"
          ? '<option value="gmd">gmd (canonical level)</option>' +
            '<option value="attainment_note">attainment note</option>' +
            '<option value="note">note</option>'
          : '<option value="gmd">gmd (canonical target)</option>' +
            '<option value="improved_note">improved note</option>' +
            '<option value="note">note</option>') +
        '<option value="excluded">excluded (true/false)</option>' +
        "</select></div>" +
        '<div class="field"><label>New value</label>' +
        '<input class="f" id="evalue"></div>' +
        '<div class="field"><label>Reason (required)</label>' +
        '<input class="f" id="ereason" placeholder="why this is the right value"></div>' +
        '<button class="btn on" id="esave">save edit</button>' +
        '<span id="emsg" style="margin-left:10px"></span></div>';

      h += '<div class="lbl">Approve</div><div class="pad">';
      if (blocked) {
        h += '<div class="result bad"><b>Blocked.</b> ' +
          ((b.counts || {}).BLOCK) + " finding(s) cannot be waived here. " +
          "They have to be resolved in the workbook, or by a schema decision " +
          "in System 4.</div>";
      } else {
        h += '<div style="color:var(--tx-2);margin-bottom:10px">Every warning ' +
          "needs an acknowledgement in writing. A warning nobody wrote " +
          "against is not approved.</div>";
        warns.forEach(function (f, i) {
          h += '<div class="field"><label>' + esc(f.rule) + " \u00b7 " +
            esc(f.message.slice(0, 110)) + "</label>" +
            '<input class="f ack" data-rule="' + esc(f.rule) +
            '" placeholder="your acknowledgement"></div>';
        });
        h += '<div class="field"><label>Your name</label>' +
          '<input class="f" id="awho" value="' + esc(who) + '"></div>' +
          '<div class="field"><label>Note (optional)</label>' +
          '<input class="f" id="anote"></div>' +
          '<button class="btn on" id="approvebtn">approve ' +
          esc(b.country.iso3) + " \u00b7 " + esc(b.domain) + "</button>" +
          '<span id="amsg" style="margin-left:10px"></span>';
      }
      h += "</div>";
    }
    return h + "</div>";
  }

  function editableRows(b) {
    if (b.kind === "education") {
      return (b.rows || []).map(function (r) {
        return '<option value="' + esc(r.programme_id) + '">' +
          esc(r.programme) + " \u00b7 ISCED " + esc(r.isced) + "</option>";
      }).join("");
    }
    return (b.rows || []).map(function (r) {
      return '<option value="' + esc(r.code) + '">' + esc(r.label) +
        " \u00b7 " + esc(r.jmp) + "</option>";
    }).join("");
  }

  function wireReview(b) {
    var msg = function (id, text, bad) {
      var el = $("#" + id);
      if (el) {
        el.innerHTML = '<span class="pill ' + (bad ? "er" : "") + '">' +
          esc(text) + "</span>";
      }
    };
    $("#main").querySelectorAll("[data-undo]").forEach(function (btn) {
      btn.onclick = function () {
        post("/api/unpatch", { seq: +btn.dataset.undo })
          .then(function () { return source.reload(); })
          .then(after).catch(fail);
      };
    });
    var save = $("#esave");
    if (save) save.onclick = function () {
      who = $("#ewho").value.trim();
      try { localStorage.setItem("gmdcv-who", who); } catch (e) {}
      post("/api/patch", { patch: {
        target: "rows", id: $("#etarget").value, field: $("#efield").value,
        value: $("#evalue").value, reason: $("#ereason").value, by: who } })
        .then(function () { return source.reload(); })
        .then(after)
        .catch(function (e) { msg("emsg", e.message, true); });
    };
    var ap = $("#approvebtn");
    if (ap) ap.onclick = function () {
      who = $("#awho").value.trim();
      try { localStorage.setItem("gmdcv-who", who); } catch (e) {}
      var acks = [];
      $("#main").querySelectorAll("input.ack").forEach(function (i) {
        acks.push({ rule: i.dataset.rule, text: i.value.trim() });
      });
      post("/api/approve", {
        by: who, fingerprint: b.fingerprint, version: b.version,
        verdict: b.verdict, counts: b.counts, acknowledged: acks,
        note: $("#anote").value, patches: ((b._review || {}).patches || []).length
      }).then(function () { return source.reload(); }).then(after)
        .catch(function (e) { msg("amsg", e.message, true); });
    };
    var rk = $("#revokebtn");
    if (rk) rk.onclick = function () {
      post("/api/revoke", { by: who || "unnamed",
                            reason: "withdrawn from the viewer" })
        .then(function () { return source.reload(); }).then(after).catch(fail);
    };
  }

  /* ---------- artefacts ---------- */
  function artefactsView() {
    var list = artefacts[state.iso] || [];
    if (!list.length) {
      return '<div class="card"><div class="empty">' +
        (source.kind === "embed"
          ? "This page is a frozen snapshot, so the files it was built from " +
            "are not attached. Serve the folder or pick it to read them."
          : "No readable artefacts found beside the view bundles.") +
        "</div></div>";
    }
    var h = '<div class="card"><h2><span>Artefacts</span><span class="sub">' +
      "the files the code actually wrote, read from " +
      (source.kind === "server" ? "disk" : "the folder you chose") +
      "</span></h2>" +
      '<table class="tbl"><thead><tr><th>File</th><th>Size</th><th></th>' +
      "</tr></thead><tbody>";
    list.forEach(function (f, i) {
      h += '<tr><td class="mono">' + esc(f.name) + "</td>" +
        '<td class="mono" style="color:var(--tx-2)">' +
        (f.size >= 1024 ? Math.round(f.size / 1024) + " KB" : f.size + " B") +
        "</td>" +
        '<td><button class="btn" data-raw="' + i + '">view</button></td></tr>';
    });
    h += '</tbody></table><div id="rawbox"></div></div>';
    return h;
  }

  function wireArtefacts() {
    var list = artefacts[state.iso] || [];
    $("#main").querySelectorAll("[data-raw]").forEach(function (btn) {
      btn.onclick = function () {
        var f = list[+btn.dataset.raw];
        var box = $("#rawbox");
        box.innerHTML = '<div class="pad" style="color:var(--tx-2)">reading ' +
          esc(f.name) + "…</div>";
        Promise.resolve(f.read()).then(function (t) {
          box.innerHTML = '<div class="lbl">' + esc(f.name) + "</div>" +
            '<pre class="raw">' + esc(t.length > 400000
              ? t.slice(0, 400000) + "\n… truncated" : t) + "</pre>";
        }).catch(function (e) {
          box.innerHTML = '<div class="pad" style="color:var(--t-er)">' +
            esc(String(e)) + "</div>";
        });
      };
    });
  }

  /* ---------- render ---------- */
  function render() {
    var b = countries[state.iso].doms[state.domain];
    $("#sys").textContent = DOM_SYS[b.domain];
    if (state.tab === "files") {
      $("#main").innerHTML = artefactsView();
      $("#side").innerHTML = findingsCard(b) + provenanceCard(b);
      wireArtefacts();
      window.scrollTo(0, 0);
      return;
    }
    if (state.tab === "bench") {
      $("#main").innerHTML = benchmarkView(b);
      $("#side").innerHTML = findingsCard(b) + provenanceCard(b);
      var sel = $("#bsrc");
      if (sel) {
        var draw = function () { $("#bbody").innerHTML = benchmarkSource(b, +sel.value); };
        sel.onchange = draw; draw();
      }
      window.scrollTo(0, 0);
      return;
    }
    if (state.tab === "review") {
      $("#main").innerHTML = reviewView(b);
      $("#side").innerHTML = findingsCard(b) + provenanceCard(b);
      wireReview(b);
      window.scrollTo(0, 0);
      return;
    }
    $("#main").innerHTML = b.kind === "education" ? eduView(b) : washView(b);
    $("#side").innerHTML =
      (b.kind === "education" ? resolverCard(b) : "") +
      findingsCard(b) + provenanceCard(b);

    if (b.kind === "education") {
      var draw = function () { drawResolve(b); };
      $("#rg").oninput = draw; $("#ry").oninput = draw;
      $("#side").querySelectorAll(".presets .btn").forEach(function (x) {
        x.onclick = function () {
          $("#rg").value = x.dataset.g; $("#ry").value = x.dataset.y; draw();
        };
      });
      draw();
    } else {
      var shown = false, t = $("#tgl");
      t.onclick = function () {
        shown = !shown;
        t.textContent = shown ? "hide unused subgroups" : "show unused subgroups";
        t.classList.toggle("on", shown);
        $("#tree").innerHTML = treeHtml(b, shown);
      };
      var q = $("#rowq");
      q.oninput = function () {
        var v = q.value.toLowerCase();
        $("#rowbody").innerHTML = rowsHtml((b.rows || []).filter(function (r) {
          return !v || (r.label + " " + r.classification + " " + r.subgroup + " " +
            r.gmd).toLowerCase().indexOf(v) >= 0;
        }));
      };
    }
    window.scrollTo(0, 0);
  }

  /* ---------- chrome ---------- */
  function renderTop() {
    var c = $("#countries"), d = $("#domains");
    c.hidden = isoList.length < 2;
    c.innerHTML = isoList.map(function (k) {
      return '<button data-iso="' + k + '"' + (k === state.iso ? ' class="on"' : "") +
        ">" + esc(countries[k].name || k) + '<span class="tag">' + esc(k) + "</span></button>";
    }).join("");
    var doms = DOM_ORDER.filter(function (x) { return countries[state.iso].doms[x]; });
    d.innerHTML = doms.map(function (x) {
      var b = countries[state.iso].doms[x];
      return '<button data-dom="' + x + '"' + (x === state.domain && state.tab === "view" ? ' class="on"' : "") + ">" +
        esc(DOM_LABEL[x]) + verdictPill(b.verdict, b.counts) + "</button>";
    }).join("") +
      '<button data-tab="bench"' + (state.tab === "bench" ? ' class="on"' : "") +
      ">Benchmark</button>" +
      '<button data-tab="review"' + (state.tab === "review" ? ' class="on"' : "") +
      ">Review" + reviewPill() + "</button>" +
      '<button data-tab="files"' + (state.tab === "files" ? ' class="on"' : "") +
      ">Artefacts</button>";
    c.querySelectorAll("button").forEach(function (b) {
      b.onclick = function () { go(b.dataset.iso, null, "view"); };
    });
    d.querySelectorAll("button").forEach(function (b) {
      b.onclick = function () {
        if (b.dataset.tab) { state.tab = b.dataset.tab; renderTop(); render(); }
        else { go(state.iso, b.dataset.dom, "view"); }
      };
    });
  }

  function cur() { return countries[state.iso].doms[state.domain]; }

  function reviewPill() {
    var b = countries[state.iso] && countries[state.iso].doms[state.domain];
    var rv = (b && b._review) || {};
    if (rv.approval && rv.approval.approved) {
      return '<span class="pill">approved</span>';
    }
    var n = (rv.patches || []).length;
    return n ? '<span class="pill ac">' + n + " edit" + (n > 1 ? "s" : "") +
      "</span>" : "";
  }

  function canReview() { return source.kind === "server"; }

  function post(path, body) {
    var b = cur();
    return fetch(path, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(Object.assign(
        { dir: b._dir || "", stem: b._stem || "" }, body))
    }).then(function (r) {
      return r.json().then(function (d) {
        if (!r.ok) throw new Error(d.error || (r.status + " " + r.statusText));
        return d;
      });
    });
  }

  function renderSource() {
    var bar = $("#srcbar");
    var where = source.kind === "server"
      ? '<span class="tag">live</span><span class="mono">' + esc(source.root) + "</span>"
      : source.kind === "folder"
        ? '<span class="tag">folder</span><span class="mono">' + esc(source.label) + "</span>"
        : '<span class="tag wa">snapshot</span><span class="mono">frozen at build time</span>';
    var pickers = "";
    if (source.kind === "server") {
      pickers = '<select class="btn" id="folderpick" title="country folder">' +
        '<option value=""' + (source.current === "" ? " selected" : "") +
        ">all folders (" + (source.folders || []).length + ")</option>" +
        (source.folders || []).map(function (f) {
          return '<option value="' + esc(f.dir) + '"' +
            (f.dir === source.current ? " selected" : "") + ">" +
            esc(f.iso3) + " · " + esc(f.dir || ".") + "</option>";
        }).join("") + "</select>";
    }
    bar.innerHTML = where + pickers +
      (source.reload ? '<button class="btn" id="reloadbtn">reload</button>' : "") +
      (source.kind !== "server" ? '<button class="btn" id="pickbtn">open folder…</button>' : "");
    var r = $("#reloadbtn");
    if (r) r.onclick = function () {
      r.disabled = true; r.textContent = "reading…";
      Promise.resolve(source.reload()).then(after).catch(fail);
    };
    var p = $("#pickbtn");
    if (p) p.onclick = function () { pickFolder().then(function (x) { if (x !== null) after(); }).catch(fail); };
    var fp = $("#folderpick");
    if (fp) fp.onchange = function () { loadServer(fp.value).then(after).catch(fail); };
  }

  function go(iso, dom, tab) {
    state.iso = iso;
    state.tab = tab || "view";
    var doms = DOM_ORDER.filter(function (x) { return countries[iso].doms[x]; });
    state.domain = (dom && countries[iso].doms[dom]) ? dom : doms[0];
    renderTop();
    render();
    try { localStorage.setItem("gmdcv", iso + "|" + state.domain); } catch (e) {}
  }

  function gate(msg, err) {
    $("#cols").hidden = true;
    $("#gate").innerHTML = '<div class="card"><div class="empty">' +
      (err ? '<div class="pill er" style="margin-bottom:10px">could not load</div><br>' : "") +
      esc(msg) +
      (MODE === "server" ? "" :
        '<div style="margin-top:14px"><button class="btn on" id="gatepick">' +
        "open a country folder…</button></div>") +
      "</div></div>";
    var g = $("#gatepick");
    if (g) g.onclick = function () {
      pickFolder().then(function (x) { if (x !== null) after(); }).catch(fail);
    };
    renderSource();
  }

  function after() {
    if (!isoList.length) { return gate("That folder holds no view bundles."); }
    $("#gate").innerHTML = "";
    $("#cols").hidden = false;
    var last = null;
    try { last = (localStorage.getItem("gmdcv") || "").split("|"); } catch (e) {}
    var iso = (state.iso && countries[state.iso]) ? state.iso
      : (last && countries[last[0]]) ? last[0] : isoList[0];
    renderSource();
    go(iso, (state.domain || (last && last[1])), state.tab);
  }

  function fail(e) {
    gate(String((e && e.message) || e), true);
  }

  /* ---------- boot ---------- */
  $("#themebtn").onclick = function () {
    var d = document.documentElement.getAttribute("data-theme") === "dark";
    document.documentElement.setAttribute("data-theme", d ? "light" : "dark");
    try { localStorage.setItem("gmdcv-theme", d ? "light" : "dark"); } catch (e) {}
  };
  try {
    var th = localStorage.getItem("gmdcv-theme");
    if (th) document.documentElement.setAttribute("data-theme", th);
  } catch (e) {}

  /* Drag and drop.  Chromium can hand over a real directory handle, which is
     worth having because it makes "reload" re-read the disk. When it declines
     -- and it declines for a plain file drop -- fall back to the files
     themselves rather than doing nothing, which is what the first version of
     this did. `dataTransfer.files` is captured synchronously because the
     object is neutered once the handler returns. */
  function handleDrop(e) {
    e.preventDefault();
    document.body.classList.remove("dropping");
    var dt = e.dataTransfer;
    if (!dt) return;
    var files = Array.prototype.slice.call(dt.files || []);
    var item = dt.items && dt.items[0];
    var fallback = function () {
      if (!files.length) {
        return fail(new Error("nothing readable was dropped -- drop a country "
                              + "folder, or the files inside it"));
      }
      loadFiles(files, "dropped files", null).then(after).catch(fail);
    };
    if (item && item.getAsFileSystemHandle) {
      var pr;
      try { pr = item.getAsFileSystemHandle(); } catch (err) { return fallback(); }
      return Promise.resolve(pr).then(function (h) {
        if (h && h.kind === "directory") return loadHandle(h).then(after);
        fallback();
      }).catch(fallback);
    }
    fallback();
  }

  document.addEventListener("dragover", function (e) {
    e.preventDefault();
    document.body.classList.add("dropping");
  });
  document.addEventListener("dragleave", function (e) {
    if (e.relatedTarget === null) document.body.classList.remove("dropping");
  });
  document.addEventListener("drop", handleDrop);

  if (MODE === "server") {
    gate("Reading the folder…");
    loadServer(null).then(after).catch(fail);
  } else if ((window.__BUNDLES__ || []).length) {
    ingest(window.__BUNDLES__);
    source = { kind: "embed", label: "frozen snapshot", reload: null };
    after();
  } else {
    source = { kind: "folder", label: "nothing loaded", reload: null };
    gate("Choose the folder the extractor wrote — a country folder such as " +
         "out/IND, or the out/ folder above it. You can also drop it anywhere " +
         "on this page. Nothing is uploaded; the browser reads the files.");
  }
})();
