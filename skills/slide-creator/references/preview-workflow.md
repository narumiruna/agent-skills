# Marp Server Preview + Playwright Review

Use this workflow to preview Marp slides in server mode and review specific pages with Playwright.

## Preconditions

- `marp` CLI installed
- Playwright installed with a Chromium browser

## Workflow

1) Start Marp server mode from the slide directory:
```bash
marp -s examples/slides/marketplace/
```

2) Open the rendered deck in a browser:
```
http://localhost:8080/slides.md
```

3) Use Playwright to review a specific page:
- Navigate to the URL
- Use ArrowRight to reach the target page
- Capture a screenshot

## Troubleshooting

- If the server fails to bind a port (EPERM), rerun with elevated permissions.
- If Playwright blocks `file://`, use server mode URLs.
- If assets 404, ensure you are in server mode and the deck is opened via `/slides.md`.
