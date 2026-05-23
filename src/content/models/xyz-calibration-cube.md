---
title: "XYZ 10mm Calibration Cube"
image: "/images/models/xyz-calibration-cube.svg"
stl_path: "/models/xyz-calibration-cube.stl"
license: "CC-BY-4.0"
author: "Halit"
source_url: "https://www.printables.com/model/32539-xyz-10mm-calibration-cube"
difficulty: "beginner"
est_print_time_minutes: 20
supports_required: false
layer_height_mm: 0.2
description: "A 10 mm cube labelled with X, Y, Z axes. Print three copies, measure all axes with calipers, and tune your dimensional accuracy."
skill_tags: ["calibration", "no-supports", "measurement"]
featured: false
learning_order: 1
learning_skill: "Measure XYZ dimensional accuracy with calipers"
---

## Why print this

Dimensional accuracy matters the moment you print a functional part that needs to fit something else. This cube gives you a concrete, measurable benchmark. If the X axis is 10.3 mm instead of 10.0 mm, you know your flow rate is high. Measure it; fix it.

## Before you slice

Print three copies in a single job. Three samples average out bed variation and give you a meaningful data set. No supports, no brim needed on a flat 10×10 mm footprint. Use 0.2 mm layer height, 40% infill for rigidity.

## What to expect

1. Import the STL, duplicate it twice on the build plate (three copies total).
2. Slice at 0.2 mm layer height, 40% infill, no supports.
3. Print time is approximately 20 minutes for all three.
4. Let the bed cool, remove all three cubes.
5. With calipers, measure X, Y, and Z on all three copies. Target: 10.0 mm ± 0.2 mm on all axes.
6. If X/Y are off, adjust flow rate (extrusion multiplier) in the slicer. If Z is off, check layer height setting and Z offset.

## If it goes wrong

- **X/Y both over 10 mm** — extrusion multiplier too high. Reduce by 2–3%.
- **X/Y both under 10 mm** — extrusion multiplier too low. Increase by 2–3%.
- **Z too short** — layer height set incorrectly in slicer, or first-layer Z offset is wrong.
- **Elephant's foot at base** — first layer over-squished. Raise Z offset slightly and re-measure.
