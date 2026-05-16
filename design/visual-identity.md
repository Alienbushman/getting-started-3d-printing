# Visual Identity — getting-started-3d-printing

Locked 2026-05-16 via planner ticket [getting-started-3d-printing:008] (#2068). Read alongside PROJECT_SCOPE.md and design/wireframes.md.

Vibe references (locked at scope-lock #2059): alienbushman.com (parent), alienbushman.com/imdb/ (sibling), printables.com (3D-printing density). Workshop / builder, NOT poetic.

## Tokens

### Color

| token | hex | role |
|---|---|---|
| `bg` | `#FAF8F4` | warm paper background |
| `ink` | `#1A1A1A` | body text |
| `accent` | `#E85D2F` | brand — printer-filament-orange; primary CTAs, active states |
| `accent-soft` | `#FCE4D6` | accent tint for callouts |
| `success` | `#2D8F47` | confirmations |
| `warning` | `#D97706` | non-blocking caveats |
| `danger` | `#C53030` | print-will-fail caveats |
| `neutral-50` | `#F4F2EE` | hover background |
| `neutral-100` | `#E5E2DC` | borders, dividers |
| `neutral-300` | `#A8A39A` | muted text |
| `neutral-500` | `#6B675F` | secondary text |
| `neutral-900` | `#2A2724` | strong text on bg |

### Typography

- Display font: **Space Grotesk** (Google Fonts / Fontsource, free for commercial).
- Body font: **Inter** (Google Fonts / Fontsource, free for commercial).
- Single weight pair: Space Grotesk 600 (semibold) for headings, Inter 400/500 for body, Inter 600 for emphasis.

Scale (key into Tailwind `fontSize`):

| token | px | line-height | use |
|---|---|---|---|
| `xs` | 12 | 1.4 | metadata, captions |
| `sm` | 14 | 1.5 | secondary body |
| `base` | 16 | 1.6 | body |
| `lg` | 18 | 1.5 | lead paragraph |
| `xl` | 22 | 1.4 | h3 |
| `2xl` | 28 | 1.3 | h2 |
| `3xl` | 36 | 1.2 | h1 |

### Spacing + layout

- Base unit: **4px** (Tailwind default).
- Radius scale: `0` / `2` / `4` / `8` / `16` (use Tailwind's `rounded-{none,sm,DEFAULT,lg,2xl}` map).
- Container max-width: **1100 px** (content-focused, NOT page-stretching).
- Page horizontal gutter: `1rem` mobile, `2rem` tablet+, `3rem` desktop+.

### Breakpoints

| token | min-width | use |
|---|---|---|
| `sm` | 640px | mobile landscape / small tablet |
| `md` | 768px | tablet |
| `lg` | 1024px | desktop |
| `xl` | 1280px | large desktop |

## Imagery treatment

- **Model previews**: square 1:1 aspect ratio, locked. Easier grid, matches printables convention.
- **Image crop**: `object-cover` with focal point centred; if the source is wide, the model should be centred in the crop already.
- **Attribution**: caption below the image, `text-xs text-neutral-500`, format: "Model by <author>, <license-spdx>". On the detail page, full attribution callout (see wireframes §3).

## Motion

- Page transitions: **none**. Astro static page-load is the transition.
- Link hover: 1px underline appears (no movement). `text-decoration: underline; text-underline-offset: 2px;`.
- Card hover: subtle border colour shift (`neutral-100` → `accent-soft`). NO transform/lift. Workshop, not portfolio-bouncy.
- Buttons: 80ms opacity ease on press.

## Component primitives (build later, just enumerated here)

| primitive | variants | notes |
|---|---|---|
| `Button` | primary, secondary, ghost | primary = accent bg; secondary = outline ink; ghost = no border |
| `Card` | default, featured | featured has thin accent border-left |
| `Tag` / `Badge` | difficulty-beginner, difficulty-intermediate, kind:supports, kind:no-supports | small pill, `text-xs`, neutral bg |
| `DifficultyMeter` | 1–5 dots | 5 dots, filled-by-level |
| `Section` | default, alt-bg | alt-bg uses `neutral-50` |
| `Callout` | info, warn, danger | accent/warning/danger border-left, body in matching tint |
| `CodeBlock` | default | monospace + copy button |
| `ModelCard` | gallery, featured | wraps image + title + meta row |
| `GuideToc` | hub, sidebar | numbered list with `order` from collection |

## ASCII mocks (rendering targets)

### Card (default)

```
+-------------------------------------------+
|                                           |
|         [square 1:1 image]                |
|                                           |
+-------------------------------------------+
| Title in Space Grotesk 18                 |
| Difficulty ● ● ○ ○ ○   ·   ~3h            |
| `no-supports` `first-print`                |
+-------------------------------------------+
```

### Callout (warn)

```
+-------------------------------------------+
| ⚠  This print needs supports.             |
|     Watch the overhangs section first.    |
+-------------------------------------------+
```
- Border-left 3px solid `warning`, bg `accent-soft` if info or paper-neutral if warn.

## Mapping to Tailwind config

The coder turning this into `tailwind.config.ts` should:
- Set `theme.colors` from the token table above (use the exact keys).
- Set `theme.fontFamily` to `display: ['"Space Grotesk"', 'system-ui']` and `sans: ['Inter', 'system-ui']`.
- Set `theme.fontSize` from the scale table.
- Set `theme.borderRadius` from the radius scale.
- Set `theme.maxWidth.content` = `1100px`.
- Load both fonts via Fontsource (`pnpm add @fontsource/inter @fontsource/space-grotesk`) in the root layout.

## What's deliberately NOT here

- Dark mode. v0.1.0 ships light-only. Workshop tone is warm-paper; dark mode adds testing surface for marginal benefit on a content-static site.
- Logo / wordmark. Repo name renders as plaintext in the nav for v0.1.0.
- Custom illustrations. v0.1.0 uses photographs of models only.

Sign-off: alienbushman.
