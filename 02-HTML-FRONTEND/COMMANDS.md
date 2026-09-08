# FastAPI Tutorial Commands

Commands used while following Corey Schafer's FastAPI tutorial.

> This course uses **Python `venv` + `pip`**, not `uv`.

# Video 2 --- HTML Frontend

## 1. Activate the Existing Virtual Environment

The `.venv` is located in the parent `FastAPI_Tutorials` directory.

From:

``` text
FastAPI_Tutorials\02-HTML-FRONTEND
```

run:

``` powershell
..\.venv\Scripts\activate
```

The terminal should show:

``` text
(.venv)
```

------------------------------------------------------------------------

## 2. Run the Development Server

From the `02-HTML-FRONTEND` directory:

``` powershell
fastapi dev main.py
```

------------------------------------------------------------------------

## 3. Open the Application

``` text
http://127.0.0.1:8000
```

------------------------------------------------------------------------

## 4. Open Swagger UI

``` text
http://127.0.0.1:8000/docs
```

------------------------------------------------------------------------

## 5. Open ReDoc

``` text
http://127.0.0.1:8000/redoc
```

------------------------------------------------------------------------

## 6. Stop the Development Server

Press:

``` text
CTRL + C
```

------------------------------------------------------------------------

# Environment Commands

## Create a Virtual Environment

Only needed when creating a new environment:

``` powershell
python -m venv .venv
```

## Activate

``` powershell
.venv\Scripts\activate
```

or, from a child tutorial folder when `.venv` is in the parent:

``` powershell
..\.venv\Scripts\activate
```

## Deactivate

``` powershell
deactivate
```

## Check Python

``` powershell
python --version
```

## Check Python Executable

``` powershell
python -c "import sys; print(sys.executable)"
```

## Check FastAPI

``` powershell
pip show fastapi
```

------------------------------------------------------------------------

# Git Commands

Check status:

``` powershell
git status
```

Add changes:

``` powershell
git add .
```

Commit Video 2:

``` powershell
git commit -m "Complete FastAPI Video 2 - HTML frontend"
```

Push:

``` powershell
git push
```

------------------------------------------------------------------------

# Corey's `uv` vs My Setup

  Corey Schafer          My Setup
  ---------------------- -----------------------------------------
  `uv`                   Python `venv`
  `uv add ...`           `pip install ...`
  `uv run ...`           Run the command directly inside `.venv`
  `uv run fastapi dev`   `fastapi dev main.py`

The FastAPI concepts remain the same; only the
environment/package-management commands differ.

------------------------------------------------------------------------

# Video 2 Command Checklist

``` powershell
..\.venv\Scripts\activate
fastapi dev main.py
```

**Video 2 completed.**
