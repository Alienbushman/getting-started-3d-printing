# Contributing

This is a portfolio project. External pull requests are not actively solicited,
but corrections are welcome — especially:

- Typos or factual errors in guides or glossary entries.
- Broken source links (models move on Printables).
- Licence corrections for any model entry.

## How to add a model

1. **Research** — verify the licence at the source URL. Only CC0, CC-BY, CC-BY-SA,
   and CC-BY-NC licences are accepted (the NC variants must be flagged in the UI).
   Record the confirmed licence in `research/attribution.md`.

2. **Edit `research/models.yaml`** — add the model entry. This file is the canonical
   source of truth; frontmatter is synced from it.

3. **Add the Markdown entry** — create `src/content/models/<slug>.md` with the
   required frontmatter fields (see `src/content/config.ts` for the schema) and a
   prose body.

4. **Drop the STL** — place a decimated viewer-quality STL in `public/models/<slug>.stl`
   (target ≤ 2 MB; use `scripts/decimate-for-viewer.py` if the original is large).
   The primary download still links to `source_url` — we don't host the print-quality file.

5. **Add a thumbnail** — `public/images/models/<slug>.svg` (or `.jpg` from a slicer
   screenshot). Update `public/images/IMAGE_CREDITS.md` with provenance.

6. **Build and verify** — `npm run build` should pass with zero errors. Check the
   model card in the gallery, the detail page, and the STL viewer.

7. **Commit** — follow the existing commit style:
   `content: add <slug> model entry [getting-started-3d-printing:NNN]`

## Code style

- Tailwind only — no custom CSS unless unavoidable.
- No React or other heavy frameworks.
- Keep Astro components small and focused.
- All interactive elements must be keyboard-operable and have visible focus styles.
- No real names, emails, or private identifiers in any committed file.

## Licence

By submitting a pull request you agree your contribution is released under the
project's [MIT Licence](LICENSE).
