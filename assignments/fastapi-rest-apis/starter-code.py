from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

items_db: Dict[int, Item] = {
    1: Item(id=1, name="Notebook", description="A simple notebook", price=4.99),
    2: Item(id=2, name="Pencil", description="A pencil for writing", price=1.25),
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/items/")
def list_items():
    return list(items_db.values())

@app.post("/items/")
def create_item(item: Item):
    if item.id in items_db:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items_db[item.id] = item
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"detail": "Item deleted"}

@app.get("/search/")
def search_items(q: Optional[str] = None, max_price: Optional[float] = None):
    results = list(items_db.values())
    if q:
        results = [item for item in results if q.lower() in item.name.lower() or (item.description and q.lower() in item.description.lower())]
    if max_price is not None:
        results = [item for item in results if item.price <= max_price]
    return results
