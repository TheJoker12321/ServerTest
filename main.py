from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Caesar(BaseModel):

    text: str
    offset: int
    mode: str = "encrypt" or  "decrypt"

@app.get("/test")
def test():
    return {"msg": "hi from test"}

@app.get("/test/{name}")
def extraction_name(name: str):
    with open("names.txt", "a") as file:
        file.write(name)
    return { "msg": "saved user"}
