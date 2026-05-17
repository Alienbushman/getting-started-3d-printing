# STL Download Manifest

Generated 2026-05-17 by the human-verification follow-up to [getting-started-3d-printing:013] / [getting-started-3d-printing:028].

All 10 STLs are staged here (this directory is gitignored). [getting-started-3d-printing:029] copies them into `public/models/` and verifies each is reachable via the built site.

## Verified + downloaded

| slug | bytes | license | source | safe to ship |
|---|---:|---|---|:-:|
| 3dbenchy | 11,285,384 | Public Domain | CreativeTools/3DBenchy GitHub master | yes |
| xyz-calibration-cube | 6,884 | CC-BY 4.0 | Printables CDN | yes |
| low-poly-dog | 94,065 | CC-BY-SA 4.0 | Printables CDN | yes |
| cable-clip | 125,484 | CC-BY-NC 4.0 | Printables CDN | non-commercial only |
| snap-fit-box | 71,384 | CC-BY-NC-SA 4.0 | Printables CDN | non-commercial only |
| flexi-rex | 745,584 | CC-BY-SA 4.0 | DrLex0/print3D-FlexiRex GitHub master | yes |
| spiral-vase-rose | 132,811,984 | CC-BY 4.0 | Printables CDN | yes (but see size note) |
| cute-mini-octopus | 11,218,584 | CC-BY-NC-SA 4.0 | Printables CDN | non-commercial only |
| nameplate | 337,919 | CC-BY-NC-SA 4.0 | Printables CDN | non-commercial only |
| two-color-coin | 547,684 | CC0 / Public Domain | Printables CDN (SnobbishGoose dual-extrusion coin) | yes |

## Decisions the user (or [getting-started-3d-printing:029]) still owns

1. **Non-commercial models (4 of 10).** cable-clip, snap-fit-box, cute-mini-octopus, nameplate are CC-BY-NC-* . The site is currently a non-commercial portfolio — keeping them is fine for that stance, and each is marked `commercial_use: false` in [research/models.yaml](research/models.yaml). If the site is ever monetised, swap these. Scouted CC-BY substitutes for octopus: Davis County Library "Cute Mini Octopus v2" (Thingiverse thing:5779691, CC-BY 4.0).

2. **spiral-vase-rose is 132 MB.** Too heavy for a casual web download — bandwidth, Docker image bloat, GitHub 100 MB single-file limit (would need git LFS). The model is over-tessellated; lytta exported with very high triangle density. Options: (a) downscale-decimate via slicer or trimesh before placing, (b) swap to a lighter spiral vase model, (c) ship via git LFS, (d) link to source instead of mirroring locally.

3. **two-color-coin source was changed** from "TBD" to SnobbishGoose's Dual Extrusion Calibration Coin (PD). The model markdown body at [src/content/models/two-color-coin.md](../src/content/models/two-color-coin.md) was written against a generic placeholder — it needs a content-pass to match the actual coin (63.5mm diameter, colour-change-line tuning use).

## How the downloads were obtained

For the eight Printables-sourced STLs:

```
POST https://api.printables.com/graphql/
{ print(id: <id>) { stls { name fileSize filePreviewPath } } }
```

The `filePreviewPath` (e.g. `media/prints/32539/stls/<folder_id>_<uuid>/<name>_preview.png`) gives the CDN folder. The STL lives at:

```
https://media.printables.com/<folder>/<lowercased-filename>.stl
```

Lowercased — Printables stores CDN objects lowercased, even when the API returns mixed-case `name`. Anonymous GET works.

For 3DBenchy and flexi-rex, the canonical home is GitHub and direct raw URLs work:
- https://raw.githubusercontent.com/CreativeTools/3DBenchy/master/Single-part/3DBenchy.stl
- https://raw.githubusercontent.com/DrLex0/print3D-FlexiRex/master/Flexi-Rex-improved.stl
