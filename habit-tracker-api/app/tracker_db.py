from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()

_db_pool = None


async def init_pool():
    global _db_pool
    db_url = os.getenv("DATABASE_URL")
    _db_pool = await asyncpg.create_pool(db_url)


async def close_pool():
    global _db_pool
    if _db_pool:
        await _db_pool.close()


async def get_db():
    async with _db_pool.acquire() as conn:
        yield conn


async def add_habit(db, name):
    row = await db.fetchrow(
        "INSERT INTO habits (name) VALUES ($1) RETURNING id, created_at", name
    )
    return {"id": row["id"], "name": name, "created_at": row["created_at"]}


async def get_all_habits(db, skip: int = 0, limit: int = 100):
    rows = await db.fetch("SELECT id, name FROM habits LIMIT $1 OFFSET $2", limit, skip)
    return [dict(row) for row in rows]


async def update_habit(db, habit_id: int, new_name: str):
    row = await db.fetchrow(
        "UPDATE habits SET name = $1 WHERE id = $2 RETURNING id AS habit_id, name AS new_name",
        new_name,
        habit_id,
    )
    if row is None:
        return None
    else:
        return {"habit_id": row["habit_id"], "new_name": row["new_name"]}


async def delete_habit(db, habit_id: int):
    row = await db.fetchrow("DELETE FROM habits WHERE id = $1 RETURNING id", habit_id)
    if row is None:
        return None
    else:
        return f"Привычка с ID: {row['id']} удалена!"


async def mark_habit_complete(db, habit_id: int):
    try:
        row = await db.fetchrow(
            "INSERT INTO habit_completions (habit_id, created_at) VALUES ($1, NOW()) RETURNING habit_id, created_at",
            habit_id,
        )
        return {"habit_id": row["habit_id"], "created_at": row["created_at"]}
    except asyncpg.exceptions.UniqueViolationError:
        return None
