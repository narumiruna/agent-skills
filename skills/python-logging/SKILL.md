---
name: python-logging
description: Use when choosing or configuring Python logging, especially deciding between stdlib logging and loguru for apps or CLIs.
---

# Python Logging

## Overview

Choose the logging system based on project boundaries. Core principle: use stdlib logging for reusable libraries and ecosystem integration; use loguru only when an app or CLI owns the whole logging surface.

## Use When

- Choosing between stdlib `logging` and `loguru`.
- Configuring log levels, handlers, formatters, or structured context.
- Adding logging to libraries, apps, CLIs, or services.
- Deciding how logging should interact with ops tooling.

## Quick Reference

| Need | Use |
| --- | --- |
| Library or long-lived service | stdlib `logging` |
| Simple app or CLI | `loguru` |
| Integrations (Sentry/OTel) | stdlib `logging` |
| Mixed library + app | stdlib in library; app config at boundary |

## Decision Rules

Use stdlib `logging` when:
- Building a reusable library
- You need handler hierarchies or integration with ops tooling
- You expect callers to configure logging

Use `loguru` when:
- You want minimal setup and readable output
- You are building a small app or CLI
- You control process startup and logging configuration

## Workflow

1. Decide whether the code is a library, service, CLI, or one-off app.
2. Keep libraries passive: create `logging.getLogger(__name__)` and do not call `basicConfig()`.
3. Configure handlers and levels once at the application entry point.
4. Avoid mixing stdlib logging and loguru unless the app owns the bridge and boundary.

## Example

Stdlib logger setup:
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("App started")
```

## Common Mistakes

- Forcing loguru in a reusable library.
- Mixing two logging systems without a clear boundary.
- Calling `basicConfig()` inside imported library modules.
- Creating handlers repeatedly in functions that run more than once.

## Red Flags

- Logging recommendations with no rationale for library vs app use.
- Global logging setup hidden in modules that are imported by tests or other applications.

## References

- `references/logging.md` - stdlib logging patterns
- `references/loguru.md` - loguru patterns
