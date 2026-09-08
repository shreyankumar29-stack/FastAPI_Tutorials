# FastAPI Tutorial Notes

# Video 2 --- HTML Frontend

**Status:** Completed

## 1. Request

FastAPI's `Request` object can be used when the endpoint needs
information about the incoming HTTP request.

Import:

``` python
from fastapi import Request
```

Example:

``` python
def home(request: Request):
    ...
```

The request is also passed to the template response.

------------------------------------------------------------------------

## 2. Jinja2Templates

Jinja2 is a template engine that allows HTML pages to contain dynamic
data.

Import:

``` python
from fastapi.templating import Jinja2Templates
```

Create the template configuration:

``` python
templates = Jinja2Templates(directory="templates")
```

The `directory` points to the folder containing the HTML templates.

Project example:

``` text
02-HTML-FRONTEND/
└── templates/
    ├── home.html
    └── layout.html
```

------------------------------------------------------------------------

## 3. TemplateResponse

A template can be returned from a FastAPI route using:

``` python
return templates.TemplateResponse(
    request,
    "home.html",
    {"posts": posts, "title": "Home"}
)
```

The three important pieces are:

1.  The request
2.  The template filename
3.  The context/data passed to the template

------------------------------------------------------------------------

## 4. Passing Data to HTML

Python data can be passed to the template through a dictionary.

Example:

``` python
{"posts": posts, "title": "Home"}
```

The template can then use the variables:

``` text
posts
title
```

This allows Python to provide dynamic content to an HTML page.

------------------------------------------------------------------------

## 5. Posts Data

The tutorial uses a list of dictionaries:

``` python
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

This data can be sent to the HTML template as:

``` python
{"posts": posts, "title": "Home"}
```

------------------------------------------------------------------------

## 6. Template Inheritance

The project uses:

``` text
layout.html
home.html
```

`home.html` extends the common layout.

Example:

``` jinja2
{% extends "layout.html" %}
```

This allows common page elements to remain in `layout.html` instead of
being repeated in every page.

------------------------------------------------------------------------

## 7. Jinja2 Dynamic Content

Jinja2 uses template expressions to display Python data.

Example:

``` jinja2
{{ title }}
```

The value comes from the context dictionary passed by Python.

Jinja2 also supports control structures such as loops.

------------------------------------------------------------------------

## 8. `url_for()`

Templates can generate URLs using:

``` jinja2
{{ url_for("home") }}
```

The name passed to `url_for()` must match an existing route name.

Example:

``` python
@app.get("/")
def home(request: Request):
    ...
```

The route name is `home`.

Therefore:

``` jinja2
{{ url_for("home") }}
```

can resolve the URL.

------------------------------------------------------------------------

## 9. Route Names Are Case-Sensitive

I encountered this error:

``` text
No route exists for name "home" and params "".
```

The template requested:

``` jinja2
url_for("home")
```

but the Python function was:

``` python
def Home(request: Request):
```

`Home` and `home` are different names.

Correct:

``` python
def home(request: Request):
```

------------------------------------------------------------------------

## 10. Multiple Decorators on One Function

The project uses:

``` python
@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    ...
```

This allows more than one URL to use the same function.

Conceptually:

``` text
/       ──┐
          ├──→ home()
/posts ──┘
```

------------------------------------------------------------------------

## 11. `include_in_schema=False`

The route definitions contain:

``` python
include_in_schema=False
```

This prevents those routes from appearing in the automatically generated
OpenAPI schema/documentation.

The route can still be accessed normally.

------------------------------------------------------------------------

## 12. Development Server

The application is started with:

``` powershell
fastapi dev main.py
```

FastAPI starts the development server and automatically reloads when
code changes.

------------------------------------------------------------------------

## 13. Important Error

The error:

``` text
HTTP 500
```

does not necessarily mean FastAPI itself is incorrectly installed.

In this case, the server started successfully, but the template
rendering failed because `url_for("home")` could not find a route with
that name.

------------------------------------------------------------------------

## 14. Debugging Method

When an error occurs:

1.  Look at the HTTP status.
2.  Read the traceback.
3.  Find the file mentioned near the bottom.
4.  Find the exact line causing the exception.
5.  Understand what the error message means.
6.  Compare names carefully, including capitalization.
7.  Fix the smallest required part.
8.  Reload the page and test again.

------------------------------------------------------------------------

## 15. Key Takeaways

``` text
FastAPI
   ↓
Request
   ↓
Jinja2Templates
   ↓
TemplateResponse
   ↓
HTML Template
   ↓
Dynamic Data
```

Important concepts from this part:

-   `Request`
-   `Jinja2Templates`
-   `TemplateResponse`
-   Jinja2 variables
-   Template inheritance
-   `url_for()`
-   Route names
-   Multiple route decorators
-   `include_in_schema=False`
-   Debugging template errors

**Video 2 completed.**
