# FastAPI Tutorial — Video 7: Commands

Commands used for the **Sync to Async** part of the FastAPI tutorial.

## Navigate to the Project

```powershell
cd "07-Sync-Async"
```

## Activate the Shared Virtual Environment

```powershell
..\.venv\Scripts\activate
```

## Install Dependencies

FastAPI:

```powershell
pip install "fastapi[standard]"
```

SQLAlchemy:

```powershell
pip install sqlalchemy
```

Async SQLite driver:

```powershell
pip install aiosqlite
```

## Check Packages

```powershell
pip show fastapi
```

```powershell
pip show sqlalchemy
```

```powershell
pip show aiosqlite
```

```powershell
pip list
```

## Run the Application

```powershell
fastapi dev main.py
```

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

## ReDoc

```text
http://127.0.0.1:8000/redoc
```

## Stop the Server

```text
CTRL + C
```

## Syntax Checks

```powershell
python -m py_compile database.py
```

```powershell
python -m py_compile models.py
```

```powershell
python -m py_compile schemas.py
```

```powershell
python -m py_compile main.py
```

No output normally means the syntax check passed.

## Check Async Driver

```powershell
pip show aiosqlite
```

If missing:

```powershell
pip install aiosqlite
```

## Important Database URL

Correct:

```python
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"
```

Incorrect:

```python
SQLALCHEMY_DATABASE_URL = "sqlit+aiosqlite:///./blog.db"
```

## Update Requirements

```powershell
pip freeze > requirements.txt
```

## Git Commands

```powershell
git status
```

```powershell
git add 07-Sync-Async/
```

```powershell
git commit -m "Complete FastAPI Video 7 Sync Async"
```

```powershell
git push
```

## Quick Command List

```powershell
cd "07-Sync-Async"
..\.venv\Scripts\activate
pip install aiosqlite
fastapi dev main.py
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

Stop:

```text
CTRL + C
```
