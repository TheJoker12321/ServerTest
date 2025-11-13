from fastapi import FastAPI
from pydantic import BaseModel

from caesar_cipher import CaesarCipher
from fence_cipher import FenceCipher

app = FastAPI()

class Caesar(BaseModel):

    text: str
    offset: int
    mode: str = "encrypt" or  "decrypt"

class Fence(BaseModel):
    text: str

@app.get("/test")
def test():
    return {"msg": "hi from test"}

@app.get("/test/{name}")
def extraction_name(name: str):
    with open("names.txt", "a") as file:
        file.write(name)
    return { "msg": "saved user"}

@app.post("/caesar")
def return_caesar_cipher(caesar: Caesar):
    cipher = CaesarCipher()
    caesar = caesar.__dict__
    if caesar["mode"] == "encrypt":
        return {"encrypted_text": cipher.cipher(caesar["text"], caesar["offset"], "encrypt")}
    return {"decrypted_text": cipher.cipher(caesar["text"], caesar["offset"], "decrypt")}

@app.get("/fence/encrypt")
def encrypt_fence(text: str):
    return {"encrypted_text": FenceCipher().encrypt(text)}

@app.post("/fence/decrypt")
def decrypt_fence(fence: Fence):
    return {"decrypted": FenceCipher().decrypt(fence.text)}