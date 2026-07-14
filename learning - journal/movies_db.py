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