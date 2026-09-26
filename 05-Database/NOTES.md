# FastAPI Tutorial — Video 5: Database

## Overview
This part introduces database integration into the FastAPI application using SQLAlchemy.

### Topics
- SQLAlchemy and ORM
- Database engine
- Declarative Base
- Database sessions
- FastAPI database dependency
- SQLAlchemy models
- `Mapped`
- `mapped_column`
- `ForeignKey`
- Relationships
- Pydantic schemas with database models
- `ConfigDict(from_attributes=True)`
- Debugging import and syntax errors

## Project Structure

```text
05-Database/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── templates/
└── static/
```

| File | Purpose |
|---|---|
| `main.py` | FastAPI application and routes |
| `database.py` | Database engine, Base, session/dependency setup |
| `models.py` | SQLAlchemy database models |
| `schemas.py` | Pydantic request/response schemas |

## SQLAlchemy

SQLAlchemy is a Python SQL toolkit and ORM. An ORM allows Python classes to represent database tables.

```text
Python Class → SQLAlchemy ORM → Database Table
```

## Declarative Base

SQLAlchemy models inherit from a common base:

```python
class Base(DeclarativeBase):
    pass
```

Then in `models.py`:

```python
from database import Base
```

and models inherit from `Base`.

## Database Session

A SQLAlchemy `Session` is used for database operations such as querying, adding, updating, deleting, and committing records.

```python
from sqlalchemy.orm import Session
```

FastAPI can provide a session to an endpoint through a dependency.

## SQLAlchemy Models

Modern SQLAlchemy uses:

```python
from sqlalchemy.orm import Mapped, mapped_column, relationship
```

Example:

```python
id: Mapped[int] = mapped_column(primary_key=True)
```

### `Mapped`
Represents a SQLAlchemy-mapped Python attribute.

### `mapped_column()`
Configures a database column.

### `ForeignKey`
Connects a column to another table:

```python
ForeignKey("users.id")
```

### `relationship()`
Defines relationships between SQLAlchemy models.

## Pydantic vs SQLAlchemy

### SQLAlchemy model
Represents database data:

```text
Database ↔ SQLAlchemy Model
```

### Pydantic schema
Represents API input/output:

```text
Client ↔ Pydantic Schema
```

Overall:

```text
Client
  ↓
Pydantic Schema
  ↓
FastAPI
  ↓
SQLAlchemy Model
  ↓
Database
```

## `from_attributes=True`

The response schema can contain:

```python
model_config = ConfigDict(from_attributes=True)
```

This allows Pydantic to read values from object attributes, which is useful for SQLAlchemy/ORM objects.

## Error Encountered

The application failed during startup with:

```text
SyntaxError: from __future__ imports must occur at the beginning of the file
```

The traceback led through:

```text
main.py
  ↓
import models
  ↓
models.py
  ↓
from database import Base
  ↓
database.py
  ↓
SyntaxError
```

The problem was:

```python
from __future__ import annotations
```

appearing around line 25 of `database.py`.

### Correct placement

```python
from __future__ import annotations

from sqlalchemy import create_engine
```

A `from __future__` import must be at the beginning of the file, before normal imports and executable code.

If it is not required, it can also be removed.

## Debugging Lesson

When reading a traceback:

1. Find the file and line shown near the bottom.
2. Look at the final exception.
3. Trace the import chain backward.
4. Fix the actual source error rather than the first file mentioned.

## Quick Revision

**SQLAlchemy:** Python SQL toolkit and ORM.

**Session:** Used to communicate with the database.

**Base:** Parent class for SQLAlchemy models.

**Mapped:** SQLAlchemy type annotation for mapped attributes.

**mapped_column():** Defines/configures a database column.

**ForeignKey:** Connects related database tables.

**relationship():** Defines model relationships.

**Pydantic:** Handles API validation/serialization.

**`from_attributes=True`:** Allows Pydantic to read ORM object attributes.

## Main Learning Outcome

After this part, you should understand:
- The role of SQLAlchemy in FastAPI.
- Database engines and sessions.
- SQLAlchemy declarative models.
- `Mapped` and `mapped_column`.
- Foreign keys and relationships.
- The difference between database models and Pydantic schemas.
- Basic FastAPI database dependency usage.
- How to debug Python import and syntax errors.
