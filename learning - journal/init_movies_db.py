import aiosqlite
import asyncio


async def init_db():
    async with aiosqlite.connect('movies.db') as db:
        # 1. Таблица жанров
        await db.execute("""
            CREATE TABLE IF NOT EXISTS genres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)

        # 2. Таблица фильмов
        await db.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL UNIQUE,
                release_year INTEGER CHECK (release_year >= 1800),
                rating REAL CHECK (rating >= 0.0 AND rating <= 10.0)
            )
        """)

        # 3. Связующая таблица (Many-to-Many)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS movie_genres (
                movie_id INTEGER,
                genre_id INTEGER,
                PRIMARY KEY (movie_id, genre_id),
                FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
                FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
            )
        """)

        await db.commit()
        print("✅ База данных 'movies.db' успешно создана с ограничениями!")


if __name__ == "__main__":
    asyncio.run(init_db())