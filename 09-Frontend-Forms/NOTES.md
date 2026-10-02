# Part 8 – Routers Notes

## 1. What is APIRouter?

`APIRouter` is used to group related FastAPI path operations.

Instead of putting every endpoint inside `main.py`, routes can be separated into different files.

```python
from fastapi import APIRouter

router = APIRouter()
```

---

## 2. Creating Routes

```python
@router.get("/posts")
def get_posts():
    return {"message": "Get posts"}
```

Another route:

```python
@router.post("/posts")
def create_post():
    return {"message": "Create post"}
```

---

## 3. Registering a Router

The router must be included in the main FastAPI application.

```python
from fastapi import FastAPI
from routers import posts

app = FastAPI()

app.include_router(posts.router)
```

If a router is not included, FastAPI will not register its routes.

---

## 4. Router Prefix

A prefix can be added when registering a router.

```python
app.include_router(
    posts.router,
    prefix="/api"
)
```

A route:

```python
@router.get("/posts")
```

will then be available at:

```text
/api/posts
```

---

## 5. Router Tags

Tags organize endpoints in Swagger/OpenAPI.

```python
app.include_router(
    posts.router,
    prefix="/api",
    tags=["Posts"]
)
```

Swagger will group these endpoints under the `Posts` tag.

---

## 6. Separate Routers

A larger application can have different routers.

```text
routers/
├── posts.py
├── users.py
└── auth.py
```

Example `users.py`:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {"message": "All users"}
```

Then:

```python
from routers import posts, users

app.include_router(posts.router)
app.include_router(users.router)
```

---

## 7. Why Routers?

Without routers:

```text
main.py
└── hundreds of endpoints
```

With routers:

```text
main.py
routers/
├── posts.py
├── users.py
└── auth.py
```

This makes the project easier to maintain.

---

## 8. Router Dependencies

Routers can also have shared dependencies.

```python
router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)
```

This avoids repeating the same configuration on every route.

---

## 9. Important Concept

`APIRouter` does **not** create a second FastAPI application.

It creates a group of routes that are later included in the main `FastAPI()` application.

---

## Common Mistakes

### Forgetting the import

```python
from fastapi import APIRouter
```

### Forgetting to include the router

```python
app.include_router(posts.router)
```

### Wrong router variable

If the router file contains:

```python
router = APIRouter()
```

then use:

```python
app.include_router(posts.router)
```

---

## Key Takeaways

- `APIRouter()` groups related endpoints.
- Routes can be moved out of `main.py`.
- `include_router()` registers them with the application.
- `prefix` adds a common URL prefix.
- `tags` organizes Swagger documentation.
- Routers improve project structure and maintainability.
