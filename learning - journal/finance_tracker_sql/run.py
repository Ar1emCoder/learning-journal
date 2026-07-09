import sqlite3

conn = sqlite3.connect('finance_tracker.db')
cursor = conn.cursor()

# Создаем через файл sql
with open('init_db.sql', 'r', encoding='utf-8') as f:
    cursor.executescript(f.read())

# Заполняем данными через sql
with open('seed_data.sql', 'r', encoding='utf-8') as f:
    cursor.executescript(f.read())

conn.commit()
print("База данный создана и заполнена!")

# Проверка
cursor.execute("SELECT * FROM users")
print("Пользователи:", cursor.fetchall())

cursor.execute("SELECT * FROM transactions")
print("Транзакции:", cursor.fetchall())

conn.close()