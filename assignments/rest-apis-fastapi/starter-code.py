"""
FastAPI REST API Starter Code

This is a basic FastAPI application template. You will build upon this to create
a fully functional REST API. Uncomment and complete the endpoint functions below.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Create a FastAPI application instance
app = FastAPI(
    title="My REST API",
    description="A REST API built with FastAPI",
    version="1.0.0"
)

# Define your data model using Pydantic
class Item(BaseModel):
    """Model for an item in the API"""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

# In-memory data storage (replace with a database in production)
items_db: List[Item] = []


@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.
    
    Returns:
        A dictionary with a welcome message
    """
    return {"message": "Welcome to the REST API"}


# TODO: Implement the following endpoints

# 1. GET /items - Retrieve all items
# @app.get("/items")
# async def get_items():
#     """Retrieve all items from the database"""
#     pass


# 2. GET /items/{item_id} - Retrieve a specific item by ID
# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     """Retrieve a specific item by its ID"""
#     pass


# 3. POST /items - Create a new item
# @app.post("/items", status_code=status.HTTP_201_CREATED)
# async def create_item(item: Item):
#     """Create a new item and add it to the database"""
#     pass


# 4. PUT /items/{item_id} - Update an existing item
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     """Update an existing item by its ID"""
#     pass


# 5. DELETE /items/{item_id} - Delete an item
# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     """Delete an item by its ID"""
#     pass


if __name__ == "__main__":
    import uvicorn
    # Run the application with: python starter-code.py
    # Then visit http://localhost:8000/docs to view the interactive API documentation
    uvicorn.run(app, host="0.0.0.0", port=8000)
