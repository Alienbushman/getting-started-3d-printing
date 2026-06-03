# Model Attribution — getting-started-3d-printing

Compiled 2026-05-16 for ticket [getting-started-3d-printing:006].
Sign-off: alienbushman.

This file must be kept in sync with `research/models.yaml`.
Before downloading any STL, confirm the license at the source URL listed below.
All model files retain their original licenses — this project's MIT code license
does NOT extend to model files (see PROJECT_SCOPE.md §5).

---

## Attribution Table

| # | Slug | Title | Author | License | Source / License URL | Verify Status |
|---|------|-------|--------|---------|----------------------|---------------|
| 1 | `3dbenchy` | 3DBenchy — The Jolly 3D Printing Torture Test | CreativeTools | **Public Domain** | https://www.printables.com/model/3161 | ✅ Confirmed |
| 2 | `xyz-calibration-cube` | XYZ 10mm Calibration Cube | Halit | CC 4.0 (variant TBC) | https://www.printables.com/model/32539 | ⚠ Unverified |
| 3 | `low-poly-dog` | Low Poly Dog | Andrew_Sink (remix: EliasRosseau) | CC (variant TBC) | https://www.printables.com/model/35662 | ⚠ Unverified |
| 4 | `cable-clip` | Simple Cable Clip | Jan-E.de | CC (variant TBC) | https://www.printables.com/model/125902 | ⚠ Unverified |
| 5 | `snap-fit-box` | Storage Box with Snap-Fit Lid | Extrutim | CC (variant TBC) | https://www.printables.com/model/20961 | ⚠ Unverified |
| 6 | `flexi-rex` | Flexi Rex with Stronger Links | DrLex (remix: Kirbs → airfish/zheng3) | **CC-BY-SA 4.0** | https://www.printables.com/model/46241 | ✅ Confirmed |
| 7 | `spiral-vase-rose` | Spiral Vase Rose | lytta | CC-BY (probable) | https://www.printables.com/model/131488 | 🔶 Probable |
| 8 | `cute-mini-octopus` | Cute Mini Octopus | McGybeer | CC (variant TBC) | https://www.printables.com/model/178035 | ⚠ Unverified |
| 9 | `nameplate` | Nameplate | Makkuro | CC (variant TBC) | https://www.printables.com/model/33277 | ⚠ Unverified |
| 10 | `two-color-coin` | Dual Extrusion Calibration Coin | SnobbishGoose | **CC0-1.0** | https://www.printables.com/model/346994 | ✅ Confirmed |

**Legend:** ✅ Confirmed · 🔶 Probable (verify before use) · ⚠ Unverified (must check manually) · ❌ Not yet selected

---

## Verification Notes

The Printables.com license badge is rendered client-side and is not readable by automated
web scraping. All entries marked ⚠ or 🔶 **must be manually confirmed** by visiting the
source URL and checking the "License" badge on the model page before the STL is downloaded
into `research/_staging/`.

Suggested verification workflow:
1. Open the source URL in a browser.
2. Locate the "License" badge (usually near the model name or in the file info panel).
3. Confirm it is one of: CC0, CC-BY, CC-BY-SA, or CC-BY-NC (non-commercial projects only).
4. If the license is CC-BY-ND or all-rights-reserved: **remove from the list** and find a replacement.
5. Update this file and `models.yaml` with the confirmed license string and change status to ✅.

---

## Required Attributions for Confirmed Licenses

The following attributions MUST appear in the site wherever the model is displayed:

### 3DBenchy
> 3DBenchy by CreativeTools is in the public domain. No attribution required, but original
> source: https://www.printables.com/model/3161

### Flexi Rex with Stronger Links
> "Flexi Rex with stronger links" by DrLex is licensed under
> [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
> Based on Flexi Rex by Kirbs, airfish, and zheng3.
> Source: https://www.printables.com/model/46241

---

## Model #10 — Two-Color Calibration Coin

SnobbishGoose's Dual Extrusion Calibration Coin (Printables #346994).
Released CC0-1.0 (public domain). Confirmed via Printables model page 2026-05-17.
63.5 mm flat disc, no supports, teaches M600 filament-change workflow.
