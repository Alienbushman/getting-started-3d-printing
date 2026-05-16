# Project Scope — getting-started-3d-printing

Locked 2026-05-16 via planner ticket [getting-started-3d-printing:001] (#2059).
Mirror in memory: artifact #591 (scope=getting-started-3d-printing, category=decision, importance=1.5).

Downstream tickets read this file. Do not re-litigate without going through a new planner ticket.

## 1. URL path prefix: `/3d-printing/`

Trailing slash enforced. Matches the sibling convention (`/imdb/`, `/cars/`, `/geometric-shape-generator/`) under alienbushman.com.

Reflect in:
- Astro `base` config (`astro.config.mjs`)
- `alienbushman-website` docker-compose env (sibling repo)
- nginx `location /3d-printing/ { ... }` block (sibling repo)
- landing card `href` (sibling repo)

## 2. Tech stack: Astro 5 + content collections + Tailwind

Rationale: static-first; matches the `landing/` Astro 5 sibling. Content collections handle markdown guides + per-model entries with STL/image attachments natively. Rejected only-with-reason: nothing dynamic enough here to warrant a server runtime.

## 3. Visual tone: workshop / builder

NOT poetic, NOT manifesto. Sign-off `alienbushman` everywhere a sign-off appears; real name never in public content.

Reference URLs nailing the vibe (use these as anchors before writing copy):
- https://alienbushman.com — parent brand landing
- https://alienbushman.com/imdb/ — sibling showing content + UI density
- https://www.printables.com/ — 3D-printing-native density pattern (adopt directness, not their brand)

## 4. Content scope cap (v0.1.0)

- 8 getting-started guides
- 10 model entries
- No video (deferred — hosting/encoding adds platform decisions not load-bearing for "getting started")

## 5. License

- Site code: MIT (see `LICENSE` at repo root)
- Model files: keep their original license (CC0 / CC-BY / etc.). Never relicense. Each model entry's frontmatter records the original license + attribution.
