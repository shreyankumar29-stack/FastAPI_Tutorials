# FastAPI Tutorial — Video 3: Path Parameters

This folder contains the code and notes for **Video 3** of the FastAPI tutorial, focused on **Path Parameters**.

## 📚 Topics Covered

- Path parameters in FastAPI
- Type hints and automatic validation
- Dynamic post URLs
- Retrieving a post using its ID
- Jinja2 `url_for()` with path parameters
- Named FastAPI routes
- Rendering an individual post page
- `HTTPException`
- HTTP 404 Not Found
- API endpoints with path parameters
- HTML routes vs API routes
- `include_in_schema=False`
- Static files and templates
- Debugging route-name and import errors

## 📁 Project Structure

```text
03-Path-Parameters/
│
├── main.py
│
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

## 🚀 Setup

The project uses the shared virtual environment from the parent `FastAPI_Tutorials` directory.

From this folder:

```powershell
..\.venv\Scripts\activate
```

If FastAPI is not installed in the environment:

```powershell
pip install "fastapi[standard]"
```

## ▶️ Run the Application

Start the development server:

```powershell
fastapi dev main.py
```

FastAPI will provide the local application URL in the terminal.

## 🌐 Important Routes

### Home

```text
/
```

### Posts

```text
/posts
```

### Individual Post

```text
/posts/{post_id}
```

Examples:

```text
/posts/1
/posts/2
```

### Posts API

```text
/api/posts
```

### Individual Post API

```text
/api/posts/{post_id}
```

Examples:

```text
/api/posts/1
/api/posts/2
```

## 🔑 Path Parameter Example

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

Here:

- `{post_id}` is the path parameter.
- `post_id: int` tells FastAPI to expect an integer.
- FastAPI performs validation automatically.
- A missing post results in a `404 Not Found`.

## 🔗 Jinja2 Dynamic URLs

The individual post link can be generated in the template:

```jinja2
{{ url_for('post_page', post_id=post.id) }}
```

The route must have the corresponding name:

```python
@app.get(
    "/posts/{post_id}",
    include_in_schema=False,
    name="post_page"
)
```

The route name and the name used in `url_for()` must match.

## ❌ Error Handling

For a post that does not exist:

```python
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Post not found"
)
```

This returns an HTTP 404 response instead of allowing the application to continue without a result.

## 📝 Documentation

- [`NOTES.md`](NOTES.md) — Detailed concepts, explanations, examples, and troubleshooting.
- [`COMMANDS.md`](COMMANDS.md) — Commands used while working on this tutorial.

## 🎯 Learning Outcome

After completing this video, you should be able to:

1. Create dynamic FastAPI URLs.
2. Define and use path parameters.
3. Validate path parameters using type hints.
4. Find a resource by its ID.
5. Render an individual HTML page.
6. Generate dynamic URLs with Jinja2 `url_for()`.
7. Handle missing resources with `HTTPException`.
8. Create API endpoints containing path parameters.
9. Debug route-name and import errors.

## 🛠️ Technologies

- Python
- FastAPI
- Jinja2
- Starlette
- HTML/CSS
