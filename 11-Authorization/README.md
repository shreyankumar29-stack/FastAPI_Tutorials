# FastAPI Tutorial – Part 11: Authorization

Part 11: Authorization – Protecting Routes and Verifying the Current User.

## Topics
- Authorization
- Protected routes
- Bearer tokens
- `OAuth2PasswordBearer`
- JWT validation
- Current-user dependency
- `Depends()`
- Ownership checks
- Removing hardcoded user IDs
- Protecting edit/delete operations
- Account/profile concepts

## Authentication vs Authorization
```text
Authentication → Who are you?
Authorization  → What are you allowed to do?
```

## Protected Route
```python
@app.get("/protected")
async def protected_route(
    current_user: User = Depends(get_current_user)
):
    return current_user
```

## Ownership
Instead of:
```python
if post.user_id == 1:
```

use the authenticated user:
```python
if post.user_id != current_user.id:
    raise HTTPException(
        status_code=403,
        detail="Not authorized to perform this action"
    )
```

Run:
```powershell
..\.venv\Scripts\activate
fastapi dev main.py
```
