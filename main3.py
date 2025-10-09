from fastapi import FastAPI
from typing import Optional # Optional 사용을 위해 추가 (Python < 3.10)

app = FastAPI()

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, q: Optional[str] = None):
    """
    Returns a list of items with optional filtering.

    - `skip`: number of items to skip (for pagination)
    - `limit`: max number of items to return
    - `q`: optional search query
    """

    # 🧠 Why this is amazing:
    # You write comments for yourself or your team…
    # FastAPI turns them into API documentation for everyone!
    results = {"skip": skip, "limit": limit}
    if q:
        results["q"] = q
    return results

# 이전의 read_root 함수는 그대로 두거나 필요 없다면 제거해도 됩니다.
@app.get("/")
def read_root():
    return {"Hello": "World"}

