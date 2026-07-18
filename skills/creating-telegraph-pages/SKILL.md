---
name: creating-telegraph-pages
description: Create and publish public Telegra.ph articles through the official Telegraph API, including account setup, content conversion to Telegraph nodes, credential handling, and publication verification. Use when the user asks to create, publish, or post a page or article on telegra.ph.
---

# Creating Telegraph Pages

Publish structured articles with the bundled `scripts/telegraph.py` helper. Treat page creation as an external write: verify the final title, author details, and content before publishing unless the user's request already makes them explicit.

## Workflow

1. Prepare the article.
   - Preserve the user's wording and language unless editing was requested.
   - Confirm ambiguous title, byline, links, or publication intent before the external write.
   - Do not publish secrets, private data, or local-only asset paths.

2. Convert the body to a JSON array of Telegraph nodes in a temporary file. Use strings for text and objects shaped as `{"tag": "p", "children": ["Text"]}` for elements.
   - Use only `a`, `aside`, `b`, `blockquote`, `br`, `code`, `em`, `figcaption`, `figure`, `h3`, `h4`, `hr`, `i`, `iframe`, `img`, `li`, `ol`, `p`, `pre`, `s`, `strong`, `u`, `ul`, or `video`.
   - Use only `href` and `src` attributes.
   - Keep the encoded content at or below 64 KB.
   - Convert Markdown headings to `h3` or `h4`; Telegraph does not support `h1` or `h2` nodes.

3. Obtain an access token.
   - Prefer an existing token supplied through `TELEGRAPH_ACCESS_TOKEN`.
   - Never place the token in a command argument, committed file, log, or response.
   - If the user has no account, ask before creating one because it changes external state. Run:

     ```shell
     uv run python scripts/telegraph.py create-account --short-name '<account-name>'
     ```

   - Treat the returned `access_token` as a secret and ask the user to store it securely. Do not create repeated accounts to avoid managing a token.

4. Publish only after the content is ready:

   ```shell
   uv run python scripts/telegraph.py create-page \
     --title '<title>' \
     --author-name '<author>' \
     /tmp/telegraph-content.json
   ```

   Omit `--author-name` or add `--author-url` when appropriate. Inject `TELEGRAPH_ACCESS_TOKEN` through the execution environment; do not write the literal token into shell history.

5. Verify the result.
   - Check that the command returned an `https://telegra.ph/...` URL.
   - Open or fetch the public page when tools permit and verify the title, byline, links, and content structure.
   - Report the published URL and any verification limitation.
   - Remove temporary content files after successful publication when they contain sensitive drafts.

## Failure Handling

- Preserve API errors exactly enough to diagnose them, but never echo the token.
- On `ACCESS_TOKEN_INVALID`, stop and request a valid token; do not create a replacement account automatically.
- On content validation errors, fix the unsupported node or attribute before retrying.
- Do not repeatedly retry ambiguous or rate-related API errors; report the failure and retain the prepared content for a later attempt.

Use the [official Telegraph API documentation](https://telegra.ph/api) for methods or fields not covered by the helper.
