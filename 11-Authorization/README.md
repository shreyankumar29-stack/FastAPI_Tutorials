# FastAPI Tutorial – Part 10: Authentication

Part 10: Authentication – Registration and Login with JWT.

## Topics
- User registration
- Secure password hashing with `pwdlib` and Argon2
- Password verification
- Pydantic Settings
- `.env` configuration
- `SecretStr`
- JWT access tokens
- HS256
- Token expiration
- Login and authentication flow
- Swagger/Postman testing

## Authentication Flow
```text
Registration → validate data → hash password → store hash
Login → verify credentials → create JWT → return access token
```

## Settings
```python
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    secret_key: SecretStr
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

settings = Settings()
```

Example `.env`:
```env
SECRET_KEY=your-secret-key
```

Run:
```powershell
..\.venv\Scripts\activate
fastapi dev main.py
```
