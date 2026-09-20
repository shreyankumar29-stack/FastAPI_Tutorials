# FastAPI Tutorial — Video 4: Commands

Commands used while working on **Pydantic Schemas**.

## 📂 Navigate to the Folder

From `FastAPI_Tutorials`:

```powershell
cd "04-Pydantic-Schemas"
```

## 🐍 Activate the Shared Virtual Environment

```powershell
..\.venv\Scripts\activate
```

Verify that the terminal shows:

```text
(.venv)
```

## 📦 Install FastAPI

If required:

```powershell
pip install "fastapi[standard]"
```

Check FastAPI:

```powershell
pip show fastapi
```

Check Pydantic:

```powershell
pip show pydantic
```

Check Python:

```powershell
python --version
```

Check pip:

```powershell
pip --version
```

## ▶️ Start the Development Server

```powershell
fastapi dev main.py
```

## 🌐 Open the Application

Home:

```text
http://127.0.0.1:8000/
```

Posts:

```text
http://127.0.0.1:8000/posts
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## 🧪 Test the POST Endpoint

Open:

```text
http://127.0.0.1:8000/docs
```

Then:

```text
POST /api/posts
→ Try it out
→ Edit Value
```

Use:

```json
{
  "title": "My New Post",
  "content": "This is my Content",
  "author": "Test User"
}
```

Click **Execute**.

## 🧪 Test Validation

### Empty title

```json
{
  "title": "",
  "content": "This is my Content",
  "author": "Test User"
}
```

This violates:

```python
Field(min_length=1, max_length=100)
```

### Empty content

```json
{
  "title": "My New Post",
  "content": "",
  "author": "Test User"
}
```

This violates:

```python
Field(min_length=1)
```

### Empty author

```json
{
  "title": "My New Post",
  "content": "This is my Content",
  "author": ""
}
```

This violates:

```python
Field(min_length=1, max_length=50)
```

## 🛑 Stop the Server

Press:

```text
CTRL + C
```

## 🔄 Useful Git Commands

Check status:

```powershell
git status
```

Add Video 4:

```powershell
git add 04-Pydantic-Schemas/
```

Commit:

```powershell
git commit -m "Complete FastAPI Video 4 Pydantic Schemas"
```

Push:

```powershell
git push
```

## 📦 Optional Package Commands

Show all installed packages:

```powershell
pip list
```

Create/update requirements file:

```powershell
pip freeze > requirements.txt
```

## ⚠️ Troubleshooting

### `ImportError: cannot import name 'Post' from 'schemas'`

Check that the names imported in `main.py` actually exist in `schemas.py`.

For the current schema structure, the defined classes are:

```text
PostBase
PostCreate
PostResponse
```

### `422 JSON decode error`

If the error says:

```text
JSON decode error
Expecting value
```

check that the request body is valid JSON.

Use:

```json
{
  "title": "My New Post",
  "content": "This is my Content",
  "author": "Test User"
}
```

## 📌 Quick Command List

```powershell
cd "04-Pydantic-Schemas"
..\.venv\Scripts\activate
fastapi dev main.py
```

Test in:

```text
http://127.0.0.1:8000/docs
```

Stop:

```text
CTRL + C
```

Git:

```powershell
git status
git add 04-Pydantic-Schemas/
git commit -m "Complete FastAPI Video 4 Pydantic Schemas"
git push
```
