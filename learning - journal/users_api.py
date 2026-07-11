from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# Словарь для хранения пользователей
users_db: dict[int, User] = {} # id -> User
user_id_counter = 1

class User(BaseModel):
    username: str
    email: str
    age: int | None = None
--------------------------!!!---Над логикой сохранения подумать
@app.post("/users")
async def create_user(user: User):
    return {
        "message": f"Пользователь {user.username} создан. Его ID: {user_id_counter}!",
        "user": user
    }
user_id_counter += 1


@app.get("/")
async def root():
    return {"message": "Сервер работает! Открой /docs для тестирования"}
---------------------------------------------!!!----------------Дописать, чтоб всех пользователей выводил из БД
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "username": "Тестовый пользователь"}
