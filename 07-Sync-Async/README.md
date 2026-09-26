# FastAPI Tutorial — Video 7: Sync to Async

This folder contains the code and documentation for **Video 7**, where the FastAPI database layer is converted from synchronous SQLAlchemy to asynchronous SQLAlchemy.

## Topics Covered

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

## Project Structure

```text
07-Sync-Async/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── templates/
└── static/
```

## Async Database Flow

```text
Client
   ↓
FastAPI
   ↓
Async Dependency
   ↓
AsyncSession
   ↓
Async SQLAlchemy
   ↓
SQLite / aiosqlite
```

## Database URL

```python
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"
```

`sqlite+aiosqlite` is correct. `sqlit+aiosqlite` is incorrect.

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

## Complete Database Setup

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

## Install Async SQLite Driver

```powershell
pip install aiosqlite
```

## Async Query Example

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

## Common Error

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

## Learning Outcome

After Video 7, you should be able to:

1. Understand async SQLAlchemy.
2. Use `AsyncSession`.
3. Use `async_sessionmaker`.
4. Create an async engine.
5. Use `aiosqlite`.
6. Understand `async def` and `async with`.
7. Use `await` for async database operations.
8. Build an async database dependency.
9. Convert CRUD database operations to async.
10. Understand sync vs async SQLAlchemy.

## Technologies

- Python
- FastAPI
- SQLAlchemy
- aiosqlite
- Pydantic
