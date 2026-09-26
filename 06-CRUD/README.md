# FastAPI Tutorial — Video 6: CRUD Operations

This folder contains the code and documentation for **Video 6**, focused on CRUD operations with FastAPI, Pydantic, and SQLAlchemy.

## Topics Covered

- CRUD
- Create
- Read
- Update
- Delete
- POST
- GET
- PATCH
- DELETE
- SQLAlchemy sessions
- Database queries
- Pydantic update schemas
- Path parameters
- 404 handling
- 422 JSON errors
- Swagger UI testing

## Project Structure

```text
06-CRUD/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── templates/
└── static/
```

## CRUD Mapping

| Operation | HTTP Method | Purpose |
|---|---|---|
| Create | POST | Create a resource |
| Read | GET | Retrieve resources |
| Update | PATCH | Update part of a resource |
| Delete | DELETE | Delete a resource |

## User Endpoints

```text
POST   /api/users
GET    /api/users
GET    /api/users/{user_id}
PATCH  /api/users/{user_id}
DELETE /api/users/{user_id}
```

## Post Endpoints

```text
POST   /api/posts
GET    /api/posts
GET    /api/posts/{post_id}
PATCH  /api/posts/{post_id}
DELETE /api/posts/{post_id}
```

## Database Flow

```text
Client
   ↓
FastAPI Route
   ↓
Pydantic Schema
   ↓
SQLAlchemy Session
   ↓
Database
```

## Create

```python
db.add(object)
db.commit()
db.refresh(object)
```

## Read

```python
db.query(User).all()
```

or:

```python
db.query(User).filter(User.id == user_id).first()
```

## Update

```python
user.username = user_update.username
db.commit()
db.refresh(user)
```

## Delete

```python
db.delete(user)
db.commit()
```

## 404 User Not Found

If an endpoint returns:

```json
{
  "detail": "User not found"
}
```

the requested ID does not exist.

Use:

```text
GET /api/users
```

to check existing IDs.

## 422 JSON Error

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

The invalid example has a trailing comma.

## Testing

Open:

```text
http://127.0.0.1:8000/docs
```

Use **Try it out → Execute** for each endpoint.

## Learning Outcome

After Video 6, you should be able to:

1. Explain CRUD.
2. Map CRUD to HTTP methods.
3. Create database records.
4. Read database records.
5. Update records.
6. Delete records.
7. Handle missing resources with 404.
8. Identify invalid JSON and 422 errors.
9. Test APIs with Swagger UI.

## Technologies

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Jinja2
- Starlette
