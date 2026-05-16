---
title: "Your First Print, Step by Step"
order: 6
est_read_time_minutes: 10
callout: "You'll come back to this when you start a new print session after a break. The pre-flight checklist here is worth re-reading every time, especially after moving the printer or changing filament."
---

The first print is where everything becomes real. Follow these steps in order. Don't skip the first-layer check — it's the one step that prevents 80% of failed prints.

## Pre-flight checklist

Before you send anything to the printer, check these five things:

1. **Filament is loaded** — push the filament manually at the extruder and confirm it feeds smoothly into the hot end. If it's tangled on the spool, untangle it now.
2. **Build plate is clean** — wipe the bed with a sheet of paper towel and a small amount of isopropyl alcohol (IPA, 70% or higher). Oils from your fingers cause prints not to stick.
3. **Nozzle isn't clogged** — heat the hot end to print temperature and manually push filament. It should flow out smoothly with no grinding or clicking from the extruder.
4. **Slicer profile matches the printer** — open your slicer, confirm the printer profile, and confirm the filament material.
5. **Bed is leveled** — run auto-level if your printer has it. If you adjusted the bed last session, run it again.

## Step 1: Level the bed

If your printer has auto bed leveling (ABL): run it. Most printers have a menu option under "Level", "Calibrate", or "Auto Home". Let it complete before starting the print.

**Success looks like:** the printer moves the nozzle to multiple points across the bed and takes measurements without touching the bed or skipping points.

**If it goes wrong:** the nozzle may drag on the bed (Z offset too low) or float too high (Z offset too high). See the Bed Adhesion guide.

## Step 2: Load filament

Heat the hot end to the print temperature for your material (215°C for PLA). Once at temperature, push the filament into the extruder until you see it coming out of the nozzle. The extruded filament should be smooth and consistent, not bubbly or discoloured.

**Success looks like:** a thin, consistent strand of plastic comes out of the nozzle without bubbling or snapping.

**If it goes wrong:** if the extruder is grinding or clicking, the filament is probably not reaching the hot end. Remove and re-insert; check that the Bowden tube is fully seated.

## Step 3: Choose your model and slice it

For your first print, use the **3DBenchy** or an **XYZ calibration cube** — both are in the Model Gallery. These are the standard first-print models for a reason: they test a range of printer behaviours in a short time.

Open your slicer, import the model, select your printer profile and material, and use the default settings. No tweaks yet. Export the G-code.

**Success looks like:** the slicer shows the model on the build plate, generates a clean preview with no floating sections, and exports without errors.

## Step 4: Start the print and watch the first layer

Transfer the G-code to your printer and start the print. **Stay and watch the first layer.** This is not optional.

The printer will lay a skirt loop first (a ring around the model — this primes the nozzle). Then it will start the first layer of the model itself.

Look for:

- Lines that are touching each other with a slight sheen → **good**
- Lines with gaps between them → **too far from bed** — Z offset needs to go lower (closer)
- Lines squished completely flat, nozzle dragging → **too close to bed** — Z offset needs to go higher (further)
- Lines not sticking at all, curling up → **bed adhesion problem** — check bed temperature and cleanliness

![First layer comparison](/images/diagrams/first-layer-comparison.svg)

**Success looks like:** the first layer lines are touching, slightly squished into the bed, and shiny on top. The print doesn't lift at the corners.

**If it goes wrong:** see the Bed Adhesion guide.

## Step 5: Let it finish

Once the first layer looks good, you can step away. Check back every 30–60 minutes for long prints. Do not open any enclosure or touch the printer during a print.

**Success looks like:** layers build up evenly, no stringing or gaps, the model stays fixed to the bed.

**If it goes wrong during the print:** pause or cancel and diagnose. See Common Failures.

## Step 6: Remove the part

Wait until the bed has cooled to room temperature (below 30°C for PLA on PEI). The part should pop off easily — sometimes with a satisfying click. If it doesn't release, flex the PEI sheet slightly (if it's the spring steel type).

**Do not** force the part off a hot bed. You'll scratch the sheet or damage the print.

## Step 7: Inspect and iterate

Look at the finished part and ask:

- Do the layer lines look consistent, or are there gaps or blobs in specific areas?
- Did any layers shift? (Sudden horizontal offset)
- Is there stringing between features?
- Are there elephant's foot effects at the base? (Wider than expected at the bottom)

Note what you see. Each issue has a specific cause and fix — see Common Failures. Your second print will be better than your first.

## What can go wrong

- **Walking away during the first layer** — this is the single most preventable cause of failed prints. Five minutes of watching saves hours of wasted time.
- **Removing the part before the bed cools** — PEI sheets are expensive and easily scratched. PLA releases cleanly when the bed cools. Wait.
- **Changing multiple settings at once** — if your print fails, change one thing at a time. If you change three settings and the next print works, you don't know what fixed it.
- **Not cleaning the bed between prints** — even clean-looking hands leave oil. IPA before every print.
