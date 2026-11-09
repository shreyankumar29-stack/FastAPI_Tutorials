# Part 10 – Commands

## Activate venv
```powershell
..\.venv\Scripts\activate
```

## Install settings
```powershell
pip install pydantic-settings
```

## Install password hashing with Argon2
```powershell
pip install "pwdlib[argon2]"
```

## Install JWT support
```powershell
pip install PyJWT
```

## Run
```powershell
fastapi dev main.py
```

## Check packages
```powershell
pip list
pip show pwdlib
pip show pydantic-settings
pip show PyJWT
```

## Create .env
```powershell
New-Item .env -ItemType File
```

## Save dependencies
```powershell
pip freeze > requirements.txt
```

## Test endpoints
```text
POST http://localhost:8000/api/users
POST http://localhost:8000/api/auth/login
```
