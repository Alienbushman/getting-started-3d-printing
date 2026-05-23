---
title: "Cute Mini Octopus"
image: "/images/models/cute-mini-octopus.svg"
stl_path: "/models/cute-mini-octopus.stl"
license: "CC-BY-NC-SA-4.0"
commercial_use: false
author: "McGybeer"
source_url: "https://www.printables.com/model/178035-cute-mini-octopus"
difficulty: "intermediate"
est_print_time_minutes: 90
supports_required: true
layer_height_mm: 0.2
description: "A small octopus figurine with curving tentacles. The model page offers a version with built-in tree supports — practice enabling, generating, and removing supports."
skill_tags: ["supports", "figurine", "support-removal"]
featured: true
learning_order: 8
learning_skill: "Generate, print, and remove tree supports cleanly"
---

## Why print this

Supports are unavoidable once you move beyond simple geometry. This model teaches you how to enable them, let the slicer generate them, and remove them cleanly. The before/after is satisfying: a model covered in scaffolding becomes a smooth figurine.

## Before you slice

The model page provides two STL variants:
- **with-supports.stl** — built-in supports integrated into the geometry.
- **without-supports.stl** — clean model; you generate supports in the slicer.

**For this learning exercise, use the without-supports STL and generate tree supports in the slicer.** This teaches you the slicer workflow, not just the physical result.

Settings: 0.2 mm layer height, 15% infill, tree supports enabled, support contact distance 0.2 mm.

## What to expect

1. Import the without-supports STL.
2. Enable tree supports in the slicer. In PrusaSlicer: Support material → "For support enforcer only" → change to "Everywhere"; set support style to "Tree".
3. Preview the supports in the layer view. They should branch up under the tentacle tips.
4. Print time is approximately 1 hour 30 minutes.
5. After printing and cooling, remove the tree supports by hand. Start at the contact points and peel downward. They should snap off cleanly.
6. Use needle-nose pliers or flush cutters for tight spots. Don't force — snap at the contact point.

## If it goes wrong

- **Tentacle tips drooping or failing** — supports are too sparse. Increase support density or reduce maximum overhang angle.
- **Supports fused to the model surface** — support contact distance too small (or zero). Set Z contact distance to 0.2 mm and reprint.
- **Supports won't remove cleanly** — printed in ABS or PETG without adjusting contact distance. These materials bond more aggressively to supports.
- **Body looks fine but tips are rough** — this is normal for supported surfaces. A light sanding with 400-grit sandpaper cleans up support marks.
