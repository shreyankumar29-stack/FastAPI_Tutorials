# Part 10 – Authentication Notes

## Authentication vs Authorization
Authentication asks **who are you?** Authorization asks **what are you allowed to do?** Authorization is covered in Part 11.

## Password Hashing
Never store a plain password. Hash it before saving it.

```python
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
hashed_password = password_hash.hash(password)
password_hash.verify(password, hashed_password)
```

The tutorial uses `pwdlib` with Argon2.

## Pydantic Settings
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

`SecretStr` helps protect secret values. Use:
```python
settings.secret_key.get_secret_value()
```
when the actual value is required.

## JWT
JWT is used for token-based authentication.

```text
Login → verify password → create JWT → client receives token
```

JWT has:
```text
Header.Payload.Signature
```

Do not put a plain password in a token.

## HS256
```python
algorithm = "HS256"
```
HS256 is a symmetric JWT signing algorithm.

## Token Expiration
```python
access_token_expire_minutes: int = 30
```
Expiration limits how long an access token remains valid.

## OAuth2PasswordBearer
```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)
```

## Registration
```text
POST /api/users → validate → hash password → save user
```

## Login
```text
POST /api/auth/login → find user → verify password → create JWT
```

## Common Mistakes
Incorrect:
```python
algorithm: "HS256"
```
Correct:
```python
algorithm: str = "HS256"
```

Also keep `.env` out of Git:
```gitignore
.env
```
