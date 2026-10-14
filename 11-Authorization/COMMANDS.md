# Part 11 – Commands

## Activate venv
```powershell
..\.venv\Scripts\activate
```

## Run FastAPI
```powershell
fastapi dev main.py
```

## Check packages
```powershell
pip list
```

## Save dependencies
```powershell
pip freeze > requirements.txt
```

## Open Swagger
```text
http://localhost:8000/docs
```

## Postman – Bearer Token
Authorization → Type: Bearer Token → Token: `<access_token>`

## curl – protected route
```powershell
curl http://localhost:8000/api/protected
```

## curl – with bearer token
```powershell
curl http://localhost:8000/api/protected `
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
