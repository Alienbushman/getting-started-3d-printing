---
title: "Slicer Basics"
order: 5
est_read_time_minutes: 8
callout: "You'll come back to this when you want to understand why a print failed — most failure causes can be traced to a specific slicer setting. Check the five settings in this guide before assuming the printer is broken."
---

A slicer is the software that converts your 3D model into instructions the printer can follow. It sits between the model file and the print.

## The mental model

Your 3D model is a description of a shape — a mesh of triangles in 3D space. The printer can't use that directly. The slicer slices the model into horizontal layers and generates a path for the nozzle to follow on each layer, along with temperature commands, fan speed commands, and retraction moves. The output is a file called **G-code**.

Think of the slicer as a compiler: source code goes in, machine instructions come out. You configure it; it translates.

## Two slicers worth knowing

**PrusaSlicer** — free, open-source, works with any FDM printer. Strong default profiles, excellent layer preview, good documentation. This is the reference slicer for this site.

**Bambu Studio** — free, based on PrusaSlicer. Best choice if you have a Bambu Lab printer. The UI is slightly cleaner; the feature set is similar.

Both are free. Download whichever matches your hardware.

## The basic workflow

1. **Import your model** — drag an STL or 3MF file into the slicer window, or use File → Import.
2. **Choose your printer profile** — select your exact printer model from the list. This sets bed size, max temperatures, and other hardware limits.
3. **Set the material** — select PLA, PETG, or ABS. The slicer adjusts temperatures automatically.
4. **Configure the five key settings** (see below).
5. **Preview the layers** — click the layer preview slider and scrub through the layers. Look for obvious gaps, missing supports, or weird toolpaths.
6. **Export G-code** — save to SD card, USB, or send directly to the printer if you have a network connection.

## The five settings you'll actually touch

### 1. Layer height

Controls how thick each printed layer is. Thinner layers = smoother surface, longer print time. Thicker layers = faster print, more visible layer lines.

- **0.1 mm** — fine detail, slow. Good for figurines.
- **0.2 mm** — the default. Right for almost everything.
- **0.3 mm** — fast, coarser. Good for functional parts where appearance doesn't matter.

Start at 0.2 mm and only go lower if you have a specific reason.

### 2. Infill percentage

How solid the inside of the print is. 0% = hollow shell. 100% = solid plastic.

- **15%** — default for decorative prints. Plenty strong for anything non-functional.
- **40%** — functional parts that need strength.
- **80%+** — rarely needed; the perimeter walls provide most of a part's strength anyway.

### 3. Supports

Supports are automatically generated scaffolding for overhanging geometry. Any part of the model that overhangs more than about 45° from vertical without something below it will sag or fail without support.

Turn supports on when: the model has overhangs greater than 45°, bridges longer than ~80 mm, or the slicer preview shows unsupported sections.

Use **tree supports** when available — they touch the model at fewer points and leave a cleaner surface.

### 4. Print speed

How fast the nozzle moves. Faster = less time, more risk of errors (layer shifts, vibration artefacts, under-extrusion on corners).

Start at **50 mm/s** for everything and only increase after you've had a few successful prints. The stock profiles are usually safe.

### 5. Brim

A brim is a flat ring of extra material printed around the base of your model, attached at the bottom layer. It increases the footprint that contacts the bed, improving adhesion.

Use a brim when: you're printing something tall and thin, something with a small footprint, or ABS/PETG that tends to warp.

Width: 5–10 mm is usually enough.

## What can go wrong

- **Using the wrong printer profile** — a profile for a 0.6 mm nozzle will generate paths that are too wide for a 0.4 mm nozzle. Double-check the profile every session.
- **Not previewing the layers** — the layer preview catches 90% of obvious problems before you start a 10-hour print. Always scrub through it.
- **Turning supports off when the model needs them** — the slicer will warn you if overhangs are steep, but it won't stop you. Look at the model in the preview and identify any sections that are floating in mid-air.
- **Cranking speed up to save time** — a 3-hour print at 100 mm/s that fails halfway costs more time than a 4-hour print at 50 mm/s that succeeds. Speed up gradually, only after you've confirmed quality at lower speeds.
