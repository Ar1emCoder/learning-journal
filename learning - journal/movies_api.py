import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from movies_db import add_genre, get_all_genres, add_movie, get_all_movies, add_genre_to_movie, delete_movie, get_movie_with_genres

app = FastAPI(title="Каталог фильмов")

class GenreCreate(BaseModel):
    name: str

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в API Каталога фильмов!"}

@app.post("/genres/")
async def create_genre(genre: GenreCreate):
    try:
        result = await add_genre(genre.name)
        return result
    except sqlite3.IntegrityError:
        # если такой уже есть
        raise HTTPException(status_code=400, detail="Такой жанр уже существует!")

@app.get("/genres/")
async def read_genres():
    result = await get_all_genres()
    return result

class MovieCreate(BaseModel):
    title: str
    release_year: int
    rating: float

@app.post("/movies/")
async def create_movie(movie: MovieCreate):
    try:
        result = await add_movie(movie.title, movie.release_year, movie.rating)
        return result
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Такой фильм уже существует")

@app.get("/movies/")
async def read_movies():
    result = await get_all_movies()
    return result

@app.post("/movies/{movie_id}/genres/{genre_id}")
async def link_genre_to_movie(movie_id: int, genre_id: int):
    try:
        await add_genre_to_movie(movie_id, genre_id)
        return {"message": f"Жанр {genre_id} добавлен к фильму {movie_id}"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=404, detail="Фильм или жанр не найден!")


@app.delete("/movies/{movie_id}")
async def delete_movies_endpoint(movie_id: int):
    is_delete = await delete_movie(movie_id)
    if not is_delete:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    return {"message": "Фильм успешно удален"}


@app.get("/movies/{movie_id}")
async def get_movies_details(movie_id: int):
    movie = await get_movie_with_genres(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Фильм не найден!")
    return movie