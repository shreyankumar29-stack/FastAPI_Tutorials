# FastAPI Tutorial — Video 5: Database

This folder contains the code and documentation for **Video 5**, focused on connecting the FastAPI application to a database using **SQLAlchemy**.

## Topics Covered

- SQLAlchemy
- ORM
- Database engine
- Declarative Base
- Database sessions
- FastAPI database dependencies
- SQLAlchemy models
- `Mapped`
- `mapped_column`
- Foreign keys
- Relationships
- Pydantic schemas with database models
- `from_attributes=True`
- Debugging database/import errors

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

### File Responsibilities

| File | Purpose |
|---|---|
| `main.py` | FastAPI application and routes |
| `database.py` | Database connection and session setup |
| `models.py` | SQLAlchemy models |
| `schemas.py` | Pydantic request/response schemas |

## Setup

The project uses the shared virtual environment in the parent `FastAPI_Tutorials` folder.

```powershell
..\.venv\Scripts\activate
```

If needed:

```powershell
pip install "fastapi[standard]"
pip install sqlalchemy
```

## Run the Application

```powershell
fastapi dev main.py
```

## Useful URLs

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Database Architecture

```text
Client
   ↓
FastAPI
   ↓
Pydantic Schema
   ↓
SQLAlchemy Model
   ↓
Database
```

Pydantic handles API data validation and serialization, while SQLAlchemy handles database interaction.

## SQLAlchemy Concepts

Modern SQLAlchemy models can use:

```python
from sqlalchemy.orm import Mapped, mapped_column, relationship
```

Example:

```python
id: Mapped[int] = mapped_column(primary_key=True)
```

Foreign keys connect related tables, while `relationship()` defines object-level relationships.

## Pydantic Response Models

A response schema can use:

```python
model_config = ConfigDict(from_attributes=True)
```

This is useful when returning SQLAlchemy ORM objects.

## Error Encountered

The application initially failed with:

```text
SyntaxError: from __future__ imports must occur at the beginning of the file
```

The issue was in `database.py`.

This:

```python
from __future__ import annotations
```

must appear before normal imports and executable code.

Correct:

```python
from __future__ import annotations

from sqlalchemy import create_engine
```

Alternatively, remove the future import if it is not needed.

## Learning Outcome

After completing this part, you should be able to:

1. Understand SQLAlchemy's role in FastAPI.
2. Understand database sessions.
3. Create SQLAlchemy models.
4. Use `Mapped` and `mapped_column`.
5. Understand foreign keys and relationships.
6. Separate SQLAlchemy models from Pydantic schemas.
7. Understand `from_attributes=True`.
8. Follow the basic FastAPI database dependency pattern.
9. Debug import and syntax errors.

## Technologies

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Jinja2
- Starlette
