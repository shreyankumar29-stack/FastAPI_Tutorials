# FastAPI Tutorial Notes

Notes from learning FastAPI through the **Corey Schafer FastAPI tutorial series**.

---

# Video 1 — Getting Started

**Status:** ✅ Completed

---

## 1. What is FastAPI?

FastAPI is a modern Python web framework used for building APIs.

It is designed to make API development:

* Fast
* Simple
* Type-safe
* Easy to document
* Suitable for production applications

FastAPI uses Python type hints heavily.

---

# 2. Installing FastAPI

For this course, I am not using `uv`.

I am using:

```text
Python venv
+
pip
+
FastAPI
```

FastAPI can be installed using:

```bash
pip install "fastapi[standard]"
```

---

# 3. Virtual Environment

A virtual environment keeps project dependencies isolated from the system Python installation.

Create one with:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

After activation, the terminal shows:

```text
(.venv)
```

This indicates that the virtual environment is active.

---

# 4. Creating a FastAPI Application

Basic FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()
```

### Explanation

```python
from fastapi import FastAPI
```

Imports the `FastAPI` class.

```python
app = FastAPI()
```

Creates an instance of the FastAPI application.

The `app` object is used to define routes and configure the API.

---

# 5. Routes

A route defines what should happen when a client sends a request to a particular URL.

Example:

```python
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
```

### Breakdown

```python
@app.get("/")
```

Defines a GET route for `/`.

```python
def home():
```

Defines the function that handles the request.

```python
return {"message": "Hello, FastAPI!"}
```

Returns data from the endpoint.

FastAPI converts the Python dictionary into a JSON response.

---

# 6. GET Request

GET is an HTTP method commonly used to retrieve data.

For example:

```text
GET /
```

means the client is requesting the resource represented by `/`.

---

# 7. Running FastAPI

The development server can be started with:

```bash
fastapi dev main.py
```

FastAPI starts a development server using Uvicorn.

Example:

```text
http://127.0.0.1:8000
```

---

# 8. Uvicorn

Uvicorn is an **ASGI server**.

It is responsible for running the FastAPI application and handling HTTP requests.

The relationship can be understood as:

```text
Client
   ↓
Uvicorn
   ↓
FastAPI
   ↓
Route
   ↓
Python Function
   ↓
Response
```

---

# 9. Automatic API Documentation

One of FastAPI's useful features is automatic API documentation.

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides an interactive interface for testing API endpoints.

## ReDoc

```text
http://127.0.0.1:8000/redoc
```

ReDoc provides another automatically generated API documentation interface.

---

# 10. HTTP 500 Error

During Video 1, I encountered:

```text
500 Internal Server Error
```

The traceback showed:

```text
TypeError: list indices must be integers or slices, not str
```

The problematic code was:

```python
[0]['title']
```

A list is indexed using integers:

```python
items[0]
items[1]
items[2]
```

If the list contains dictionaries, then the dictionary key can be accessed afterward:

```python
items[0]["title"]
```

### Important lesson

Always read the traceback from the bottom upward and identify:

1. Error type
2. Error message
3. File
4. Line number
5. Problematic expression

---

# 11. HTTP 500 vs Application Setup

An important distinction from Video 1:

If FastAPI starts successfully:

```text
Application startup complete.
```

then FastAPI itself is running.

If a request returns:

```text
500
```

the problem may be inside the endpoint's Python code.

---

# 12. Important Concepts Learned

| Concept      | Meaning                            |
| ------------ | ---------------------------------- |
| FastAPI      | Python framework for building APIs |
| `FastAPI()`  | Creates the application            |
| Route        | Defines an API endpoint            |
| `@app.get()` | Creates a GET endpoint             |
| Uvicorn      | ASGI server                        |
| GET          | HTTP method for retrieving data    |
| JSON         | Common API response format         |
| Swagger UI   | Interactive API documentation      |
| ReDoc        | API documentation interface        |
| `.venv`      | Project virtual environment        |

---

# 13. Key Takeaways

### FastAPI application

```python
app = FastAPI()
```

### GET endpoint

```python
@app.get("/")
def home():
    return {"message": "Hello"}
```

### Start development server

```bash
fastapi dev main.py
```

### Swagger

```text
/docs
```

### ReDoc

```text
/redoc
```

---

# 14. Video 1 Summary

Video 1 introduced the basic workflow of FastAPI:

```text
Create Virtual Environment
        ↓
Install FastAPI
        ↓
Create FastAPI Application
        ↓
Create Route
        ↓
Start Server
        ↓
Send HTTP Request
        ↓
FastAPI Executes Route
        ↓
Return Response
```

**Video 1 completed successfully. ✅**

Next: **Video 2**
