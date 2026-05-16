---
title: "Common Failures and Fixes"
order: 8
est_read_time_minutes: 10
callout: "You'll come back to this every time a print looks wrong. Bookmark this page. Match the visual symptom to the failure mode and follow the one-step fix before touching any other setting."
---

Every failure has a specific cause and a specific fix. The goal here is to get you from "something looks wrong" to a working print in one change, not five.

## How to use this guide

Look at your failed print. Match what you see to one of the failure modes below. Apply the fix. Print again. If the problem persists after one change, move to the next likely cause.

**Do not change multiple settings at once.** If two changes happen simultaneously and the next print works, you've learned nothing.

---

## 1. Stringing

**What it looks like:** thin hairs of plastic connecting separate parts of the model, like a spider web between features.

**Cause:** the nozzle oozes plastic while moving between features. Usually too-high temperature or insufficient retraction.

**Fix — one step at a time:**
1. **Lower nozzle temperature by 5°C.** For PLA, try 210°C instead of 215°C.
2. If that doesn't fix it, **increase retraction distance by 0.5 mm** in the slicer. (Retraction pulls the filament back slightly before a travel move, reducing ooze.)
3. If you're still seeing strings after two adjustments, the filament may be wet — dry it first.

---

## 2. Layer shifting

**What it looks like:** the layers of the print are suddenly offset horizontally partway up — the top half of the print is misaligned from the bottom, like someone pushed it sideways.

**Cause:** the print head slipped on its axis. Usually loose belts, a collision between the nozzle and the print, or print speed too high.

**Fix:**
1. **Check belt tension.** Belts should be taut enough to twang like a guitar string. Loose belts skip. Most printers have a belt tensioner wheel — tighten it.
2. **Lower print speed.** High speed + sharp corners = the stepper motor loses steps. Try 50 mm/s.
3. **Check for collisions.** Did the nozzle catch on a warped corner or blob of plastic? A collision can shift the layer instantly.

---

## 3. Warping

**What it looks like:** the corners or edges of the print curl upward off the build plate, sometimes lifting the whole print mid-print.

**Cause:** the outer edges of the print cool and contract faster than the interior. The tension pulls the base off the bed. More common with larger flat prints and with ABS.

**Fix:**
1. **Re-run bed leveling and clean the bed with IPA.** Poor adhesion is the most common cause.
2. **Raise bed temperature by 5°C** (try 65°C for PLA, 80°C for PETG).
3. **Add a brim** — 5–10 mm around the model's perimeter.
4. **Enclose the printer** (for ABS) — warping in ABS is a physics problem that can't be fixed with settings alone without a warm enclosure.

---

## 4. Elephant's foot

**What it looks like:** the bottom of the print is wider than the rest — the first few layers flare outward, giving the print a slightly flared base.

**Cause:** the first layer is over-squished (Z offset too low) or the bed temperature is so high it's keeping the plastic soft for too long.

**Fix:**
1. **Raise the Z offset slightly** — 0.05 mm increments. The first layer should be squished, not pancaked.
2. **Lower bed temperature by 5°C** if the elephant's foot extends multiple layers.

---

## 5. Under-extrusion

**What it looks like:** gaps in the walls of the print, weak or missing layers, a rough or porous surface texture. The model looks like it wasn't printed with enough material.

**Cause:** the printer is depositing less plastic than it should. Could be a partial clog, incorrect temperature, wrong flow rate, or the extruder slipping on the filament.

**Fix:**
1. **Check nozzle temperature** — is it at the right value for your filament? A 5°C drop can cause significant under-extrusion.
2. **Cold pull** — heat the nozzle to print temp, then push filament through manually. Repeat a few times. This clears partial clogs.
3. **Increase flow rate (extrusion multiplier) by 5%** in the slicer if the above didn't work.
4. If the extruder is clicking or grinding: the nozzle is fully clogged and needs a cold pull or replacement.

---

## 6. Overheating (drooping or saggy layers)

**What it looks like:** fine features look melted, overhangs droop, the model looks saggy where there's no support below.

**Cause:** the part cooling fan isn't working, or the print speed is too high for small features (not enough time for the layer to cool before the next one is deposited on top).

**Fix:**
1. **Check the part cooling fan** — listen for it spinning during the print. If silent: check the fan wire connection or test the fan via the printer's menu.
2. **Enable "slow down for small layers"** in the slicer (usually called "minimum layer time" or similar). This forces the printer to slow down or pause on small cross-section layers.
3. **Lower nozzle temperature by 5°C** — slightly cooler plastic solidifies faster.

---

## 7. Z-banding

**What it looks like:** horizontal bands or ripples repeating at regular intervals around the outside of the print. Not random — the pattern repeats at a consistent height interval.

**Cause:** the Z lead screw has an imperfection, is not perfectly vertical, or the coupling between the motor and screw is loose. Each full rotation of the screw produces one band.

**Fix:**
1. **Check the lead screw coupling** — it's the coupler between the Z motor shaft and the lead screw. It should be tight and centred. A wobbling lead screw bends slightly each rotation.
2. **Lubricate the lead screw** — a dry screw produces more vibration. Use the PTFE-based grease (SuperLube or similar) recommended by your printer manufacturer.
3. **Reduce Z acceleration** in the slicer's machine settings if your firmware exposes it.

---

## 8. Clogged nozzle

**What it looks like:** no or very little plastic coming from the nozzle despite the extruder running. Extruder may be clicking. Under-extrusion across the whole print.

**Cause:** a piece of debris, carbonised filament, or foreign material is partially or fully blocking the nozzle bore.

**Fix — cold pull procedure:**
1. Heat the nozzle to 200°C.
2. Push a fresh piece of filament through manually until it extrudes.
3. Lower the temperature to 90°C (for PLA) while continuing to hold gentle forward pressure on the filament.
4. At 90°C, pull the filament out firmly in one smooth motion.
5. The end of the filament should come out as a plug shaped to the inside of the nozzle, with any debris embedded in it.
6. Repeat 2–3 times until the pulled plug is clean.

If cold pulls don't clear it, replace the nozzle — they're cheap and wear out.

---

## What to do when none of the above applies

If none of these match your failure, the next step is to search for your specific symptom + your printer model on Reddit or the manufacturer's forum. Include a photo of the failed print in your post. The community has seen almost everything.
