# Dock — Brand Kit

The visual identity for [Dock](https://trydock.ai) — the AI workspace for you, your team, and every agent you run.

> Writing about Dock? Building an integration page? Recording a podcast?
> Grab whatever you need from this repo. No need to ask.

![Dock](lockup/lockup-light-512.png#gh-light-mode-only)
![Dock](lockup/lockup-dark-512.png#gh-dark-mode-only)

## Quick links

- **Mark only** (favicon, app icon, social avatar) → [`mark/mark-512.png`](mark/mark-512.png) · [other sizes](mark/)
- **Horizontal lockup** (orb + Dock wordmark) → [`lockup/lockup-light-1024.png`](lockup/lockup-light-1024.png) · [dark](lockup/lockup-dark-1024.png) · [JPGs on white/dark](lockup/)
- **Wordmark only** → [`wordmark/`](wordmark/)
- **Brand colors** → [`colors/swatches.png`](colors/swatches.png)
- **Pre-sized for common uploaders** (status pages, integration directories) → [`uploaders/`](uploaders/)
  - `uploaders/400x200/` — fits the common "logo: ≤400×200, ≤150KB, png/jpg" slot
  - `uploaders/96x96/` — fits the common "favicon: ≤96×96, ≤150KB, png/gif/ico" slot, including a multi-resolution `.ico`

Need a different size, format, or variant? File an issue.

## Usage

✅ **Do**

- Use these assets in articles, blog posts, podcasts, conference decks, integration pages, and anywhere you genuinely reference Dock.
- Link the mark to <https://trydock.ai>.
- Use **Fraunces SemiBold (600)** with `-0.025em` letter-spacing for any wordmark recreation.
- Keep the orb's white outer ring and halo glow intact at every size — they make the mark legible on dark surfaces.

🚫 **Don't**

- Recolor the orb. The palette is strict (Scout `#0A84FF`, Argus `#FF2D92`, Flint `#BF5AF2`).
- Modify the mark or wordmark in any way (no strokes, no inversions, no new typefaces).
- Use the brand to imply endorsement, partnership, or affiliation that doesn't exist.
- Use the brand for anything misleading, illegal, or harmful.

For unusual uses (merch, event sponsorship, anything visible to a large audience) — drop us a line at <support@trydock.ai>.

## Hot-link from anywhere

Every file in this repo is hot-linkable from `raw.githubusercontent.com`. Example:

```html
<img
  src="https://raw.githubusercontent.com/try-dock-ai/brand/main/mark/mark-128.png"
  alt="Dock"
  width="32" height="32"
/>
```

For Markdown READMEs, prefer the GitHub-mode-aware embed:

```markdown
![Dock](https://raw.githubusercontent.com/try-dock-ai/brand/main/lockup/lockup-light-512.png#gh-light-mode-only)
![Dock](https://raw.githubusercontent.com/try-dock-ai/brand/main/lockup/lockup-dark-512.png#gh-dark-mode-only)
```

## What's in here

```
brand/
├── mark/                       # orb only
│   ├── mark-{32,64,128,256,512,1024,2048}.png        (transparent)
│   ├── mark-{256,512,1024,2048}-on-white.jpg
│   └── mark-{256,512,1024,2048}-on-dark.jpg
├── lockup/                     # orb + Dock wordmark
│   ├── lockup-{light,dark}-{128,256,512,1024}.png    (transparent)
│   └── lockup-{256,512,1024}-on-{white,dark}.jpg
├── wordmark/                   # Dock wordmark only (no orb)
│   ├── wordmark-{light,dark}-{128,256,512,1024}.png  (transparent)
│   └── wordmark-{256,512,1024}-on-{white,dark}.jpg
├── uploaders/                  # pre-sized for common uploader slots
│   ├── 400x200/                # ≤400×200, ≤150KB (status pages, integration listings)
│   │   ├── lockup-400x200.png · lockup-dark-400x200.png  (transparent)
│   │   ├── lockup-400x200-on-{white,dark}.jpg
│   │   └── mark-400x200(.png|-on-white.jpg)              (centered orb in wide canvas)
│   └── 96x96/                  # ≤96×96, ≤150KB (favicons)
│       ├── mark-96.png · mark-96-on-white.png
│       ├── mark-96.ico                                   (multi-resolution: 16/32/48/96)
│       └── mark-96-single.ico                            (96 only)
└── colors/                     # color-system swatches
    ├── swatches.svg
    ├── swatches.png
    └── swatches.jpg
```

## Colors

### Brand triad

| Name  | Hex      | RGB              | Used for                              |
| ----- | -------- | ---------------- | ------------------------------------- |
| Scout | `#0A84FF`| 10, 132, 255     | Scout (Claude Sonnet) agent identity  |
| Argus | `#FF2D92`| 255, 45, 146     | Argus (Claude Opus) agent identity    |
| Flint | `#BF5AF2`| 191, 90, 242     | Flint (Claude Haiku) agent identity   |

The mark blends all three into an iridescent conic gradient (purple top → blue right → pink bottom-left). No cyan, no magenta-bridge — those three colors only.

### Ink + surface

| Name     | Hex      | Use                                  |
| -------- | -------- | ------------------------------------ |
| Ink      | `#1A2332`| Body text, wordmark on light bg      |
| Dark ink | `#0F1722`| Dark-theme background                |
| Surface  | `#F7F9FB`| Light-theme background               |
| White    | `#FFFFFF`| Card surfaces, wordmark on dark bg   |

## Typography

- **Display / wordmark** — [Fraunces](https://fonts.google.com/specimen/Fraunces) SemiBold (600), `-0.025em` letter-spacing
- **Sans (body, UI)** — [Inter](https://fonts.google.com/specimen/Inter)
- **Mono (code only)** — [JetBrains Mono](https://www.jetbrains.com/lp/mono/)

All three are open-source.

## License

Brand assets © Vector Apps, Inc. Provided under the **Dock Brand Use Policy** (see [USAGE.md](USAGE.md)) — basically: use them to refer to Dock, don't pretend to be Dock.

The README and source recipe in this repo are MIT.

---

— [trydock.ai](https://trydock.ai) · [docs](https://trydock.ai/docs) · [status](https://status.trydock.ai)
