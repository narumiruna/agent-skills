---
name: python-peewee
description: Use when working with Peewee ORM patterns, especially DatabaseProxy setup, scoped connection/transaction handling, and SQLite-based tests.
---

# Python Peewee

## Overview

Use Peewee with `DatabaseProxy`, scoped connection handling, explicit transactions, and isolated SQLite tests. Core principle: initialize the database at the boundary, then keep models and tests deterministic.

## Use When

- Defining Peewee models or a shared `BaseModel`.
- Wiring `DatabaseProxy` for app and test databases.
- Choosing `connection_context()` vs `atomic()`.
- Writing SQLite-backed fixtures for model tests.

## Quick Reference

| Need | Pattern |
| --- | --- |
| Deferred database binding | `DatabaseProxy()` |
| Model base class | `class BaseModel(Model)` with `Meta.database` |
| Scoped connection | `with db.connection_context():` |
| Transactional writes | `with db.atomic():` |
| SQLite tests | temporary `SqliteDatabase` fixture |

## Workflow

1. Define one `DatabaseProxy` and one `BaseModel` for the model graph.
2. Initialize the proxy once at the app/test boundary.
3. Use `connection_context()` to open and close connections for scoped work.
4. Use `atomic()` around write units that must commit or roll back together.
5. In tests, bind the proxy to an isolated SQLite database and create/drop tables inside the fixture.

## Setup

### DatabaseProxy & BaseModel

```python
from peewee import DatabaseProxy, Model

db_proxy = DatabaseProxy()

class BaseModel(Model):
    class Meta:
        database = db_proxy
```

### Initialize DB

```python
from peewee import SqliteDatabase

db = SqliteDatabase("app.db", pragmas={"foreign_keys": 1})
db_proxy.initialize(db)
```

## Connections and Transactions

### Read (no transaction)

```python
with db_proxy.obj.connection_context():
    rows = MyModel.select().limit(100)
```

### Write (atomic)

```python
with db_proxy.obj.atomic():
    a.save()
    b.save()
```

### Combined

```python
db = db_proxy.obj
with db.connection_context():
    with db.atomic():
        ...
```

Use `connection_context()` for scoped connections (open/close).
Use `atomic()` for atomic writes (BEGIN/COMMIT/ROLLBACK).

## SQLite Test Fixture

```python
import pytest
from peewee import SqliteDatabase

@pytest.fixture
def test_db(tmp_path):
    db = SqliteDatabase(str(tmp_path / "test.db"))
    db_proxy.initialize(db)
    with db.connection_context():
        db.create_tables([MyModel])
    yield db
    with db.connection_context():
        db.drop_tables([MyModel])
```

Use in function-based pytest tests:

```python
def test_create_user(test_db):
    with test_db.atomic():
        user = User.create(name="Ada")

    assert User.get_by_id(user.id).name == "Ada"
```

## Common Mistakes

- Querying models before `db_proxy.initialize(db)` has run.
- Holding one global open connection for the whole process when scoped connections would be clearer.
- Using `atomic()` as a substitute for opening a connection in code paths that also need explicit connection lifetime.
- Reusing a persistent app database in tests.

## Red Flags

- Tests that depend on table state from previous tests.
- Peewee models bound directly to a production database in module import code.
- Write operations performed without a transaction boundary.
