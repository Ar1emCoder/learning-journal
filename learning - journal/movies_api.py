import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from movies_db import add_genre, get_all_genres

app = FastAPI(title="Каталог фильмов")

class GenreCreate(BaseModel):
    name: str

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в API Каталога фильмов!"}

@app.post("/genres/")
async def create_genre(genre: GenreCreate):
    result = await add_genre(genre.name)
    return result

@app.get("/genres/")
async def read_genres():
    try:
        result = await get_all_genres()
        return result
    except sqlite3.InternalError:
        # если такой уже есть
        raise HTTPException(status_code=400, detail="Такой жанр уже существует!")