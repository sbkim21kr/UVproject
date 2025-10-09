from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

# Pydantic 모델 정의
# This is a Pydantic model — it defines the structure of the data you expect:

#     name: required string

#     description: optional string

#     price: required float

#     tax: optional float

# FastAPI uses this to validate incoming data and generate docs.
class ItemAdvanced(BaseModel):
    name: str = Field(..., min_length=1, max_length=50) # ...은 필수 필드임을 의미
    description: str | None = Field(None, max_length=1000)
    price: float = Field(..., gt=0) # gt=0 은 price가 0보다 커야 함을 의미
    tax: float | None = Field(None, ge=0, le=100) # ge=0, le=100 은 0과 100 사이여야 함
    
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# POST 요청을 처리할 함수 추가

# This line defines a POST endpoint at /items/.
# Unlike GET (which retrieves data), POST is used to send data to the server,
# usually to create something new — like a new item in a database.
@app.post("/items-advanced/")
async def create_advanced_item(item: ItemAdvanced):
    return item

# 1. async def

#     This means the function is asynchronous — it can handle non-blocking operations like database access, file I/O, or network calls.

#     FastAPI supports both def and async def, but using async def is recommended when you plan to do things like:

#         Talk to a database

#         Call external APIs

#         Wait for long-running tasks

# Even if your function is simple now, using async def makes it future-proof.

# item: Item

#     This tells FastAPI: “Expect a JSON body that matches the Item model.”

#     FastAPI will:

#         Automatically parse the JSON

#         Validate the data types

#         Convert it into a Python object of type Item




    # from pydantic import BaseModel: Pydantic의 기본 클래스인 BaseModel을 가져옵니다.
    # class Item(BaseModel):: BaseModel을 상속받아 Item이라는 Pydantic 모델을 정의합니다.
    # name: str, price: float: 필드 이름과 해당 필드가 가져야 할 파이썬 타입 힌트를 지정합니다.
    # description: Optional[str] = None: Optional[str]은 str 타입이거나 None일 수 있음을 의미합니다. = None은 기본값을 None으로 설정하여 해당 필드가 선택 사항임을 나타냅니다. (Python 3.10+에서는 str | None = None)
    # @app.post("/items/"): /items/ 경로에 대한 POST 요청을 처리하는 함수임을 지정합니다.
    # async def create_item(item: Item)::
    #     async def: FastAPI는 비동기 함수도 지원합니다. 여기서는 간단한 예시를 위해 사용했지만, 복잡한 I/O 작업이 없다면 def를 사용해도 무방합니다.
    #     item: Item: 함수 매개변수로 Item 모델을 선언했습니다. FastAPI는 요청의 본문(Body)에서 JSON 데이터를 읽어 Item 모델의 유효성 검사를 수행하고, 유효하다면 해당 데이터를 item 객체로 만들어 함수에 전달합니다.
    #     item.dict(): Pydantic 모델 객체를 파이썬 딕셔너리로 변환합니다. (디버깅 등에 유용)


# Parsing means:

#     Taking data in one format and converting it into a structure your program can understand and work with.

# So yes — it's like changing the format, but it's also about understanding and organizing that data.