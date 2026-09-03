from fastapi import FastAPI, HTTPException, Depends
from app.tracker_db import update_habit, delete_habit, init_pool, close_pool, get_db


app = FastAPI()


@app.on_event("startup")
async def startup():
    await init_pool()


@app.on_event("shutdown")
async def shutdown():
    await close_pool()


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
