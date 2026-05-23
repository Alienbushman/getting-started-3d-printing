---
title: "Dual Extrusion Calibration Coin"
image: "/images/models/two-color-coin.svg"
stl_path: "/models/two-color-coin.stl"
license: "CC0-1.0"
author: "SnobbishGoose"
source_url: "https://www.printables.com/model/346994-dual-extrusion-calibration-coin"
difficulty: "intermediate"
est_print_time_minutes: 30
supports_required: false
layer_height_mm: 0.2
description: "A 63.5 mm flat coin designed to tune where the colour-change line lands on a single-extruder printer. Teaches the M600 colour-change workflow without a multi-material rig."
skill_tags: ["filament-change", "two-color", "m600"]
featured: false
learning_order: 10
learning_skill: "Swap filament mid-print to produce a two-tone object"
---

## Why print this

Two colours on one part normally means a multi-material printer. M600 (or your slicer's "colour change at layer" command) does the same job on a single extruder: the printer pauses, you swap filament, you press resume. This coin is the calibration target — it's flat, fast, and the swap line is the whole point. Once you know exactly where the line lands on your printer + filament combo, every future two-tone print becomes a planning exercise instead of a guess.

## Before you slice

The model is one flat disc, 63.5 mm across. No supports, no special bed prep beyond a clean PEI sheet — but the first layer matters because the surface is fully visible.

The lesson is the colour change, not the slicer profile. Default PLA profile is fine. Decide which layer you want the transition on; half-height (~5 mm, ~25 layers at 0.2 mm) is the conventional target for this coin.

- **PrusaSlicer / OrcaSlicer**: right-click the layer slider in the preview → "Add colour change". The slicer inserts `M600` at that height.
- **Bambu Studio**: use the layer slider's pause-at-height; the firmware handles the swap.

## What to expect

1. Load colour A. Heat hot end + bed; verify the first layer extrudes cleanly with a skirt.
2. Slice with the colour change inserted at ~5 mm.
3. Start the print. The first half prints in colour A as normal.
4. At the configured height the printer beeps and pauses, retracting filament.
5. Cut the filament near the extruder, load colour B, and purge ~30 mm by hand until the new colour runs clean.
6. Resume from the printer's display. Second-colour layers print on top.
7. Total time ~30 minutes; ~5 g PLA combined.

## If it goes wrong

- **Swap line lands at the wrong height** — recompute layer × layer-height (5 mm at 0.2 mm = layer 25). Re-insert the colour change at the right layer in the slicer.
- **Printer didn't pause** — the slicer didn't write `M600` (or your firmware doesn't accept it). Check the G-code for the M600 line; on some printers use `M0` or a pause-at-height post-processor instead.
- **Purge blob or mixed colour on the first new layers** — you didn't purge enough by hand. Extrude 30–50 mm of colour B before resuming next time.
- **Visible banding at the swap line** — the nozzle cooled during the pause. Preheat the hot end manually before pressing resume.
