from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Привет, Артём! Твой первый сервер работает"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Привет, {name}!"}

class User(BaseModel):
    username: str
    email: str
    age: int | None = None # необязательное поле