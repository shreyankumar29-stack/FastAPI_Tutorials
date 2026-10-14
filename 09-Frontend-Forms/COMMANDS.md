# Part 9 – Frontend Forms Commands

## Activate the shared virtual environment

```powershell
..\.venv\Scripts\activate
```

## Install form support

```powershell
pip install python-multipart
```

## Run FastAPI

```powershell
fastapi dev main.py
```

## Check installed package

```powershell
pip show python-multipart
```

## Check all packages

```powershell
pip list
```

## Save dependencies

```powershell
pip freeze > requirements.txt
```

## Create templates folder if needed

```powershell
New-Item templates -ItemType Directory
```

## Create a form template

```powershell
New-Item templates\login.html -ItemType File
```

## Check project structure

```powershell
Get-ChildItem
```

## Check templates

```powershell
Get-ChildItem templates
```
