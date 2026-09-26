# FastAPI Tutorial — Video 5: Commands

Commands used for the **Database / SQLAlchemy** part.

## Navigate to the Project

```powershell
cd "05-Database"
```

## Activate the Shared Virtual Environment

```powershell
..\.venv\Scripts\activate
```

Check Python:

```powershell
python --version
```

Check pip:

```powershell
pip --version
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

Check packages:

```powershell
pip show fastapi
pip show sqlalchemy
pip show pydantic
```

## Run the Development Server

```powershell
fastapi dev main.py
```

## Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

## Open ReDoc

```text
http://127.0.0.1:8000/redoc
```

## Stop the Server

Press:

```text
CTRL + C
```

## Check Python Files for Syntax Errors

Database:

```powershell
python -m py_compile database.py
```

Models:

```powershell
python -m py_compile models.py
```

Schemas:

```powershell
python -m py_compile schemas.py
```

Main:

```powershell
python -m py_compile main.py
```

A successful compile normally produces no output.

## Fix `from __future__` Error

Incorrect:

```python
from sqlalchemy import create_engine

from __future__ import annotations
```

Correct:

```python
from __future__ import annotations

from sqlalchemy import create_engine
```

Then restart:

```powershell
fastapi dev main.py
```

## Useful Package Commands

```powershell
pip list
```

```powershell
pip freeze > requirements.txt
```

## Git Commands

Check status:

```powershell
git status
```

Add the project:

```powershell
git add 05-Database/
```

Commit:

```powershell
git commit -m "Complete FastAPI Video 5 Database"
```

Push:

```powershell
git push
```

## Quick Command List

```powershell
cd "05-Database"
..\.venv\Scripts\activate
pip install "fastapi[standard]"
pip install sqlalchemy
fastapi dev main.py
```

Stop with:

```text
CTRL + C
```
