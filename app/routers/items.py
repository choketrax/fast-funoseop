
from fastapi import APIRouter, HTTPException
from typing import List
from ..models.item import Item, ItemCreate

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

# In-memory storage for demo purposes
items_db = {}
counter = 0

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):
    global counter
    counter += 1
    new_item = Item(id=counter, **item.model_dump())
    items_db[counter] = new_item
    return new_item

@router.get("/", response_model=List[Item])
async def read_items():
    return list(items_db.values())

@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemCreate):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = Item(id=item_id, **item.model_dump())
    items_db[item_id] = updated_item
    return updated_item

@router.delete("/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}
