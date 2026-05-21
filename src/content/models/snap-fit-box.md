---
title: "Storage Box with Snap-Fit Lid"
image: "/images/models/snap-fit-box.svg"
stl_path: "/models/snap-fit-box.stl"
license: "CC-BY-NC-SA-4.0"
commercial_use: false
author: "Extrutim"
source_url: "https://www.printables.com/model/20961-storage-box-snap-fit-lid"
difficulty: "intermediate"
est_print_time_minutes: 123
supports_required: false
layer_height_mm: 0.2
description: "A two-part storage box with a snap-fit lid. A hands-on lesson in snap joint tolerances — the lid either clicks or it doesn't."
skill_tags: ["functional", "no-supports", "snap-fit", "tolerance"]
featured: false
---

## Why print this

Snap-fit joints are everywhere in consumer products. Printing one that actually snaps makes dimensional accuracy suddenly concrete and tactile. The gap between "close enough" and "clicks properly" is measured in tenths of a millimetre.

## Before you slice

Print the box and lid as two separate jobs — they have different orientations and need different settings.

The model page provides multiple lid variants:
- **LidTight.stl** — snug fit, may need some pressure.
- **Lid_more_Space** — looser fit if the tight lid doesn't close.

Start with the standard lid. Print at 0.2 mm layer height, 15% infill for the box, 40% infill for the lid (the snap features need rigidity).

## What to expect

1. Print the box first (~75 min).
2. Print the lid second using the appropriate variant (~48 min).
3. Let both parts cool fully before testing — PLA is softer while warm.
4. Attempt to snap the lid onto the box. It should require moderate force and click audibly.
5. If it doesn't click cleanly, compare which variant fits better.

## If it goes wrong

- **Lid too tight to close** — either print `Lid_more_Space` or reduce horizontal expansion in the slicer by -0.1 mm.
- **Lid snaps on but falls off immediately** — print `LidTight.stl` or increase horizontal expansion by +0.1 mm.
- **Snap tabs break when testing** — too brittle. Increase infill on the lid to 50%, or raise nozzle temperature by 5°C for better inter-layer adhesion.
- **Box warping on a large footprint** — add a brim, clean the bed, and ensure bed temperature is 60°C for PLA.
