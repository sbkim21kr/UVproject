#  What is FastAPI?

# FastAPI is a Python framework for building web APIs
# — that means it lets you create endpoints
# that other programs (or your frontend) can call to get or send data.
# It's fast, modern, and uses Python type hints
# to make your code safer and easier to understand.


from fastapi import FastAPI

app=FastAPI()
# This creates your web application.
# Think of it as the "main engine" that will handle incoming requests.

@app.get("/")
# you're saying: "If someone visits the root of my site,
# run this function and return a response."

def read_root():
    """
    returns a simple JSON response when asked to print the route path
    """
    return {"Hello":"World"}
# @app.get("/"): This is a decorator that tells FastAPI:
# When someone sends a GET request to /, run the function below."
# read_root(): This is the function that runs when someone
# visits the root URL.
# return {"Hello": "World"}: This sends back a JSON response. 



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str|None=None):
    """
    handles item_id and selective query parameter q
    item_id must be an integer
    """
    response={"item_id": item_id}
    if q:
        response["q"] = q
    return response
# @app.get("/items/{item_id}"): This route accepts a path parameter
# called item_id. For example, /items/42.

# item_id: int: This means item_id must be an integer.
# FastAPI will automatically validate this.

# q: str | None = None: This is an optional query parameter.
# You can pass it like /items/42?q=banana.

#     If q is provided, it gets added to the response.

# The function builds a dictionary with the item_id, and optionally q,
# # and returns it as JSON.

# 🧩 Why the question mark?

# The question mark (?) in a URL separates the path from the query parameters.

# Let’s break it down:

#     /items/42 → This is the path. It tells FastAPI: 
# “Go to the items route and give me item number 42.”

#     ?q=banana → This is the query string. It starts with 
# ? and contains key-value pairs like q=banana.


    # from fastapi import FastAPI: FastAPI 클래스를 가져옵니다.
    # app = FastAPI(): FastAPI 애플리케이션의 인스턴스를 생성합니다. 이 app 객체를 사용하여 API 경로와 요청 핸들러를 정의합니다.
    # @app.get("/"): **데코레이터(Decorator)**입니다. @로 시작하는 이 구문은 바로 아래에 정의된 함수가 특정 경로와 HTTP 메서드에 대한 요청을 처리하도록 지정합니다.
    #     app.get: GET 요청을 처리하겠다는 의미입니다.
    #     "/": API의 루트 경로(기본 경로)를 의미합니다.
    # def read_root():: 경로 “/“에 대한 GET 요청이 오면 실행될 **경로 동작 함수(Path Operation Function)**입니다.
    #     함수가 반환하는 파이썬 딕셔너리는 자동으로 JSON으로 변환되어 응답으로 보내집니다.
    # @app.get("/items/{item_id}"): /items/ 다음에 오는 부분을 **경로 매개변수(Path Parameter)**로 받겠다는 의미입니다. {item_id} 부분이 동적으로 변하는 값입니다.
    # def read_item(item_id: int, q: str | None = None)::
    #     item_id: int: 경로에서 받은 item_id 값을 int 타입으로 받겠다는 의미입니다. FastAPI는 이를 자동으로 검증합니다. 만약 숫자가 아닌 값이 들어오면 에러를 반환합니다.
    #     q: str | None = None: q라는 이름의 **쿼리 매개변수(Query Parameter)**를 받습니다. | None = None은 이 파라미터가 선택적(optional)이며, 제공되지 않으면 None 값을 가진다는 의미입니다. (파이썬 3.10 이상에서는 str | None, 이전 버전에서는 Optional[str] 를 사용합니다. from typing import Optional 필요)
    #     이 함수는 URL에 ?q=somequery 와 같이 쿼리 문자열이 포함될 경우 q 변수에 해당 값이 할당됩니다.


# 터미널에서 main.py 파일이 있는 폴더로 이동한 후, 다음 명령어를 실행합니다.

# uvicorn main:app --reload

#     main: main.py 파일 (파이썬 모듈 이름).
#     app: FastAPI 인스턴스 (app = FastAPI() 에서 app 변수).
#     --reload: 코드가 변경될 때마다 서버를 자동으로 재시작해주는 옵션입니다. 개발 중에 매우 유용합니다.

# So think of /redoc as your API manual, and /docs as your API playground. 