import aiosqlite

async def add_genre(name: str):
    async with aiosqlite.connect('movies.db') as db:
        cursor = await db.execute(
            "INSERT INTO genres(name) VALUES (?) ",
            (name, )
        )
        await db.commit()
        return {"id": cursor.lastrowid, "name": name}


async def get_all_genres():
    async with aiosqlite.connect('movies.db') as db:
        cursor = await db.execute(
            "SELECT id, name FROM genres"
        )
        genres = await cursor.fetchall()
        # Превращаем список кортежей в список словарей
        return [{"id": row[0], "name": row[1]} for row in genres]


async def add_movie(title: str, release_year: int, rating: float):
    async with aiosqlite.connect('movies.db') as db:
        cursor = await db.execute(
            "INSERT INTO movies (title, release_year, rating) VALUES (?, ?, ?)",
            (title, release_year, rating)
        )
        await db.commit()
        return {"id": cursor.lastrowid, "title": title, "release_year": release_year, "rating": rating}


async def get_all_movies():
    async with aiosqlite.connect('movies.db') as db:
        cursor = await db.execute(
            "SELECT id, title, release_year, rating FROM movies"
        )
        movies = await cursor.fetchall()
        return [{"id": row[0], "title": row[1], "release_year": row[2], "rating": row[3]} for row in movies]


# Связь таблиц: жанр - фильм
async def add_genre_to_movie(movie_id: int, genre_id: int):
    async with aiosqlite.connect('movies.db') as db:
        await db.execute("PRAGMA foreign_keys = ON")

        cursor = await db.execute(
            "INSERT INTO movie_genres (movie_id, genre_id) VALUES (?, ?)",
            (movie_id, genre_id)
        )
        await db.commit()

