# Sitemap + Page Wireframes — getting-started-3d-printing

Locked 2026-05-16 via planner ticket [getting-started-3d-printing:007] (#2067). Read alongside PROJECT_SCOPE.md.

Tone reference: alienbushman.com (parent), alienbushman.com/imdb/ (sibling), printables.com (3D-printing density). Voice = workshop / builder. Sign-off `alienbushman` only.

## URL map

- `/` — Home
- `/models` — Model gallery
- `/models/[slug]` — Model detail
- `/guide` — Getting-started hub
- `/guide/[topic]` — Per-topic guide
- `/glossary` — Glossary (A-Z anchored)
- `/about` — About

All URLs sit under the `/3d-printing/` prefix when deployed via alienbushman.com (Astro `base`); the slugs above are repo-internal routes.

---

## 1. Home `/`

```
+---------------------------------------------------------+
| HERO                                                    |
|   H1: "Start printing in a day, not a month."           |
|   Sub: "10 beginner-friendly prints + 8 guides, no fluff."|
|   [Browse models] (primary)  [Read the guide] (secondary)|
+---------------------------------------------------------+
| WHAT YOU'LL LEARN (3-up cards)                          |
|   1. First print, slicer-to-bed in 20 min               |
|   2. Why your print failed (and what to change)         |
|   3. Picking a model you can actually finish            |
+---------------------------------------------------------+
| FEATURED MODELS (3-6 cards, picked by editor)           |
|   [image][title][difficulty][time]                      |
+---------------------------------------------------------+
| QUICK PATH (numbered, links to guide topics)            |
|   1. Pick a printer                                     |
|   2. Set up your first slice                            |
|   3. First print + troubleshoot                         |
+---------------------------------------------------------+
| Footer: alienbushman · github · license · sitemap       |
+---------------------------------------------------------+
```
Maps to: `guides[order ASC LIMIT 3]` for the quick path; `models[featured=true LIMIT 6]` for featured grid.

## 2. Model gallery `/models`

```
+---------------------------------------------------------+
| Filter chips: [All] [Difficulty: beginner|intermediate]  |
|   [Supports: yes|no] [Print time: <2h | 2-6h | >6h]      |
| Sort: [Difficulty ↑] [Print time ↑] [A-Z]               |
+---------------------------------------------------------+
| Grid (responsive 1/2/3 col)                             |
|   [img] title                                           |
|         diff | time | skill tag                         |
|   [img] ...                                             |
+---------------------------------------------------------+
```
Maps to: `models` collection filtered by query params, sorted by selected sort, paginated client-side (10 items expected — no server pagination needed).

## 3. Model detail `/models/[slug]`

```
+---------------------------------------------------------+
| ← Back to gallery                                       |
| H1: Model name           Difficulty: ● Beginner         |
| [Large hero image]       Print time: ~3h                |
|                          Supports: no                   |
| [Download STL] [Download 3MF (if present)]              |
+---------------------------------------------------------+
| METADATA BLOCK                                          |
|   License: CC-BY 4.0    Author: Source link             |
|   Layer height: 0.2 mm  Infill: 15%                     |
+---------------------------------------------------------+
| RECOMMENDED SLICER SETTINGS (copyable block)            |
|   nozzle_temp = 210°C                                   |
|   bed_temp = 60°C                                       |
|   ...                                                   |
+---------------------------------------------------------+
| WHAT TO EXPECT (step-by-step)                           |
|   1. Slice with the settings above.                     |
|   2. Watch the first layer carefully.                   |
|   3. ...                                                |
+---------------------------------------------------------+
| ATTRIBUTION CALLOUT                                     |
|   "Model by <author>, licensed CC-BY 4.0. Sourced from   |
|    <link>. We did not modify the geometry."             |
+---------------------------------------------------------+
```
Maps to: one row from `models` collection by slug. License callout is required for CC-BY entries.

## 4. Getting-started guide

### Hub `/guide`

```
+---------------------------------------------------------+
| H1: Getting started with 3D printing                    |
| Sub: Eight topics. ~45 minutes total. Skip around.      |
+---------------------------------------------------------+
| TOC (ordered)                                           |
|   01 Pick a printer                                     |
|   02 Slicer basics                                      |
|   ...                                                   |
+---------------------------------------------------------+
```

### Topic `/guide/[topic]`

```
+---------------------------------------------------------+
| ← Guide hub                          Topic 03 of 08     |
| H1: Topic name                       Est read: 6 min    |
+---------------------------------------------------------+
| Body (markdown render — headings, code blocks, images)  |
+---------------------------------------------------------+
| Callout: "You'll come back to this when <trigger>."     |
+---------------------------------------------------------+
| [← Prev: 02 Slicer basics]      [Next: 04 First print →]|
+---------------------------------------------------------+
```
Maps to: `guides` collection by slug; `prev`/`next` derived from `order` field.

## 5. Glossary `/glossary`

```
+---------------------------------------------------------+
| H1: Glossary                                            |
| Letter nav: A B C D E F ... (anchors to sections)       |
+---------------------------------------------------------+
| ## A                                                    |
|   **Adhesion** — How well your print sticks to the bed. |
|     [Optional inline image]                             |
|   **Ambient temp** — ...                                |
|                                                         |
| ## B                                                    |
|   ...                                                   |
+---------------------------------------------------------+
```
Maps to: `glossary` collection grouped by `letter` (derived from `term[0].toUpperCase()`).

## 6. About `/about`

```
+---------------------------------------------------------+
| H1: About this site                                     |
| Three sections of prose:                                 |
|   - Why this exists (workshop tone, ship-in-days vibe)  |
|   - How models are curated (license-clean, beginner cap)|
|   - License + attribution stance                        |
| Sign-off line: "— alienbushman, 2026"                   |
+---------------------------------------------------------+
```

---

## Astro content collection schemas

### `src/content/models/*.md` — `models` collection

| field | type | required | notes |
|---|---|---|---|
| `title` | string | yes | display name |
| `slug` | string | yes | URL slug (kebab-case) |
| `image` | string | yes | path under `public/models/` |
| `stl_path` | string | yes | path under `public/models/` |
| `threemf_path` | string | no | path under `public/models/` (optional 3MF) |
| `license` | string | yes | SPDX identifier (CC0-1.0 / CC-BY-4.0 / ...) |
| `author` | string | yes | original creator |
| `source_url` | string | yes | original upload location |
| `difficulty` | enum | yes | `beginner` \| `intermediate` |
| `est_print_time_minutes` | number | yes | integer minutes |
| `supports_required` | boolean | yes | true/false |
| `layer_height_mm` | number | yes | e.g. 0.2 |
| `slicer_settings` | object | no | freeform map; rendered as a copyable block |
| `description` | string | yes | 1-2 sentence summary for cards |
| `steps` | array<string> | no | "what to expect" numbered list |
| `skill_tags` | array<string> | no | e.g. `["first-print", "no-supports"]` |
| `featured` | boolean | no | surfaces on home featured grid |

### `src/content/guides/*.md` — `guides` collection

| field | type | required | notes |
|---|---|---|---|
| `title` | string | yes | topic name |
| `slug` | string | yes | URL slug |
| `order` | number | yes | 1..8; drives nav order |
| `est_read_time_minutes` | number | yes | integer |
| `callout` | string | no | "you'll come back to this when ..." |
| body (markdown) | — | yes | the topic body itself |

### `src/content/glossary/*.md` — `glossary` collection

| field | type | required | notes |
|---|---|---|---|
| `term` | string | yes | the entry name |
| `definition` | string | yes | 1-2 sentences |
| `image` | string | no | optional inline image path |

`letter` is derived at build time from `term[0].toUpperCase()`; not stored.

---

## Non-page concerns

- 404: simple, link back to `/` and `/models`. Workshop tone.
- Nav (global header): logo/text "getting-started-3d-printing" → `/`; links: Models, Guide, Glossary, About.
- Footer (global): copyright, license link, GitHub link, sign-off "alienbushman".
