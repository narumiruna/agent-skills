# Logging with Loguru

## Installation

```bash
uv add loguru
```

## Basic Usage

```python
from loguru import logger

# Simple logging
logger.info("Application started")
logger.debug("Processing item {item_id}", item_id=42)
logger.warning("Low disk space: {free} MB", free=512)
err = "Connection refused"
logger.error("Failed to connect: {error}", error=err)
```

## Configure Output

```python
from loguru import logger
import sys

# Remove default handler
logger.remove()

# Add custom handler with format
logger.add(
    sys.stderr,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
    level="INFO"
)

# Add file handler with rotation
logger.add(
    "logs/app.log",
    rotation="500 MB",
    retention="10 days",
    level="DEBUG"
)
```

## Exception Logging

```python
from loguru import logger

@logger.catch
def risky_function(x: int) -> float:
    """Automatically log exceptions with full traceback."""
    return 1 / x  # Will log if x is 0
```

## Structured Logging

```python
from loguru import logger

logger.info(
    "User action",
    user_id=123,
    action="login",
    ip_address="192.168.1.1"
)
```
