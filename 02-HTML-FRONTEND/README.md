# FastAPI Tutorial --- Video 2: HTML Frontend

This folder contains my implementation and documentation for **Video 2**
of the FastAPI tutorial series by **Corey Schafer**.

I am following Corey's FastAPI tutorial while using **Python `venv` +
`pip` instead of `uv`**.

## Learning Source

-   **Instructor:** Corey Schafer
-   **Framework:** FastAPI
-   **Language:** Python
-   **Template Engine:** Jinja2
-   **Environment:** Python `venv` + `pip`

## What I Learned

In this part, I learned how to use FastAPI with an HTML frontend and
Jinja2 templates.

Main concepts practiced:

-   `Request` objects
-   `Jinja2Templates`
-   Template directories
-   Rendering HTML templates
-   Passing data from Python to templates
-   Jinja2 template inheritance
-   `layout.html`
-   `home.html`
-   Dynamic post data
-   `url_for()` in templates
-   Multiple routes for the same endpoint function
-   `include_in_schema=False`
-   Debugging template and route-name errors

## Project Structure

``` text
02-HTML-FRONTEND/
│
├── templates/
│   ├── home.html
│   └── layout.html
│
├── home_finished.html
├── layout_finished.html
├── main.py
└── snippets.txt
```

The structure will change as more FastAPI concepts are introduced.

## Basic FastAPI + Jinja2 Setup

``` python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
```

`Jinja2Templates` tells FastAPI/Starlette where the HTML templates are
located.

## Rendering a Template

``` python
@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"}
    )
```

The request object is passed to the template response, together with the
template name and context data.

## Running the Application

From the `02-HTML-FRONTEND` directory:

``` powershell
fastapi dev main.py
```

The application is available at:

``` text
http://127.0.0.1:8000
```

## Documentation

FastAPI automatically provides:

``` text
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

## Debugging Experience

During this part, I encountered:

``` text
starlette.routing.NoMatchFound:
No route exists for name "home" and params "".
```

The template contained:

``` html
{{ url_for("home") }}
```

but the Python route function was named:

``` python
def Home(request: Request):
```

The route name was therefore `Home`, while the template requested
`home`.

The fix was:

``` python
def home(request: Request):
```

### Lesson

Route names are case-sensitive. When using:

``` jinja2
{{ url_for("home") }}
```

the application must have a route with the name `home`.

## Progress

-   [x] Video 1 --- Getting Started
-   [x] Video 2 --- HTML Frontend
-   [ ] Video 3
-   [ ] Video 4

## Next

Continue with the next Corey Schafer FastAPI tutorial video and update
the documentation after completing it.
