from dotenv import load_dotenv

load_dotenv()


async def add_habit(db, name):
    row = await db.fetchrow("INSERT INTO habits (name) VALUES ($1) RETURNING id", name)
    return {"id": row["id"], "name": name, "created_at": row["created_at"]}


async def get_all_habits(db, skip: int = 0, limit: int = 100):
    rows = await db.fetch("SELECT id, name FROM habits LIMIT $1 OFFSET $2", limit, skip)
    return [dict(row) for row in rows]
