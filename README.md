# FastAPI Learning Course

A structured learning repository for learning **FastAPI** by following the FastAPI tutorials by **Corey Schafer**.

The goal of this course is to understand FastAPI from the fundamentals to building production-style REST APIs, while practicing the concepts through hands-on coding.

> **Primary Learning Source:** Corey Schafer's FastAPI tutorial series
> **Language:** Python
> **Framework:** FastAPI
> **Server:** Uvicorn
> **Development Environment:** VS Code

---

## 📚 About This Course

This repository contains my code, notes, experiments, and practice work while learning FastAPI.

I am following Corey Schafer's tutorials and implementing the concepts myself rather than simply copying the code.

The course will gradually cover:

* FastAPI fundamentals
* API routing
* HTTP methods
* Path parameters
* Query parameters
* Request bodies
* Pydantic models
* Data validation
* CRUD operations
* Database integration
* SQLAlchemy
* Authentication and authorization
* JWT
* Dependency injection
* Error handling
* API testing
* Project structure
* Deployment concepts

---

## 🎯 Learning Goals

By completing this course, I aim to:

* Understand how FastAPI works internally and practically
* Build REST APIs using Python
* Work confidently with HTTP methods and status codes
* Validate API data using Pydantic
* Connect FastAPI applications with databases
* Implement CRUD operations
* Understand authentication and authorization
* Build structured and maintainable backend applications
* Test APIs using appropriate tools
* Create GitHub-ready FastAPI projects
* Apply FastAPI knowledge to real-world backend projects

---

## 🛠️ Technologies & Tools

| Technology / Tool | Purpose                           |
| ----------------- | --------------------------------- |
| Python            | Programming language              |
| FastAPI           | Web API framework                 |
| Uvicorn           | ASGI server                       |
| Pydantic          | Data validation                   |
| SQLAlchemy        | Database ORM                      |
| PostgreSQL        | Relational database               |
| SQLite            | Lightweight database for practice |
| VS Code           | Code editor                       |
| Git               | Version control                   |
| GitHub            | Project hosting                   |
| Swagger UI        | Interactive API documentation     |
| ReDoc             | API documentation                 |

---

## 📂 Repository Structure

The structure will evolve as I progress through the course.

```text
fastapi-learning/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── routers/
│
├── tests/
│
├── README.md
├── NOTES.md
├── COMMANDS.md
├── requirements.txt
└── .gitignore
```

> The complete structure will be introduced gradually instead of creating every file at the beginning.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd fastapi-learning
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install FastAPI

```bash
pip install "fastapi[standard]"
```

### 5. Run the application

For a basic FastAPI application:

```bash
fastapi dev main.py
```

The API will normally be available at:

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

These interfaces will be used throughout the course to test and understand the APIs.

---

## 🗺️ Course Roadmap

### Part 1 — FastAPI Fundamentals

* Introduction to FastAPI
* Creating a FastAPI application
* Routes
* HTTP GET requests
* Running the development server
* Automatic API documentation

### Part 2 — Routing & Parameters

* Path parameters
* Query parameters
* Multiple parameters
* Parameter validation
* HTTP methods

### Part 3 — Request & Response

* Request body
* JSON data
* Response models
* Status codes
* Headers

### Part 4 — Pydantic

* Pydantic models
* Type hints
* Data validation
* Optional fields
* Default values
* Nested models

### Part 5 — CRUD APIs

* Create
* Read
* Update
* Delete
* REST API design
* HTTP status codes

### Part 6 — Database Integration

* SQLite
* PostgreSQL
* SQLAlchemy
* Database models
* Sessions
* Relationships
* CRUD with databases

### Part 7 — Authentication

* User registration
* Password hashing
* Login
* OAuth2
* JWT tokens
* Protected routes

### Part 8 — Advanced FastAPI

* Dependency injection
* Middleware
* Exception handling
* CORS
* File uploads
* Background tasks
* Environment variables

### Part 9 — Testing

* API testing
* Pytest
* Test clients
* Testing CRUD operations
* Testing authentication

### Part 10 — Real-World Project

Build a complete backend application using the concepts learned throughout the course.

The final project will include:

* Proper project structure
* REST API
* Database
* CRUD operations
* Authentication
* Validation
* Error handling
* Testing
* Documentation
* Git/GitHub workflow

---

## 📝 Learning Method

For each tutorial section, I will follow this workflow:

```text
Corey Schafer Tutorial
        ↓
Watch & Understand
        ↓
Implement Code
        ↓
Experiment
        ↓
Debug Errors
        ↓
Practice
        ↓
Write Notes
        ↓
Update Documentation
        ↓
Commit to GitHub
```

The objective is to understand **why the code works**, not just reproduce it.

---

## 📁 Documentation

As the course progresses, additional documentation will be maintained:

### `NOTES.md`

Contains:

* Concepts learned
* Important explanations
* Code examples
* Common mistakes
* Important FastAPI terminology

### `COMMANDS.md`

Contains:

* Installation commands
* Virtual environment commands
* Server commands
* Package installation commands
* Git commands
* Useful development commands

---

## 🧪 Practice

Alongside Corey Schafer's tutorial, I will create small exercises to reinforce the concepts.

Examples:

* Simple greeting API
* Student API
* Product API
* Todo API
* User registration API
* CRUD API
* Database-backed API

---

## 🐛 Debugging Approach

When an error occurs, I will first try to understand:

1. What the error says
2. Which file caused the error
3. Which line caused the problem
4. Why the problem occurred
5. How to fix it
6. How to prevent the same problem in the future

This will help develop practical backend debugging skills.

---

## 📌 Important Notes

This repository is primarily a **learning repository**.

The code may evolve as my understanding of FastAPI improves. Some early implementations may later be refactored into better project structures or modern approaches.

Corey Schafer's tutorial is the primary learning resource, while additional documentation will be used when necessary to understand current FastAPI/Python practices.

---

## 👨‍💻 Learning Source

**Corey Schafer**

This course is being followed primarily through Corey Schafer's FastAPI tutorials.

---

## 📈 Progress

* [ ] FastAPI installation & setup
* [ ] First FastAPI application
* [ ] Routing
* [ ] Path parameters
* [ ] Query parameters
* [ ] Request body
* [ ] Pydantic
* [ ] CRUD operations
* [ ] Database integration
* [ ] SQLAlchemy
* [ ] Authentication
* [ ] JWT
* [ ] Dependency injection
* [ ] Error handling
* [ ] Testing
* [ ] Final project

---

## 📜 License

This repository is intended for educational and learning purposes.

The tutorial content belongs to its respective creator. This repository contains my own implementations, notes, experiments, and learning documentation.

---

**Learning FastAPI step by step 🚀**
