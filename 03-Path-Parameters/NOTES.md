# FastAPI Tutorial — Video 3: Path Parameters

## 1. What are Path Parameters?

A **path parameter** is a variable part of a URL.

Examples:

```text
/posts/1
/posts/2
/posts/10
```

Here, `1`, `2`, and `10` can represent the ID of a particular post.

In FastAPI:

```python
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    ...
```

The `{post_id}` in the URL must match the function parameter name.

---

## 2. Path Parameters with Type Hints

FastAPI uses Python type hints to validate path parameters.

```python
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    ...
```

For:

```text
/posts/1
```

FastAPI receives `post_id` as an integer.

For:

```text
/posts/abc
```

FastAPI rejects the request because `abc` is not an integer.

### Benefits of type hints

- Automatic validation
- Automatic data conversion
- Better editor support
- Automatic API documentation

---

## 3. Finding a Post by ID

Posts are stored as a list of dictionaries:

```python
posts: list[dict] = [
    {
        "id": 1,
        "author": "Alex",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]
```

Search for a post:

```python
for post in posts:
    if post["id"] == post_id:
        return post
```

The loop checks each post until the requested ID is found.

---

## 4. HTML Page for an Individual Post

```python
@app.get("/posts/{post_id}", include_in_schema=False, name="post_page")
def post_page(request: Request, post_id: int):
    for post in posts:
        if post["id"] == post_id:
            title = post["title"][:50]
            return templates.TemplateResponse(
                request,
                "post.html",
                {"post": post, "title": title}
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Post not found"
    )
```

### Important parts

| Part | Purpose |
|---|---|
| `/posts/{post_id}` | URL containing the path parameter |
| `post_id: int` | Receives and validates the ID |
| `request: Request` | Used for the template response |
| `post["id"] == post_id` | Finds the requested post |
| `TemplateResponse()` | Renders the HTML page |
| `HTTPException` | Handles a missing post |
| `404` | Resource was not found |

---

## 5. Jinja2 `url_for()` with Path Parameters

In the template:

```jinja2
{{ url_for('post_page', post_id=post.id) }}
```

For `post.id = 1`, this generates:

```text
/posts/1
```

For `post.id = 2`:

```text
/posts/2
```

### Route name must match

Python:

```python
@app.get(
    "/posts/{post_id}",
    include_in_schema=False,
    name="post_page"
)
```

Jinja2:

```jinja2
{{ url_for('post_page', post_id=post.id) }}
```

If the names do not match, Jinja2 can raise:

```text
No route exists for name "post_page"
```

---

## 6. Route Name vs Function Name

A route can have an explicit name:

```python
@app.get("/posts/{post_id}", name="post_page")
def post_page(...):
    ...
```

That name can be used by Jinja2:

```jinja2
{{ url_for('post_page', post_id=post.id) }}
```

Keep the route name and the name used in `url_for()` consistent.

---

## 7. HTTPException

FastAPI provides `HTTPException` for HTTP errors.

Import:

```python
from fastapi import HTTPException, status
```

Example:

```python
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Post not found"
)
```

This returns:

```text
HTTP 404 Not Found
```

The `detail` describes the error.

### Common status code

```python
status.HTTP_404_NOT_FOUND
```

means the requested resource was not found.

---

## 8. API Path Parameter

The same concept can be used for an API endpoint:

```python
@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Post not found"
    )
```

Example:

```text
GET /api/posts/1
```

returns the post with ID `1`.

---

## 9. HTML Route vs API Route

### HTML route

```python
@app.get("/posts/{post_id}")
def post_page(request: Request, post_id: int):
    ...
```

It renders an HTML template:

```python
templates.TemplateResponse(...)
```

### API route

```python
@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    ...
```

It returns Python data, which FastAPI serializes to JSON.

Example:

```json
{
    "id": 1,
    "author": "Alex",
    "title": "FastAPI is Awesome"
}
```

---

## 10. String Slicing

This:

```python
title = post["title"][:50]
```

takes at most the first 50 characters of the title.

This is standard Python string slicing.

---

## 11. `include_in_schema=False`

Example:

```python
@app.get("/posts/{post_id}", include_in_schema=False)
```

This prevents the route from appearing in FastAPI's automatically generated OpenAPI documentation.

It **does not disable the route**.

The route can still be accessed normally.

---

## 12. Static Files and Templates

Static files are mounted with:

```python
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)
```

Templates are configured with:

```python
templates = Jinja2Templates(directory="templates")
```

Typical structure:

```text
03-Path-Parameters/
│
├── main.py
├── templates/
│   ├── layout.html
│   ├── home.html
│   └── post.html
│
└── static/
    ├── css/
    ├── js/
    └── images/
```

Static files contain assets such as CSS, JavaScript, and images.

Templates contain HTML/Jinja2 files.

---

## 13. Import Error Encountered

An import error occurred with:

```python
from starlette.responses import HTTPexception as StarletteHTTPException
```

There were two issues:

1. The class name was incorrectly capitalized.
2. `HTTPException` is not imported from `starlette.responses`.

When Starlette's exception class is specifically needed:

```python
from starlette.exceptions import HTTPException as StarletteHTTPException
```

The normal FastAPI exception is:

```python
from fastapi import HTTPException
```

### Python is case-sensitive

These are different:

```text
HTTPException
HTTPexception
httpexception
```

Use the exact class name:

```python
HTTPException
```

---

## 14. Complete Request Flow

For:

```text
/posts/2
```

the flow is:

```text
Browser
   ↓
GET /posts/2
   ↓
FastAPI matches /posts/{post_id}
   ↓
post_id = 2
   ↓
Search posts list
   ↓
Find post where id == 2
   ↓
Render post.html
   ↓
Browser displays the post
```

For:

```text
/posts/99
```

when no post has ID `99`:

```text
Browser
   ↓
GET /posts/99
   ↓
post_id = 99
   ↓
Search posts
   ↓
No matching post
   ↓
HTTPException
   ↓
404 Not Found
```

---

## 15. Key Things to Remember

### Path parameter

```python
@app.get("/posts/{post_id}")
```

### Function parameter

```python
def get_post(post_id: int):
```

### Find matching data

```python
if post["id"] == post_id:
```

### Raise a 404

```python
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Post not found"
)
```

### Generate a dynamic Jinja2 URL

```jinja2
{{ url_for('post_page', post_id=post.id) }}
```

### Route name

```python
name="post_page"
```

must match:

```jinja2
url_for('post_page', ...)
```

---

## 16. Quick Revision

**What is a path parameter?**

A variable value included directly in the URL.

**Example:**

```text
/posts/5
```

where `5` is the `post_id`.

**How is it declared?**

```python
@app.get("/posts/{post_id}")
def get_post(post_id: int):
```

**How do we find the requested post?**

```python
if post["id"] == post_id:
```

**How do we return a 404?**

```python
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Post not found"
)
```

**How do we generate the URL in Jinja2?**

```jinja2
{{ url_for('post_page', post_id=post.id) }}
```

**What caused the `url_for()` error?**

The route name and the name supplied to `url_for()` did not match.

**What caused the `HTTPexception` import error?**

Incorrect capitalization and incorrect import location.

---

## 17. Main Learning Outcome

After Video 3, you should understand how to:

- Create dynamic URLs using path parameters.
- Receive and validate path parameters with FastAPI.
- Find a resource using its ID.
- Render a specific HTML page using Jinja2.
- Generate dynamic links using `url_for()`.
- Handle missing resources with `HTTPException`.
- Return a specific resource from an API endpoint.
- Understand HTML routes vs API routes.
- Use `include_in_schema=False`.
- Debug route-name and import errors.
