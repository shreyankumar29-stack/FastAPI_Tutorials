# FastAPI Tutorial — Video 6: Commands

## Navigate to the Project

```powershell
cd "06-CRUD"
```

## Activate the Shared Virtual Environment

```powershell
..\.venv\Scripts\activate
```

## Install Dependencies

```powershell
pip install "fastapi[standard]"
```

```powershell
pip install sqlalchemy
```

## Check Packages

```powershell
pip show fastapi
```

```powershell
pip show sqlalchemy
```

```powershell
pip show pydantic
```

```powershell
pip list
```

## Run the Server

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

# CRUD Testing

## Create User

Open:

```text
POST /api/users
```

Then:

```text
Try it out → Enter JSON → Execute
```

## Get All Users

Open:

```text
GET /api/users
```

Then:

```text
Try it out → Execute
```

Use the response to find existing user IDs.

## Get One User

Open:

```text
GET /api/users/{user_id}
```

Enter an existing ID, for example:

```text
1
```

Then click **Execute**.

## Update User

Open:

```text
PATCH /api/users/{user_id}
```

Enter an existing ID:

```text
1
```

Example body:

```json
{
  "username": "NewUsername"
}
```

Click **Execute**.

## Delete User

Open:

```text
DELETE /api/users/{user_id}
```

Enter an existing ID and click **Execute**.

If the ID does not exist:

```text
404 User not found
```

## JSON Validation

Valid:

```json
{
  "username": "Shreyansh"
}
```

Invalid:

```json
{
  "username": "Shreyansh",
}
```

The second example has a trailing comma and can cause:

```text
422 Unprocessable Content
JSON decode error
Illegal trailing comma before end of object
```

# Syntax Checks

```powershell
python -m py_compile main.py
```

```powershell
python -m py_compile models.py
```

```powershell
python -m py_compile schemas.py
```

```powershell
python -m py_compile database.py
```

No output normally means the file passed the syntax check.

# Requirements

```powershell
pip freeze > requirements.txt
```

# Git Commands

```powershell
git status
```

```powershell
git add 06-CRUD/
```

```powershell
git commit -m "Complete FastAPI Video 6 CRUD"
```

```powershell
git push
```

# Quick Command List

```powershell
cd "06-CRUD"
..\.venv\Scripts\activate
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
