---
title: "Two-Color Calibration Coin (TBD)"
image: "/images/models/two-color-coin.svg"
stl_path: "/models/two-color-coin.stl"
license: "TBD — verify before download"
author: "TBD — not yet selected"
source_url: "https://www.printables.com"
difficulty: "intermediate"
est_print_time_minutes: 30
supports_required: false
layer_height_mm: 0.2
description: "A flat two-colour coin teaching filament change mid-print via M600 pause. Placeholder — model not yet selected. See research/attribution.md for selection criteria."
skill_tags: ["filament-change", "two-color", "m600"]
featured: false
---

## Why print this

Filament change mid-print (via the M600 G-code command) is how you produce two-colour objects without a multi-material system. The printer pauses, you swap filament, and the top layers print in a different colour. This coin model is a simple, fast introduction to that workflow.

## Before you slice

This entry is a **placeholder**. The specific model has not yet been selected. Requirements for the replacement model:
- License: CC0 or CC-BY (CC-BY-SA acceptable).
- Fits on a 50×50 mm bed.
- Print time under 45 minutes.
- No supports required.
- Flat design with a clear colour-change layer.

Once selected: add a colour change pause at the target layer in your slicer. In PrusaSlicer, right-click a layer in the preview and add an "M600" colour change. In Bambu Studio, use the "Color" tab to set a layer-based pause.

## What to expect

1. Slice the model. Add an M600 pause at the colour-change layer.
2. Start the print. When the pause triggers, the printer will beep and wait.
3. Retract the current filament, load the second colour, and purge until the new colour extrudes cleanly.
4. Resume the print. The remaining layers will be in the new colour.

## If it goes wrong

- **Colour bleed at the change layer** — insufficient purge. Purge more filament before resuming.
- **Print stops and won't resume** — check the printer's display for a prompt. Some printers need a button press to continue after M600.
- **Filament not feeding after swap** — reheat the hot end manually and push the new filament through by hand before resuming.
