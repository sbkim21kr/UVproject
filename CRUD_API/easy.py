from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict

# Define the data model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# In-memory database (dictionary)
db: Dict[int, Item] = {}

# Create FastAPI app
app = FastAPI()

# add a root endpoint to FastAPI app
@app.get("/")
def read_root():
    return {"Hello": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"}


# Create (POST)
@app.post("/items/")
async def create_item(item: Item):
    item_id = max(db.keys()) + 1 if db else 1


    # every time you press the Create button, FastAPI gives the new item the next available ID,
    #  based on the largest one already in use.
    db[item_id] = item
    return {"item_id": item_id, "item": item}

# Read (GET)
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in db:
        return {"message": "Item not found"}
    return {"item_id": item_id, "item": db[item_id]}



# Update (PUT)
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in db:
        return {"message": "Item not found"}
    db[item_id] = item
    return {"item_id": item_id, "item": item}

# Delete (DELETE)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in db:
        return {"message": "Item not found"}
    del db[item_id]
    return {"message": f"Item {item_id} deleted successfully"}
