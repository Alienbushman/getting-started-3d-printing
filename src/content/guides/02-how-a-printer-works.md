---
title: "How an FDM Printer Works"
order: 2
est_read_time_minutes: 6
callout: "You'll come back to this when something goes wrong mid-print and you need to know which part of the machine to look at. The anatomy here maps directly to the failure modes in Common Failures."
---

Before you start tweaking settings, you need a picture of what each part does. Once you have that mental map, every failure mode makes immediate sense.

## The mental model

An FDM printer is three machines in one:

1. **A motion system** — three axes (X, Y, Z) that move the print head over the bed.
2. **A heating system** — a hot end that melts filament, and a heated bed that keeps the first layer stuck.
3. **An extrusion system** — a motor that pushes filament into the hot end at a controlled rate.

The slicer software turns your 3D model into a sequence of movements and temperatures. The printer executes that sequence.

## Anatomy of an FDM printer

![Anatomy of an FDM printer](/images/diagrams/printer-anatomy.svg)

**Key parts:**

- **Build plate (bed)** — the flat surface the print sits on. Heated to keep the first layer from peeling off.
- **Z lead screw** — moves the bed (or the gantry) up and down. Each layer, the Z axis moves up by the layer height.
- **X gantry** — the horizontal rail the print head travels along.
- **Extruder** — the motor that grips the filament and pushes it toward the hot end.
- **Hot end** — the part that melts the filament. Contains a heater block, thermistor (temperature sensor), and nozzle.
- **Nozzle** — the small hole (usually 0.4 mm diameter) the melted plastic comes out of.
- **Part cooling fan** — blows cool air on the just-extruded plastic to solidify it quickly. Critical for bridges and overhangs.

## The print sequence

1. **Home** — the printer moves all axes to their zero positions.
2. **Heat up** — bed and hot end heat to their target temperatures. The printer waits.
3. **Skirt** — one or two loops printed around the outside of your model to prime the nozzle and check adhesion before the real print starts.
4. **First layer** — printed slowly with extra squish. The most critical layer.
5. **Subsequent layers** — each layer, the Z axis steps up by the layer height. Repeat until done.
6. **Cool down** — fan ramps up, heaters turn off. Don't remove the part until the bed cools.

## The four settings you actually control

The slicer sets all of these — you don't type them in manually at the printer. But you set them in the slicer before you export the G-code.

| Setting | What it controls | Beginner default |
|---|---|---|
| **Layer height** | Thickness of each printed layer. Thinner = smoother, slower. Thicker = faster, coarser. | 0.2 mm |
| **Print speed** | How fast the nozzle moves. Faster = faster print, more errors. | 50–80 mm/s |
| **Nozzle temp** | Melting temperature for the filament. Too low = under-extrusion. Too high = stringing. | 215°C for PLA |
| **Bed temp** | Temperature of the build plate. Helps the first layer stick. | 60°C for PLA |

## What can go wrong

- **Moving the printer while it's printing** — even a nudge can cause a layer shift. Put the printer on a stable surface.
- **Opening the slicer profile for the wrong printer** — nozzle temperatures and speeds vary. Always check your printer profile is selected before slicing.
- **Removing the part while the bed is still hot** — PLA printed on a PEI sheet pops off cleanly when the bed cools to room temperature. Force it hot and you'll gouge the sheet.
- **Ignoring the first layer** — if the first layer looks wrong (gaps, not sticking, or squished flat), pause and fix it. Don't walk away and check in an hour. See Bed Adhesion for what to look for.
