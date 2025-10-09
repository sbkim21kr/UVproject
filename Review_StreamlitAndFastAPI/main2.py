from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"}
