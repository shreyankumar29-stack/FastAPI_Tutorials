# FastAPI Tutorial — Video 4: Pydantic Schemas

This folder contains the code and documentation for **Video 4**, focused on using **Pydantic schemas for request validation and response data** in FastAPI.

## 📚 Topics Covered

- Pydantic and `BaseModel`
- Creating schemas
- `Field()` validation
- `PostBase`
- `PostCreate`
- `PostResponse`
- Schema inheritance
- `ConfigDict`
- `from_attributes=True`
- Request body validation
- Response schemas
- Swagger UI / OpenAPI schemas
- HTTP 422 validation errors
- JSON decoding errors
- Debugging schema import errors

## 📁 Project Structure

```text
04-Pydantic-Schemas/
│
├── main.py
├── schemas.py
│
├── templates/
│   ├── layout.html
│   ├── home.html
│   └── post.html
│
└── static/
    ├── css/
    ├── js/
    └── images/
```

## 🚀 Setup

This project uses the shared virtual environment from the parent `FastAPI_Tutorials` directory.

From this folder:

```powershell
..\.venv\Scripts\activate
```

If FastAPI is not installed:

```powershell
pip install "fastapi[standard]"
```

## ▶️ Run the Application

```powershell
fastapi dev main.py
```

## 🌐 Important Routes

### Home

```text
/
```

### Posts

```text
/posts
```

### Create Post API

```text
POST /api/posts
```

### Get Posts API

```text
GET /api/posts
```

### Individual Post API

```text
GET /api/posts/{post_id}
```

## 🧩 Pydantic Schemas

The tutorial uses three related schemas:

```text
PostBase
   ├── PostCreate
   └── PostResponse
```

### PostBase

Contains the common fields:

```python
class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)
```

### PostCreate

Used for creating a post:

```python
class PostCreate(PostBase):
    pass
```

### PostResponse

Used for returning a post:

```python
class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str
```

## 📝 Example Request Body

For `POST /api/posts`:

```json
{
  "title": "My New Post",
  "content": "This is my Content",
  "author": "Test User"
}
```

The request uses the fields defined by `PostCreate`.

## 🔍 Validation

The schema validates:

- `title`: 1–100 characters
- `content`: minimum 1 character
- `author`: 1–50 characters

Invalid data can result in a `422 Unprocessable Content` response.

## 📖 Swagger UI

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

The Pydantic schemas are automatically reflected in the request and response documentation.

## ⚠️ Errors Encountered

### Schema Import Error

If `main.py` contains:

```python
from schemas import Post, PostCreate, PostResponse
```

but `schemas.py` only defines:

```text
PostBase
PostCreate
PostResponse
```

Python raises:

```text
ImportError: cannot import name 'Post' from 'schemas'
```

The imported names must match the classes actually defined in `schemas.py`.

### JSON Decode Error

A response such as:

```text
422 Unprocessable Content
JSON decode error
Expecting value
```

means the request body could not be decoded as valid JSON.

A valid request body is:

```json
{
  "title": "My New Post",
  "content": "This is my Content",
  "author": "Test User"
}
```

## 🎯 Learning Outcome

After completing Video 4, you should be able to:

1. Create Pydantic models with `BaseModel`.
2. Add validation using `Field()`.
3. Reuse schemas using inheritance.
4. Separate create and response schemas.
5. Validate JSON request bodies in FastAPI.
6. Understand how schemas appear in Swagger UI.
7. Use `ConfigDict(from_attributes=True)`.
8. Distinguish JSON decoding errors from Pydantic validation errors.
9. Debug schema import problems.

## 🛠️ Technologies

- Python
- FastAPI
- Pydantic
- Jinja2
- Starlette
