# Part 8 – Routers Commands

## Activate the shared virtual environment

```powershell
..\.venv\Scripts\activate
```

## Create routers folder

```powershell
New-Item routers -ItemType Directory
```

## Create router files

```powershell
New-Item routers\__init__.py, routers\posts.py, routers\users.py -ItemType File
```

## Run FastAPI

```powershell
fastapi dev main.py
```

## Check installed packages

```powershell
pip list
```

## Check project files

```powershell
Get-ChildItem
```

## Check router files

```powershell
Get-ChildItem routers
```

## Save dependencies

```powershell
pip freeze > requirements.txt
```
