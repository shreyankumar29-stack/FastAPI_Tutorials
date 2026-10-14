# Part 9 – Frontend Forms Notes

## 1. What is an HTML Form?

An HTML `<form>` collects information from the user and sends it to the backend.

Example:

```html
<form method="post" action="/login">
    <input type="text" name="username">
    <input type="password" name="password">
    <button type="submit">Login</button>
</form>
```

Important attributes:

- `method` → HTTP method used to submit the form
- `action` → URL receiving the form data
- `name` → identifies each submitted field

---

## 2. GET vs POST

### GET

```html
<form method="get" action="/search">
```

Data is generally sent as query parameters.

Example:

```text
/search?query=fastapi
```

### POST

```html
<form method="post" action="/login">
```

Data is sent in the request body.

POST is commonly used for submitting or creating data.

---

## 3. FastAPI Form()

FastAPI uses `Form()` to receive HTML form fields.

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

The parameter names must correspond to the HTML input `name` attributes.

For example:

```html
<input name="username">
```

matches:

```python
username: str = Form(...)
```

---

## 4. Install python-multipart

Form parsing requires the multipart package.

```powershell
pip install python-multipart
```

If it is missing, FastAPI can report an error indicating that `python-multipart` is required.

---

## 5. Forms with Jinja2

A form can be placed inside a Jinja2 template.

Example:

```html
{% extends "layout.html" %}

{% block content %}

<form method="post" action="/login">
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <button type="submit">Login</button>
</form>

{% endblock %}
```

The template is rendered using `Jinja2Templates`.

---

## 6. GET Route for the Form Page

```python
@app.get("/login", include_in_schema=False)
def login_page(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html"
    )
```

This displays the form.

---

## 7. POST Route for Form Submission

```python
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

The browser sends the submitted form fields to this endpoint.

---

## 8. Form Flow

The overall flow is:

```text
Browser
   ↓
GET /login
   ↓
FastAPI renders login.html
   ↓
User fills the form
   ↓
POST /login
   ↓
FastAPI receives Form(...)
   ↓
Backend processes the data
   ↓
Response / redirect
```

---

## 9. Redirect After Submission

FastAPI can redirect the user after processing a form.

```python
from fastapi.responses import RedirectResponse

return RedirectResponse(
    url="/",
    status_code=303
)
```

A `303 See Other` response is commonly used after a successful POST when redirecting to another page.

---

## 10. Important Difference: JSON vs Form Data

JSON request:

```python
@app.post("/posts")
def create_post(post: PostCreate):
    ...
```

HTML form:

```python
@app.post("/login")
def login(username: str = Form(...)):
    ...
```

They are different request formats and should be handled accordingly.

---

## Common Mistakes

### Missing `Form`

Incorrect:

```python
async def login(username: str):
```

For an HTML form field, use:

```python
async def login(username: str = Form(...)):
```

### Missing `python-multipart`

Install:

```powershell
pip install python-multipart
```

### Mismatched field names

HTML:

```html
<input name="username">
```

FastAPI:

```python
username: str = Form(...)
```

The names should match.

### Wrong action URL

If the form has:

```html
<form method="post" action="/login">
```

there must be a matching POST route:

```python
@app.post("/login")
```

---

## Key Takeaways

- HTML forms send user-entered data to the backend.
- `Form()` receives form fields in FastAPI.
- `python-multipart` is required for form parsing.
- The HTML `name` must match the FastAPI parameter.
- Jinja2 templates can display the form.
- GET can display the form page.
- POST can process submitted data.
- `RedirectResponse` can redirect after successful submission.
