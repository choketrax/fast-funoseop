
# Fast-Funoseop API

A FastAPI-based REST API for managing items.

## Features

- RESTful API endpoints for CRUD operations on items
- Interactive API documentation with Swagger UI and ReDoc
- Input validation using Pydantic models
- CORS support
- Auto-reload during development

## API Endpoints

- `GET /` - Welcome message
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation

### Items

- `POST /items/` - Create a new item
- `GET /items/` - List all items
- `GET /items/{item_id}` - Get a specific item
- `PUT /items/{item_id}` - Update an item
- `DELETE /items/{item_id}` - Delete an item

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --host 0.0.0.0 --port 54633 --reload
```

3. Visit the API documentation:
- Swagger UI: http://localhost:54633/docs
- ReDoc: http://localhost:54633/redoc

## Item Model

```python
{
    "id": 1,              # Optional, auto-generated
    "name": "string",     # Required
    "description": "string",  # Optional
    "price": 0.0,        # Required
    "is_available": true  # Optional, defaults to true
}
```
