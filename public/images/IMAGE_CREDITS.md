# Image Credits — getting-started-3d-printing

Compiled 2026-05-16 for ticket [getting-started-3d-printing:009].
Sign-off: alienbushman.

---

## Hero Image

| File | Source URL | License | Author | Optimization |
|------|-----------|---------|--------|--------------|
| `hero.jpg` | https://unsplash.com/photos/a-3d-printer-is-in-action-in-a-workshop-zWIFZeu5qeE | [Unsplash License](https://unsplash.com/license) (free for commercial + non-commercial use; no attribution required) | Jakub Zerdzicki (@jakubzerdzicki) | 1600×900 px, JPEG q=70, 179 KB |

---

## Supporting Photos

| File | Source URL | License | Author | Optimization |
|------|-----------|---------|--------|--------------|
| `nozzle-closeup.jpg` | https://unsplash.com/photos/close-up-view-of-a-3d-printer-nozzle-46dKqAGqQAw | [Unsplash License](https://unsplash.com/license) | Jakub Zerdzicki (@jakubzerdzicki) | 1600×1067 px, JPEG q=85, 131 KB |
| `printer-in-operation.jpg` | https://unsplash.com/photos/close-up-of-a-3d-printer-in-operation-IrpcG2ZcOuM | [Unsplash License](https://unsplash.com/license) | Jakub Zerdzicki (@jakubzerdzicki) | 1600×1067 px, JPEG q=85, 150 KB |

Unsplash License summary: free to use for commercial and non-commercial purposes.
Attribution appreciated but not required. Cannot be sold as a standalone photo.

---

## Diagrams (original work)

All diagrams in `diagrams/` are original SVG files created for this project.
No third-party license applies.

| File | Description | Author |
|------|-------------|--------|
| `diagrams/printer-anatomy.svg` | Labelled cross-section of an FDM printer showing extruder, hot end, fan, gantry, lead screw, build plate, filament path | alienbushman |
| `diagrams/first-layer-comparison.svg` | Three-panel comparison: good first layer vs. too far from bed vs. too close to bed | alienbushman |
| `diagrams/support-removal.svg` | Two-panel: print with tree supports enabled vs. finished part after support removal | alienbushman |

---

## Model Preview Images (placeholders)

All files in `models/*.svg` are placeholder images generated for this project.
They are original work and require no third-party attribution.
Replace each with a real render or slicer screenshot before the v0.1.0 release.

**Replacement workflow:**
1. Open the slicer (PrusaSlicer or Bambu Studio).
2. Import the STL from `public/models/<slug>.stl`.
3. Orient the model, apply the default colour, and take a screenshot at 4:3 aspect ratio.
4. Optimize: max 1600 px long edge, JPEG q=85, target ≤200 KB.
5. Save as `public/images/models/<slug>.jpg` (replacing the .svg placeholder).
6. Update this file with the new entry (source = "slicer screenshot", license = "original work").

| File | Slug | Status |
|------|------|--------|
| `models/3dbenchy.svg` | 3dbenchy | PLACEHOLDER — replace with slicer render |
| `models/xyz-calibration-cube.svg` | xyz-calibration-cube | PLACEHOLDER |
| `models/low-poly-dog.svg` | low-poly-dog | PLACEHOLDER |
| `models/cable-clip.svg` | cable-clip | PLACEHOLDER |
| `models/snap-fit-box.svg` | snap-fit-box | PLACEHOLDER |
| `models/flexi-rex.svg` | flexi-rex | PLACEHOLDER |
| `models/spiral-vase-rose.svg` | spiral-vase-rose | PLACEHOLDER |
| `models/cute-mini-octopus.svg` | cute-mini-octopus | PLACEHOLDER |
| `models/nameplate.svg` | nameplate | PLACEHOLDER |
| `models/two-color-coin.svg` | two-color-coin | PLACEHOLDER (model not yet selected) |

---

## General Constraint Reminder

- No real-name watermarks in any asset.
- Every asset must have a traceable license before use in production.
- Model STL files retain their original CC0/CC-BY/etc. licenses (see `research/attribution.md`).
- Site code (MIT) does NOT extend to image or model assets.
