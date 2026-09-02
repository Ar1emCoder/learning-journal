import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()


async def init_db():
    db_url = os.getenv("DATABASE_URL")
    conn = await asyncpg.connect(db_url)
    await conn.execute(
        """
        CREATE TABLE habits(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW());
        """
    )

    await conn.execute(
        """
        CREATE TABLE habit_completions(
            id SERIAL PRIMARY KEY,
            habit_id INTEGER,
            created_at TIMESTAMP DEFAULT NOW(),
            FOREIGN KEY (habit_id) REFERENCES habits(id) ON DELETE CASCADE);
        """
    )
