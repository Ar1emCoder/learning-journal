import sqlite3
import os

# Удаляем старую битую базу
if os.path.exists('finance_tracker.db'):
    os.remove('finance_tracker.db')
    print("🗑 Старая база удалена")

conn = sqlite3.connect('finance_tracker.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# 1. USERS (множественное число)
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        balance REAL DEFAULT 0.0
    )
''')

# 2. CATEGORIES
cursor.execute('''
    CREATE TABLE categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT,
        color TEXT DEFAULT '#000000'
    )
''')

# 3. TRANSACTIONS (связующая таблица)
cursor.execute('''
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        type TEXT NOT NULL CHECK(type IN ('income', 'expense')),
        date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
''')

# Заполняем данными
cursor.executemany("INSERT INTO users (username, email, balance) VALUES (?, ?, ?)", [
    ('artem', 'artem@test.com', 10000),
    ('ivan', 'ivan@test.com', 5000)
])

cursor.executemany("INSERT INTO categories (name, description, color) VALUES (?, ?, ?)", [
    ('Еда', 'Продукты', '#FF6B6B'),
    ('Транспорт', 'Такси', '#4ECDC4')
])

cursor.executemany("INSERT INTO transactions (user_id, category_id, amount, type) VALUES (?, ?, ?, ?)", [
    (1, 1, -500, 'expense'),
    (1, 2, -350, 'expense'),
    (2, 1, -800, 'expense')
])

conn.commit()
conn.close()
print("✅ Новая база 'finance_tracker.db' создана с правильными таблицами!")