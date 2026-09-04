from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from app.tracker_db import (
    add_habit,
    get_all_habits,
    update_habit,
    delete_habit,
    init_pool,
    close_pool,
    get_db,
    mark_habit_complete,
)


app = FastAPI()


class HabitCreate(BaseModel):
    name: str


@app.on_event("startup")
async def startup():
    await init_pool()


@app.on_event("shutdown")
async def shutdown():
    await close_pool()


@app.post("/habits")
async def create_habit(habit: HabitCreate, db=Depends(get_db)):
    result = await add_habit(db, habit.name)
    return result


@app.get("/habits")
async def read_habits(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    result = await get_all_habits(db, skip, limit)
    return result


@app.put("/habits/{habit_id}")
async def update_habit_endpoint(habit_id: int, new_name: str, db=Depends(get_db)):
    updated_habit = await update_habit(db, habit_id, new_name)
    if updated_habit is None:
        raise HTTPException(status_code=404, detail="Привычка не найдена!")
    return updated_habit


@app.delete("/habits/{habit_id}")
async def delete_habit_endpoint(habit_id: int, db=Depends(get_db)):
    result = await delete_habit(db, habit_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Привычка не найдена!")
    return {"message": result}


@app.post("/habits/{habit_id}/complete")
async def completed_habit(habit_id: int, db=Depends(get_db)):
    result = await mark_habit_complete(db, habit_id)
    if result is None:
        raise HTTPException(status_code=409, detail="Уже отмечено на сегодня!")
    else:
        return {"message": "Выполнено!", "data": result}
