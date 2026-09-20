# FastAPI Tutorial — Video 4: Pydantic Schemas

## 1. What is Pydantic?

Pydantic is used in FastAPI for **data validation and data modeling**.

It helps with:
- Validating request data
- Defining the expected structure of data
- Type validation and conversion
- Generating schemas in Swagger UI

---

## 2. BaseModel

Pydantic models inherit from `BaseModel`.

```python
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    author: str
```

---

## 3. Field Validation

`Field()` adds validation rules to model fields.

```python
from pydantic import BaseModel, Field

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)
```

| Field | Rule |
|---|---|
| title | 1–100 characters |
| content | At least 1 character |
| author | 1–50 characters |

---

## 4. PostBase

`PostBase` contains the fields common to posts:

```python
class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)
```

It is used as a base class for other schemas.

---

## 5. PostCreate

```python
class PostCreate(PostBase):
    pass
```

`PostCreate` inherits:
- `title`
- `content`
- `author`

It represents the data expected when **creating a post**.

`pass` means no additional fields are added.

---

## 6. PostResponse

```python
class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str
```

It contains:

```text
title
content
author
id
date_posted
```

The `id` and `date_posted` fields can be returned by the server rather than supplied when creating the post.

---

## 7. ConfigDict

```python
from pydantic import ConfigDict
```

The response schema uses:

```python
model_config = ConfigDict(from_attributes=True)
```

`from_attributes=True` allows Pydantic to read values from object attributes, which is useful when working with ORM/database objects.

---

## 8. Schema Inheritance

The structure is:

```text
              PostBase
             /        \
            /          \
     PostCreate     PostResponse
                       |
                 id: int
                 date_posted: str
```

This avoids repeating common fields.

---

## 9. Request Body

`POST /api/posts` accepts JSON based on `PostCreate`.

Example:

```json
{
  "title": "My New Post",
  "content": "This is my Content",
  "author": "Test User"
}
```

The client provides:

```text
title
content
author
```

---

## 10. Response Schema

A response can contain:

```json
{
  "title": "My New Post",
  "content": "This is my Content",
  "author": "Test User",
  "id": 3,
  "date_posted": "September 15, 2026"
}
```

The exact response depends on the endpoint implementation.

---

## 11. FastAPI + Pydantic Flow

```text
Client
   ↓
JSON Request
   ↓
FastAPI
   ↓
PostCreate
   ↓
Pydantic Validation
   ↓
Endpoint
   ↓
Response
```

FastAPI uses the Pydantic schema to understand and validate the request body.

---

## 12. Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI automatically displays the request and response schemas.

For `POST /api/posts`, the request body can look like:

```json
{
  "title": "My New Post",
  "content": "This is my Content",
  "author": "Test User"
}
```

The generated response schema can include:

```text
title
content
author
id
date_posted
```

---

## 13. 422 Validation Error

FastAPI commonly returns:

```text
422 Unprocessable Content
```

when request data cannot be processed.

### Pydantic validation error

Examples:
- Required field missing
- String too short
- String too long

### JSON decoding error

An error such as:

```text
type: json_invalid
msg: JSON decode error
ctx: Expecting value
```

means FastAPI could not decode the request body as valid JSON.

These are different from Pydantic field-validation errors.

A valid JSON body is:

```json
{
  "title": "My New Post",
  "content": "This is my Content",
  "author": "Test User"
}
```

---

## 14. Important Import Error

`main.py` previously tried to import:

```python
from schemas import Post, PostCreate, PostResponse
```

But the current `schemas.py` defines:

```text
PostBase
PostCreate
PostResponse
```

There is no `Post` class.

Therefore importing `Post` causes:

```text
ImportError: cannot import name 'Post' from 'schemas'
```

Always make sure the names imported in `main.py` match the classes actually defined in `schemas.py`.

---

## 15. Complete schemas.py

```python
from pydantic import BaseModel, ConfigDict, Field


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str
```

---

## 16. Why Separate Create and Response Schemas?

### `PostCreate`

Used for incoming data:

```text
title
content
author
```

### `PostResponse`

Used for outgoing data:

```text
title
content
author
id
date_posted
```

Separating them makes the API structure clearer and prevents clients from having to provide fields generated by the server.

---

## 17. Quick Revision

**Pydantic:** Data validation and modeling library used by FastAPI.

**BaseModel:**
```python
class PostBase(BaseModel):
```

**Field:**
```python
Field(min_length=1, max_length=100)
```

**Create schema:**
```python
class PostCreate(PostBase):
    pass
```

**Response schema:**
```python
class PostResponse(PostBase):
    id: int
    date_posted: str
```

**Model configuration:**
```python
model_config = ConfigDict(from_attributes=True)
```

**Swagger UI:**
```text
http://127.0.0.1:8000/docs
```

**Valid POST JSON:**
```json
{
  "title": "My New Post",
  "content": "This is my Content",
  "author": "Test User"
}
```

---

## 18. Main Learning Outcome

After Video 4, you should understand:

- Pydantic and `BaseModel`
- Request and response schemas
- `Field()` validation
- Schema inheritance
- `PostBase`, `PostCreate`, and `PostResponse`
- `ConfigDict(from_attributes=True)`
- Request-body validation in FastAPI
- Automatic Swagger schema generation
- The difference between JSON decoding errors and validation errors
- Why schema names must match imports
