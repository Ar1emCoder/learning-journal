import sqlite3

conn = sqlite3.connect('finance_tracker.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT
        age INTEGER)
    """
)
conn.commit()
print("Таблица 'users' создана!")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Все таблицы в базе:", [t[0] for t in tables])

conn.close()