# FastAPI Tutorial – Part 9: Frontend Forms

This part focuses on receiving data from **HTML forms** in FastAPI and connecting frontend templates with backend routes.

## Topics Covered

- HTML forms
- GET and POST form submission
- FastAPI `Form()`
- `python-multipart`
- Jinja2 templates
- Receiving form fields
- Redirecting after form submission
- Connecting frontend and backend

## Example HTML Form

```html
<form method="post" action="/login">
    <input type="text" name="username">
    <input type="password" name="password">
    <button type="submit">Login</button>
</form>
```

## FastAPI Route

```python
from fastapi import Form

@app.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...)
):
    return {
        "username": username,
        "password": password
    }
```

## Required Package

HTML form handling requires multipart support:

```powershell
pip install python-multipart
```

## Run

```powershell
..\.venv\Scripts\activate
fastapi dev main.py
```

> This documentation is organized for your FastAPI tutorial workflow and focuses specifically on Frontend Forms.
