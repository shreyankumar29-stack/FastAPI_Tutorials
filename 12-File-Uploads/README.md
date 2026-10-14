# FastAPI Tutorial – Part 8: Routers

This part focuses on organizing a FastAPI application using **APIRouter**.

## Topics Covered

- What is `APIRouter`?
- Why use routers?
- Creating separate router files
- Registering routers with `app.include_router()`
- Router prefixes
- Router tags
- Organizing API endpoints
- Keeping `main.py` clean

## Typical Structure

```text
project/
├── main.py
├── routers/
│   ├── __init__.py
│   ├── posts.py
│   └── users.py
├── templates/
├── static/
└── database.py
```

## Basic Router

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/posts")
def get_posts():
    return {"message": "All posts"}
```

Register it in `main.py`:

```python
from fastapi import FastAPI
from routers import posts

app = FastAPI()

app.include_router(posts.router)
```

## Run

```powershell
..\.venv\Scripts\activate
fastapi dev main.py
```

> This documentation is organized for your FastAPI tutorial workflow and focuses specifically on Routers.
