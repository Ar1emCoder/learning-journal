from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from database import create_user, get_user_by_id, get_all_users
import time

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    print(f"{request.method} {request.url.path}")

    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"{request.method} {request.url.path} - {response.status_code} ({process_time} сек)")

    return response

class User(BaseModel):
    username: str
    email: str
    age: int | None = None

@app.get("/")
async def root():
    return {"message": "Сервер работает с SQLite!"}

@app.post("/users")
async def create_user_endpoint(user: User):
    ans = await create_user(user.username, user.email, user.age)
    return ans

@app.get("/users")
async def get_users():
    ans = await get_all_users()
    return ans

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    ans = await get_user_by_id(user_id)
    if ans is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден!")
    else:
        return ans