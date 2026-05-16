---
title: "Filament 101: PLA, PETG, and ABS"
order: 4
est_read_time_minutes: 7
callout: "You'll come back to this when a print fails in a way that looks like a material problem — warping, stringing more than usual, or parts breaking at the layer line. Match the symptom to the material section here first."
---

Filament is the raw material your printer melts and deposits. Picking the wrong one for your use case is one of the most common beginner mistakes. The good news: the right material for a first printer is almost always PLA.

## The mental model

Think of filament materials like paint types: watercolour, oil, acrylic. Each has a different working temperature, drying time, and strength once cured. You wouldn't use watercolour to paint outdoor furniture. You wouldn't use oil paint for a quick sketch. Same logic applies to filament.

## The three materials you need to know

| | PLA | PETG | ABS |
|---|---|---|---|
| **Nozzle temp** | 200–215°C | 230–245°C | 230–250°C |
| **Bed temp** | 55–65°C | 70–85°C | 90–110°C |
| **Enclosure needed** | No | No (helps) | Yes |
| **Common use** | Prototypes, decorative, learning | Functional parts, water-resistant | Heat-resistant, structural |
| **Common failure** | Warps if bed too cold; brittle | Stringing; moisture-sensitive | Severe warping; toxic fumes if unenclosed |

### PLA (Polylactic Acid)

PLA is the easiest filament to print. It prints at low temperatures, sticks well to a heated PEI bed, doesn't warp much, and doesn't require an enclosure. It's made from corn starch and is technically biodegradable — though it takes industrial composting conditions to actually break down.

The catch: **PLA has a low heat resistance**. It softens around 60°C, which means it will deform in a car on a hot day, or anywhere near a heat source. It's also more brittle than PETG or ABS under impact.

Use PLA for: decorative prints, organizers, anything that won't see heat or mechanical stress.

### PETG (Polyethylene Terephthalate Glycol)

PETG is PLA's more capable sibling. It's tougher, slightly flexible, and more heat-resistant (around 80°C). It's good for functional parts like brackets, clips, and anything that needs a bit of give under load.

The trade-offs: PETG strings more than PLA. It's also moisture-sensitive — store your spool in a sealed bag with desiccant, or you'll get bubbling and poor layer adhesion. Print temperatures are higher, so make sure your hot end can handle it (most can).

Use PETG for: functional parts, anything that needs impact resistance, outdoor-ish use.

### ABS (Acrylonitrile Butadiene Styrene)

ABS is strong, impact-resistant, and heat-tolerant (up to 100°C+). It's what LEGO bricks are made of. It's also the hardest of the three to print.

ABS warps — badly. Without an enclosure to maintain a consistent ambient temperature, the part will curl off the bed mid-print. It also produces fumes that are unpleasant and potentially harmful. You need an enclosure with ventilation.

Use ABS for: parts that see real heat or impact, enclosure-mounted hardware, anything that needs to live in a car.

**Beginner recommendation: skip ABS until you've nailed PLA and PETG.**

## The practical flowchart

1. **Start with PLA.** It's forgiving, cheap, and covers 80% of beginner use cases.
2. **Switch to PETG** when you need something tougher or slightly heat-resistant, and once you've dialled in your first-layer settings.
3. **Add ABS** only when you have a specific need for high heat resistance and you've already got an enclosure.

## What can go wrong

- **Using moisture-damaged filament** — PETG and ABS absorb moisture from the air. If your prints are bubbling, snapping, or producing inconsistent extrusion, the filament may be wet. Dry it in a food dehydrator at 65°C for 6–8 hours.
- **Storing filament open on a shelf** — PLA tolerates this better than PETG/ABS, but ideally store all filament in sealed bags or airtight containers with desiccant.
- **Printing ABS without an enclosure** — the base of the print will cool too fast, contract, and peel off the bed. This isn't a settings problem; it's a physics problem. The fix is an enclosure.
- **Mixing up temperature settings** — if you load PETG and forget to change the temperature from your PLA profile, you'll under-extrude or clog. Always double-check the material in the slicer before printing.
