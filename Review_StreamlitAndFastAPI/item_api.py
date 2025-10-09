import fastapi
from pydantic import BaseModel

app = fastapi.FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: Item):
    return item
