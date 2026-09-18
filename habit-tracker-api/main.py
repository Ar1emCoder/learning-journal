from fastapi import FastAPI
from app import habits
from app.tracker_db import init_pool, close_pool
from app.init_tracker_db import init_db

# 1. Создаем главное приложение
app = FastAPI(title="Habit Tracker API")

# 2. Подключаем роутер из habits.py
app.include_router(habits.router)

# 3. События запуска и остановки переносим сюда
@app.on_event("startup")
async def startup():
    await init_pool()
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    await close_pool()