# FastAPI Tutorial

A learning repository for **FastAPI**, following the FastAPI tutorial series by **Corey Schafer**.

This repository contains my implementations, notes, commands, and practice work as I progress through the tutorial.

> **Learning Source:** Corey Schafer
> **Framework:** FastAPI
> **Language:** Python
> **Environment:** Python `venv` + `pip`

---

## 📚 About

This course is focused on learning FastAPI and building modern REST APIs with Python.

I am following Corey Schafer's tutorials and implementing the concepts myself to understand how FastAPI works rather than simply copying the code.

### Environment Difference

Corey Schafer uses `uv` in the tutorial.

For this course, I am using:

```text
Python
   ↓
venv
   ↓
pip
   ↓
FastAPI
   ↓
Uvicorn
```

instead of `uv`.

The FastAPI concepts remain the same; only the environment/package-management commands differ.

---

## 🎯 Learning Goals

* Understand FastAPI fundamentals
* Create and run FastAPI applications
* Understand API routes
* Work with HTTP methods
* Learn path and query parameters
* Handle request and response data
* Use Pydantic models
* Build CRUD APIs
* Connect APIs with databases
* Implement authentication
* Test APIs
* Build real-world backend applications

---

## 🛠️ Technologies

* Python
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy
* PostgreSQL
* SQLite
* VS Code
* Git
* GitHub
* Swagger UI
* ReDoc

---

## 📂 Current Project Structure

```text
FastAPI_Tutorials/
│
├── .venv/
│
├── 01-Getting-Started/
│   └── main.py
│
├── README.md
├── NOTES.md
└── COMMANDS.md
```

The project structure will grow as new tutorial sections are completed.

---


# ✅ Video 1 — Getting Started

In Video 1, I learned the basics of creating and running a FastAPI application.

### Topics Covered

* FastAPI installation
* Virtual environments
* Creating a FastAPI application
* `FastAPI()` object
* API routes
* GET requests
* Running the development server
* Uvicorn
* Automatic API documentation
* Swagger UI
* ReDoc
* Debugging a basic API error

---

## 🚀 Basic FastAPI Application

```python
from fastapi import FastAPI

app = FastAPI()
```

A FastAPI application is created using the `FastAPI()` class.

---

## 🌐 Running the Application

The development server can be started using:

```bash
fastapi dev main.py
```

The application runs at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 🐛 Debugging

During Video 1, I encountered an HTTP `500` error caused by incorrect Python list/dictionary indexing.

The error was:

```text
TypeError: list indices must be integers or slices, not str
```

This reinforced the importance of reading the traceback and identifying the exact line causing the error.

---

## 📌 Learning Approach

For every tutorial video:

```text
Watch
  ↓
Code Along
  ↓
Understand
  ↓
Practice
  ↓
Debug
  ↓
Document
  ↓
Commit to GitHub
```

The objective is to understand the concepts and not just reproduce the tutorial code.

---

## 📜 Learning Source

This course is primarily based on the **FastAPI tutorial series by Corey Schafer**.

The tutorial content belongs to its respective creator. This repository contains my own implementations, notes, experiments, and learning documentation.

---

