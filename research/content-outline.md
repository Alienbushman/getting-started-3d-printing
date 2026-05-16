# Content Outline — getting-started-3d-printing

Drafted 2026-05-16 for [getting-started-3d-printing:005].
Sign-off: alienbushman.
Scope: 8 guides (per PROJECT_SCOPE.md v0.1.0 cap), 0 video, FDM focus.

---

## Getting-Started Guide Sections (8 of 8)

Dropped from default list vs. scope cap: Supports + overhangs, Post-processing. Both deferred to v0.2.0.

---

### 1. What Is 3D Printing?

**Slug:** `what-is-3d-printing`
**Est. read time:** 4 min

FDM (Fused Deposition Modeling) explained in one paragraph without jargon: a printer melts plastic filament and deposits it layer by layer to build a solid object from a digital file. Contrast with SLA/resin briefly (one sentence) then park it — this site is FDM-only. Cover what kinds of objects are realistic to print (functional parts, figurines, organizers, jigs) and what aren't (food-contact, high-heat, structural load-bearing without careful material selection). Close with a "you'll come back to this when…" callout pointing to the Filament 101 guide for material limits.

---

### 2. How an FDM Printer Works

**Slug:** `how-a-printer-works`
**Est. read time:** 6 min

A labelled diagram of an FDM printer (bed, gantry, extruder, hot end, part cooling fan, Z lead screw). Walk through the motion sequence: home → heat up → lay skirt → print layers → cool → done. Explain the four key variables a beginner controls: layer height, print speed, nozzle temperature, bed temperature. One callout: "The slicer sets all of these — you don't type them in manually." Links forward to Slicer Basics.

---

### 3. Picking Your First Printer

**Slug:** `picking-your-first-printer`
**Est. read time:** 8 min

Decision framework, not a ranked list (ranked lists age badly). Three tiers: sub-$300 (Bambu A1 Mini, Ender 3 V3 SE class), $300–$700 (Prusa MK4S, Bambu P1S class), $700+ (Prusa XL, Core XY pro class). Key decision axes: enclosed vs. open-frame (ABS/ASA needs enclosure), auto bed leveling (essential for beginners), community support size, spare part availability. One firm recommendation: for a first printer, prioritize auto bed leveling and a large community over raw build volume. Attribute hardware mentions to manufacturer pages; no affiliate links.

---

### 4. Filament 101: PLA, PETG, and ABS

**Slug:** `filament-101`
**Est. read time:** 7 min

Three-column comparison: PLA (easy, biodegradable-ish, not heat-resistant, best for learning), PETG (tougher, slightly moisture-sensitive, good functional parts, forgiving), ABS (strong, heat-resistant, warps without enclosure, fumes — avoid for beginners). One table: print temp, bed temp, enclosure needed, common use case, common failure mode. One callout: "Start with PLA. Switch to PETG once you've nailed your first layer. Save ABS for when you know why you need it." Links forward to Common Failures for material-specific failures.

---

### 5. Slicer Basics

**Slug:** `slicer-basics`
**Est. read time:** 8 min

What a slicer does: converts an STL/3MF into G-code layer instructions. Two slicers covered (both free): PrusaSlicer (printer-agnostic, strong defaults) and Bambu Studio (best for Bambu hardware). Workflow: import model → choose printer profile → set layer height + infill + supports → preview layers → export G-code. Explain the five settings beginners actually adjust: layer height (0.2mm default), infill % (15% decorative, 40% functional), support (on/off auto), print speed (start slow), brim (when adhesion is tricky). One screenshot-description per slicer (text description only; actual screenshots in the implementation ticket).

---

### 6. Your First Print, Step by Step

**Slug:** `your-first-print`
**Est. read time:** 10 min

A numbered pre-flight + print procedure: (1) Level the bed (or run auto-level). (2) Load filament — heat the hot end, push filament until you see it extrude cleanly. (3) Open slicer, import the test model (3DBenchy or calibration cube). (4) Use the printer's default profile. (5) Start print — watch the first layer. (6) Let it finish; don't touch it until the bed cools. (7) Remove the part; inspect for the common first-layer issues. Each step has a one-sentence "what success looks like" and a one-sentence "if it goes wrong, see [link]." Links to Bed Adhesion and Common Failures.

---

### 7. Bed Adhesion and the First Layer

**Slug:** `bed-adhesion`
**Est. read time:** 6 min

Why the first layer matters: it's the foundation every other layer sits on. Three failure modes: too far from bed (spaghetti), too close (nozzle gouges), not sticking (warping). Solutions: (1) Re-run bed leveling. (2) Clean the build plate with IPA. (3) Increase bed temperature by 5°C. (4) Add a brim in the slicer. Surface types: PEI spring steel (most recommended), glass, BuildTak. One callout: "The first layer is the most important thing to get right. Print a single-layer square as a quick test before any long print."

---

### 8. Common Failures and Fixes

**Slug:** `common-failures`
**Est. read time:** 10 min

Eight failure modes, each with: photo description, cause, one-step fix. Failures covered: (1) Stringing — retraction too low; increase retraction distance 0.5mm at a time. (2) Layer shifting — loose belts or print speed too high; check belt tension, slow down. (3) Warping — insufficient bed adhesion or draft; raise bed temp, add brim, enclose for ABS. (4) Elephant's foot — first layer squished too close; raise Z offset slightly. (5) Under-extrusion — partial clog or wrong temperature; cold pull, check temp. (6) Overheating (drooping) — cooling fan failure or speed too fast for geometry; check fan, slow small-feature layers. (7) Z-banding — lead screw issue or vibration; check screw coupling. (8) Clogged nozzle — cold pull procedure. Links back to relevant guide sections.

---

## Glossary Term List (35 terms)

For `/glossary` page — each term gets ~2 sentences in the implementation ticket.

| Term | Category |
|------|----------|
| FDM (Fused Deposition Modeling) | Technology |
| Slicer | Software |
| G-code | Software |
| STL | File format |
| 3MF | File format |
| Layer height | Settings |
| Infill | Settings |
| Infill pattern | Settings |
| Print speed | Settings |
| Nozzle temperature | Settings |
| Bed temperature | Settings |
| Retraction | Settings |
| Z-hop | Settings |
| Brim | Settings |
| Raft | Settings |
| Skirt | Settings |
| Support | Settings |
| Overhang | Geometry |
| Bridge / Bridging | Geometry |
| First layer | Printing |
| Bed adhesion | Printing |
| Vase mode (spiralize) | Printing |
| Part cooling fan | Hardware |
| Hot end | Hardware |
| Extruder | Hardware |
| Build plate / Bed | Hardware |
| PEI (spring steel sheet) | Hardware |
| PLA | Material |
| PETG | Material |
| ABS | Material |
| TPU | Material |
| Stringing | Failure mode |
| Elephant's foot | Failure mode |
| Warping | Failure mode |
| Layer shifting | Failure mode |
