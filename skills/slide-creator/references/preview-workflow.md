# Marp Server Preview + Playwright Review

Use this workflow to preview Marp slides in server mode and review specific pages with Playwright.

## Preconditions

- `marp` CLI installed
- Playwright installed with Chromium
- A slide directory that contains `slides.md` and related assets

## Full workflow

1) Start Marp server mode from the slide directory:
```bash
marp -s examples/slides/marketplace/
```

2) Confirm the preview URL loads:
```
http://localhost:8080/slides.md
```

3) Jump to a specific page using the hash:
```
http://localhost:8080/slides.md#5
```

4) Review the page in a browser.

5) Capture a screenshot with Playwright (example):
```bash
node --input-type=module <<'EOF'
import { chromium } from 'playwright';

const url = 'http://localhost:8080/slides.md#5';
const out = '/tmp/slide-5.png';

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto(url, { waitUntil: 'domcontentloaded' });
await page.screenshot({ path: out, fullPage: true });
await browser.close();
EOF
```

## Playwright page navigation

If you cannot use the `#N` hash, send ArrowRight N-1 times:
- Page 1: no keypress
- Page 5: press ArrowRight 4 times

## Troubleshooting

- If the server fails to bind a port (EPERM), rerun with elevated permissions.
- If Playwright blocks `file://`, use server mode URLs.
- If assets 404, ensure you are in server mode and the deck is opened via `/slides.md`.
