# getting-started-3d-printing

> Beginner-friendly 3D printing guides and printable models — deployed at [alienbushman.com/3d-printing/](https://alienbushman.com/3d-printing/)

A static site that teaches beginners how to 3D print through curated models, step-by-step guides, a glossary, and an interactive failure-diagnostic tool. Every page is generated at build time with Astro 5 and served from a Docker + nginx container inside the [alienbushman-website](https://github.com/Alienbushman/alienbushman-website) orchestrator.

## What's here

- **10 printable models** — curated beginner curriculum, ordered from first-print calibration to multi-colour M600 swaps. Each detail page shows difficulty, est. print time, recommended slicer settings, an interactive Three.js STL viewer, and a direct "Get the STL on Printables →" CTA to the author's page.
- **8-topic getting-started guide** — covers everything from choosing a printer to dialling in retraction, written for complete beginners.
- **~25-term glossary** — FDM jargon with gotchas, cross-references, and diagrams.
- **Failure diagnostic** — symptom-picker UI: choose what you see, get the focused fix sequence.
- **Pagefind site search** — static full-text index built at Docker deploy time; no runtime server needed.

## Tech stack

| Layer | Technology |
|---|---|
| Site generator | Astro 5 (static output) |
| Styling | Tailwind CSS 3 |
| 3D preview | Three.js + STLLoader + OrbitControls |
| Search | Pagefind (static index, built post-`astro build`) |
| Content | Astro content collections (MDX-lite Markdown) |
| Fonts | Fontsource — Inter 400/500/600 + Space Grotesk 600 (self-hosted) |
| Container | Docker — multi-stage: Node 22 build → nginx:alpine serve |
| Reverse proxy | nginx subpath `/3d-printing/` — part of alienbushman-website orchestrator |

## Project structure

```
getting-started-3d-printing/
├── src/
│   ├── content/
│   │   ├── models/        # 10 model Markdown entries (frontmatter + prose)
│   │   ├── guides/        # 8 beginner-guide topics
│   │   └── glossary/      # ~25 term definitions
│   ├── pages/             # Astro routes (index, models, guides, glossary, search…)
│   ├── components/        # StlViewer, ModelCard, Callout, DifficultyMeter, etc.
│   └── layouts/           # Base.astro — nav, footer, OG tags, skip-link
├── public/
│   ├── models/            # Decimated STL files for the in-browser viewer
│   └── images/            # Hero photo, diagrams (SVG), model preview thumbnails
├── research/              # models.yaml (source of truth), attribution.md, content outline
├── design/                # Visual-identity tokens, wireframe notes
├── docs/                  # AUDIT.md (a11y/perf/responsive results)
├── scripts/               # decimate-for-viewer.py (reduces STLs to ≤2 MB)
├── Dockerfile             # Multi-stage build → nginx:alpine
├── nginx.conf             # Subpath config: /3d-printing/ → /usr/share/nginx/html
└── astro.config.mjs       # base: '/3d-printing/', site: 'https://alienbushman.com'
```

## Local dev

```bash
npm install
npm run dev        # http://localhost:4321/3d-printing/
```

## Build

```bash
npm run build      # astro build + pagefind index → dist/
```

## Docker

```bash
docker build -t 3d-printing .
docker run --rm -p 8080:80 3d-printing
# open http://localhost:8080/3d-printing/
```

The Dockerfile installs all deps, runs `npm run build`, then copies `dist/` into an nginx:alpine image alongside `nginx.conf`.

## How content is organised

Content lives in three Astro collections under `src/content/`:

| Collection | File | Key frontmatter |
|---|---|---|
| `models` | `src/content/models/<slug>.md` | `title`, `difficulty`, `license`, `commercial_use`, `learning_order`, `source_url` |
| `guides` | `src/content/guides/<topic>.md` | `title`, `order`, `est_read_time_minutes` |
| `glossary` | `src/content/glossary/<term>.md` | `term`, `definition`, `see_also`, `gotcha` |

`research/models.yaml` is the canonical source of truth for model metadata — edit there first, then sync frontmatter. `research/attribution.md` records verified licence status for every model.

## Attribution & licence

**Site code** is released under the [MIT Licence](LICENSE).

**Model files** are NOT included in the MIT licence. Each model retains its original
licence (CC0, CC-BY, CC-BY-SA, or CC-BY-NC) as listed on its detail page and in
[`research/attribution.md`](research/attribution.md).

**Images** are either original work (diagrams, model SVG placeholders) or sourced from
Unsplash under the Unsplash Licence. Full credits in
[`public/images/IMAGE_CREDITS.md`](public/images/IMAGE_CREDITS.md).

Models marked **Non-commercial only** are clearly badged in the UI before the user leaves
this site.

## Acknowledgements

Built as part of the [alienbushman.com](https://alienbushman.com) portfolio — a hub of
small projects that each demonstrate a production-quality implementation of a specific
technology. This site covers Astro 5 static generation, Tailwind design systems, and
Three.js 3D in the browser.

---

*— alienbushman*
