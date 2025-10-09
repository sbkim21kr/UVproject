# main.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, Dict, Any

# Pydantic 모델 정의
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

# 메모리 내 데이터 저장소
fake_items_db: Dict[int, Item] = {}

# --- API 엔드포인트 정의 ---

# 루트 경로
@app.get("/")
def read_root():
    return {"Hello": "Welcome to the Simple Item API!"}

# 아이템 생성 (Create)
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
# It sets the HTTP status code for the response.
# status.HTTP_201_CREATED is a constant provided by FastAPI
# (via fastapi.status) that equals 201.
# HTTP 201 means: ✅ “Resource successfully created.”

async def create_item(item: Item):
    new_item_id = max(fake_items_db.keys()) + 1 if fake_items_db else 1

# ~~~if fake_items_db:~~~ is equivalent to ~~~if len(fake_items_db) > 0:~~~

    fake_items_db[new_item_id] = item
    # ID를 포함하여 반환 (간단하게 딕셔너리로)
    return {"item_id": new_item_id, **item.dict()}


    # “Create a new dictionary that includes item_id and
    # all the key-value pairs from item.dict().”


# The ** operator:

#     Unpacks a dictionary

#     Inserts its key-value pairs into another dictionary or function call




# 1. item: Item
#     FastAPI expects a JSON body that matches the Item model.
#     It parses and validates the input automatically.
# 2. new_item_id = max(...)
#     Generates a new ID by finding the highest existing key and adding 1.
#     If the DB is empty, starts at 1.
# 3. fake_items_db[new_item_id] = item
#     Stores the item in the in-memory dictionary using the new ID.
# 4. return {"item_id": ..., **item.dict()}
#     Returns a dictionary with:
#         The new item_id
#         All fields from the Item model



















# 모든 아이템 조회 (Read All)
@app.get("/items/", response_model=list[Dict[str, Any]]) # 응답 모델을 리스트로 명시

# response_model=list[Dict[str, Any]] tells FastAPI
# to expect a list of flexible key-value pairs.


# Pagination means breaking up a large list of data into smaller, manageable chunks — like pages in a book.
# Instead of sending all items at once, you send:
#     Page 1 → items 1–10
#     Page 2 → items 11–20
#     Page 3 → items 21–30 …and so on.

# The skip parameter tells your API:
#     “Ignore the first N items and start from there.”
# So:
#     skip=0 → start from the beginning
#     skip=10 → skip the first 10 items and start from item 11



async def read_all_items(skip: int = 0, limit: int = 10):
    all_items = [
        {"item_id": item_id, **item.dict()}
        for item_id, item in fake_items_db.items()
    ]
    return all_items[skip : skip + limit]

# 특정 아이템 조회 (Read One)
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    # It tells FastAPI:
    # “Stop here and send a structured error response to the client.”
    return fake_items_db[item_id]

# 아이템 수정 (Update)
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    fake_items_db[item_id] = item
    return item

# 아이템 삭제 (Delete)
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    del fake_items_db[item_id]
    return # No Content 응답
