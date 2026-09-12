# FastAPI Tutorial — Video 3: Commands

This file contains the commands used for the **Path Parameters** tutorial.

## 📂 Navigate to the Project

From the parent `FastAPI_Tutorials` directory:

```powershell
cd "03-Path-Parameters"
```

---

## 🐍 Activate Virtual Environment

The `.venv` is located in the parent directory:

```powershell
..\.venv\Scripts\activate
```

Verify that the environment is active. The terminal should show:

```text
(.venv)
```

---

## 📦 Install FastAPI

If FastAPI is not installed:

```powershell
pip install "fastapi[standard]"
```

Check the installed FastAPI package:

```powershell
pip show fastapi
```

Check Python:

```powershell
python --version
```

Check pip:

```powershell
pip --version
```

---

## ▶️ Run FastAPI Development Server

From the `03-Path-Parameters` folder:

```powershell
fastapi dev main.py
```

---

## 🌐 Test the Routes

Open the application in a browser.

### Home

```text
http://127.0.0.1:8000/
```

### Posts

```text
http://127.0.0.1:8000/posts
```

### Individual Post

```text
http://127.0.0.1:8000/posts/1
```

```text
http://127.0.0.1:8000/posts/2
```

### Posts API

```text
http://127.0.0.1:8000/api/posts
```

### Individual Post API

```text
http://127.0.0.1:8000/api/posts/1
```

```text
http://127.0.0.1:8000/api/posts/2
```

---

## 📖 FastAPI Documentation

The API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

Routes using:

```python
include_in_schema=False
```

are excluded from the generated API schema.

---

## 🧪 Test a 404 Response

Try an ID that does not exist:

```text
http://127.0.0.1:8000/posts/99
```

or:

```text
http://127.0.0.1:8000/api/posts/99
```

The application should return:

```text
404 Not Found
```

---

## 🛑 Stop the Development Server

Press:

```text
CTRL + C
```

---

## 🔄 Useful Git Commands

Check the current status:

```powershell
git status
```

Add the Video 3 files:

```powershell
git add 03-Path-Parameters/
```

Commit:

```powershell
git commit -m "Complete FastAPI Video 3 Path Parameters"
```

Push:

```powershell
git push
```

---

## 🧹 Optional: Check Installed Packages

```powershell
pip list
```

Save installed packages:

```powershell
pip freeze > requirements.txt
```

> Keep `.venv/` out of Git. The virtual environment should not be committed to the repository.

---

## ⚠️ Common Errors from This Video

### 1. Route name mismatch

Template:

```jinja2
{{ url_for('post_page', post_id=post.id) }}
```

Route:

```python
name="post_page"
```

These names must match.

---

### 2. Incorrect HTTPException capitalization

Incorrect:

```python
HTTPexception
```

Correct:

```python
HTTPException
```

Python is case-sensitive.

---

### 3. Incorrect Starlette import

If Starlette's HTTP exception is specifically required:

```python
from starlette.exceptions import HTTPException as StarletteHTTPException
```

The normal FastAPI exception is:

```python
from fastapi import HTTPException
```

---

## 📌 Quick Command List

```powershell
cd "03-Path-Parameters"
..\.venv\Scripts\activate
pip install "fastapi[standard]"
fastapi dev main.py
```

Stop server:

```text
CTRL + C
```

Git:

```powershell
git status
git add 03-Path-Parameters/
git commit -m "Complete FastAPI Video 3 Path Parameters"
git push
```
