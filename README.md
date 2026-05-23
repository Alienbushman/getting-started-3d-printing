# getting-started-3d-printing

Beginner-friendly 3D printing guides and printable models. Deployed at `alienbushman.com/3d-printing/`.

**Stack:** Astro 5 · Tailwind CSS · Three.js (STL viewer) · Pagefind (static search) · nginx (Docker)

## Local dev

```bash
npm install
npm run dev        # http://localhost:4321/3d-printing/
```

## Build

```bash
npm run build      # output → dist/
```

## Docker

```bash
docker build -t 3d-printing .
docker run --rm -p 8080:80 3d-printing
# open http://localhost:8080/3d-printing/
```

## Model library

Each model lists licence, author, and source. STL downloads happen on the original
author's page (Printables for 8 of 10, the same Printables mirrors for 3DBenchy +
flexi-rex that the upstream GitHub repos publish) — this site curates and teaches;
the authors host. 4 of 10 are CC-BY-NC (non-commercial only) and clearly marked in
the UI before you leave the site.

### Why we link

Smaller artefact, no re-distribution attribution burden in this repo, fresh files
if authors update their models, and authors get the engagement on their own page.
Source links are inert if the upstream model is taken down — that's a real cost
and the trade-off accepted for v0.1.1.

## What's in v0.2.0

- `:039` — **Pagefind site search** at `/search/`. Static index built into the
  Docker image at deploy time; covers models, guides, and glossary.
- `:040` — **Beginner path** at `/start/`. 10 models in numbered curriculum order
  via a new `learning_order` schema field; each step calls out the skill it teaches.
- `:041` — **Failure diagnostic** at `/diagnose/`. Symptom-picker UI on top of
  the common-failures guide; pick what you see, get the focused fix sequence.
- `:042` — **Three.js STL viewer** on every detail page. Drag-orbit / scroll-zoom
  preview, loaded from decimated viewer-quality copies in `public/models/` (the
  primary download CTA still goes to the upstream source).

## What's in v0.1.1

- `:032` — rewrite the two-color-coin entry against the actual chosen model
  (SnobbishGoose's CC0 Dual Extrusion Calibration Coin) instead of a TBD placeholder.
- `:033` — `commercial_use` schema field plus an amber "Non-commercial" pill on the
  gallery, homepage, and detail page for the 4 CC-BY-NC models. Sync 5 model
  frontmatters with the verified licence data from `research/models.yaml`.
- `:037` — replace the never-shipped local "Download STL" button with a primary
  "Get the STL on Printables →" CTA that opens the author's page (`rel="noopener
  external"`, `target="_blank"`).

## License

Site code: MIT. Model files retain their original licenses (see each model detail page).
