# Logging with Python stdlib

Use stdlib logging for libraries, services, and applications that need standard ecosystem integration. Library modules should create loggers but leave handler and level configuration to the application entry point.

## Basic Configuration

```python
import logging

format_str = "%(asctime)s | %(levelname)s | %(name)s:%(lineno)d - %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=format_str,
)

logger = logging.getLogger(__name__)
logger.info("Application started")
```

## Library Pattern

```python
import logging

logger = logging.getLogger(__name__)


def load_user(user_id: int) -> None:
    logger.info("Loading user", extra={"user_id": user_id})
```

Do not call `logging.basicConfig()` or attach process-wide handlers inside reusable library modules.

## Loggers and Handlers

```python
import logging
import sys

logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler(sys.stderr)
console_handler.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("logs/app.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(format_str)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

Configure handlers once at process startup. If setup code can run more than once, guard against duplicate handlers or centralize setup in a single entry point.

## Structured Context

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s:%(lineno)d | %(user_id)s | %(message)s",
)

logger = logging.getLogger(__name__)
logger.info("User action", extra={"user_id": 123})
```

## Exceptions

```python
import logging

logger = logging.getLogger(__name__)

try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Computation failed")
```
