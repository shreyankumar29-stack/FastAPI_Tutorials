# Part 11 – Authorization Notes

## 1. Authorization
Authorization determines what an authenticated user is allowed to access or modify.

Example:
```text
User A owns Post 1
User B owns Post 2
```
User A should not be allowed to edit User B's post.

## 2. Bearer Token
Protected requests normally send:
```text
Authorization: Bearer <access_token>
```

## 3. OAuth2PasswordBearer
```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)
```

## 4. Dependency Chain
```text
Request
 ↓
Bearer token
 ↓
Decode/validate JWT
 ↓
Find user
 ↓
Current user
 ↓
Protected route
```

## 5. Current User
A `get_current_user()` dependency can:
1. Receive the bearer token.
2. Decode and validate the JWT.
3. Extract the user identity.
4. Find the database user.
5. Return the current user.

Concept:
```python
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # decode token
    # find user
    # return user
    ...
```

## 6. Protecting Routes
```python
@app.get("/account")
async def account(
    current_user: User = Depends(get_current_user)
):
    return current_user
```

## 7. Ownership Checks
```python
if post.user_id != current_user.id:
    raise HTTPException(
        status_code=403,
        detail="Not authorized to perform this action"
    )
```

Use the same concept for update/delete operations.

## 8. Remove Hardcoded IDs
Avoid:
```python
if post.user_id == 1:
```
Use:
```python
if post.user_id != current_user.id:
```

## 9. Status Codes
- `401` → missing/invalid authentication credentials
- `403` → authenticated but not permitted

## 10. Authorization Flow
```text
Login → JWT
      ↓
Bearer token
      ↓
JWT validation
      ↓
Current user
      ↓
Permission/ownership check
      ↓
Allow or reject
```

## Testing
Without token:
```text
Authorization header missing → protected request rejected
```

With token:
```text
Authorization: Bearer <access_token>
```

Wrong owner:
```text
Valid user + another user's post → reject with authorization error
```

## Key Takeaways
- Authentication identifies the user.
- Authorization controls permissions.
- `Depends()` connects security dependencies to routes.
- `get_current_user()` identifies the authenticated user.
- Ownership checks protect user resources.
- Hardcoded user IDs should be removed.
