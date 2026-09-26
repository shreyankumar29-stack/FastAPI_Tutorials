# FastAPI Tutorial — Video 7: Sync to Async

## Overview

Video 7 focuses on converting the database layer from synchronous SQLAlchemy usage to asynchronous SQLAlchemy usage.

### Topics Covered

- Async SQLAlchemy
- `AsyncSession`
- `async_sessionmaker`
- `create_async_engine`
- `aiosqlite`
- `async def`
- `async with`
- `await`
- Async database dependencies
- Async CRUD operations
- Sync vs Async SQLAlchemy

## Async Database URL

For SQLite with `aiosqlite`:

```python
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"
```

Make sure it is `sqlite`, not `sqlit`.

Install the async SQLite driver:

```powershell
pip install aiosqlite
```

## Async Engine

```python
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
```

## Async Session

```python
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
```

## Async Database Dependency

```python
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

`async def` is required because the function uses `async with`.

## Complete `database.py`

```python
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"


engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)


AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

## Why `async def`?

Incorrect:

```python
def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

Correct:

```python
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

`async with` can only be used inside an asynchronous function.

## Async Queries

With SQLAlchemy's async execution style:

```python
from sqlalchemy import select

result = await db.execute(select(User))
users = result.scalars().all()
```

## Async Create

```python
db.add(user)
await db.commit()
await db.refresh(user)
```

## Async Update

```python
user.username = user_update.username
await db.commit()
await db.refresh(user)
```

## Async Delete

```python
db.delete(user)
await db.commit()
```

## Sync vs Async

| Synchronous | Asynchronous |
|---|---|
| `Session` | `AsyncSession` |
| `create_engine()` | `create_async_engine()` |
| `sessionmaker()` | `async_sessionmaker()` |
| `def` | `async def` |
| normal context manager | `async with` |
| direct DB I/O | `await` DB I/O |
| normal SQLite driver | `aiosqlite` |

## Common Error: Wrong Database URL

Incorrect:

```python
SQLALCHEMY_DATABASE_URL = "sqlit+aiosqlite:///./blog.db"
```

Correct:

```python
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"
```

The missing `e` in `sqlite` causes SQLAlchemy to fail while loading the database dialect/driver.

## Main Learning Outcome

After Video 7, you should understand:

- Why asynchronous database operations are useful.
- How to create an async SQLAlchemy engine.
- How `AsyncSession` works.
- How to create an async database dependency.
- Why `async def` is required with `async with`.
- Why `aiosqlite` is needed for async SQLite.
- How CRUD operations change when using `AsyncSession`.
- The difference between synchronous and asynchronous SQLAlchemy.
