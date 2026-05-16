---
title: "Bed Adhesion and the First Layer"
order: 7
est_read_time_minutes: 6
callout: "You'll come back to this the first time a print pops off mid-print or you can't get the first layer to look right. The diagnostic order here — offset, then clean, then temperature, then brim — solves 95% of adhesion problems."
---

The first layer is the foundation everything else sits on. If it's wrong, every layer above it will be wrong too, and the print will eventually fail.

## The mental model

Think of the first layer like the base coat of paint on a wall. If the surface is dirty, the paint won't stick. If you apply it too thick or too thin, the result is poor. Get the base coat right and everything on top of it is easier.

The two things that control first-layer quality are: **Z offset** (how close the nozzle is to the bed) and **bed temperature** (how well the first layer stays stuck).

## The three failure modes

![First layer: good vs bad](/images/diagrams/first-layer-comparison.svg)

### Too far from bed

The nozzle is too high. The plastic falls to the bed instead of being squished into it. Lines don't stick to each other and may not adhere to the bed at all. Prints come out looking like loose spaghetti.

**Fix:** lower the Z offset by 0.05 mm increments. Most printers let you adjust this via a "baby step" Z dial during the print.

### Too close to bed

The nozzle is too low. It scrapes across the bed, drags through already-deposited plastic, and can scratch or gouge the build surface. The first layer may look fine, but the nozzle resistance will cause the extruder motor to skip or click.

**Fix:** raise the Z offset by 0.05 mm increments.

### Good first layer

Lines are touching, slightly shiny, and stay flat. They look like they've been ironed into the bed surface. This is what you're aiming for.

## Four solutions to adhesion problems

Try these in order:

### 1. Re-run bed leveling

If your first layer looks different in different corners of the bed, the bed isn't level. Run auto-leveling or manually re-level before adjusting the Z offset.

### 2. Clean the build plate

Oils from your hands are invisible but break adhesion. Use a paper towel and isopropyl alcohol (IPA, 70% or higher) to wipe the entire build surface before each print. Do this every print — not just when you have problems.

### 3. Raise bed temperature

PLA on PEI: 60°C is the standard. If you're having trouble, try 65°C. The extra heat keeps the first layer plastic for slightly longer, giving it more time to bond.

PETG: 70–85°C. PETG actually bonds too well to bare PEI at high temperatures — if you have trouble removing the part after the print, lower the bed temp slightly.

### 4. Add a brim in the slicer

A brim is extra material printed around the base of the model, attached to it, to increase the footprint that contacts the bed. Slice with a brim of 5–10 mm for anything tall and thin, anything printed in ABS, or any model that's been popping off mid-print.

## Build surface types

**PEI spring steel sheet** — the most recommended surface for beginners. PLA and PETG stick well when hot and release cleanly when cool. Easy to clean. Handles being flexed to pop parts off without damage. This is what most modern printers ship with.

**Glass** — flat and heat-resistant, but requires glue stick or hairspray for reliable adhesion. Works fine once you get the adhesive layer right; more fiddly to maintain than PEI.

**BuildTak** — a textured surface that grips well. Good for ABS. Parts can be hard to remove if you over-stick them.

## The quick test for a newly levelled bed

Before any long print, print a single-layer square that covers most of the build plate. A 150×150 mm single-layer square takes about 4 minutes and immediately shows you if the leveling is consistent across the bed. Fix any problem areas before committing to a multi-hour print.

## What can go wrong

- **Touching the build plate after cleaning** — you've immediately re-contaminated it. Clean, don't touch, print.
- **Chasing Z offset without leveling first** — if the bed is tilted, no single Z offset value will work across the whole surface. Level first, then fine-tune the offset.
- **Using glue stick on PEI** — PEI is designed to work without any adhesive for PLA. Glue stick can make adhesion worse by creating an uneven surface. Use it only on glass or bare metal beds.
- **Assuming the bed level drifts randomly** — it usually doesn't. If your previously-good leveling has gone off, look for a physical cause: the printer was moved, a Z end-stop loosened, or the bed hardware shifted. Find the cause before re-leveling.
