import sqlite3

conn = sqlite3.connect('finance.db')
cursor = conn.cursor()

# Создание таблицы users
create_user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL, 
        balance REAL DEFAULT 0.0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
cursor.execute(create_user_table)
print("Таблица 'users' создана! (или уже существовала)")

# добавление данных (INSERT)
# 1 способ = используем ? вместо прямого подставления значений - это безопасно
cursor.execute(
    "INSERT INTO users (username, email, balance) VALUES (?, ?, ?)",
    ('artem', 'artem@test.com', 66072.40)
)
# 2 способ = сразу несколько
users_to_add = [
    ('ivan', 'ivan@test.com', 1000.54),
    ('dmitry', 'mity@execute.com', 3444.88),
    ('arseniy', 'ars@test.com', 786.67)
]

cursor.executemany(
    "INSERT INTO users (username, email, balance) VALUES (?, ?, ?)",
    users_to_add
)

print('Данные добавлены в таблицу')

# Чтение данных (SELECT)
# 1 = чтение данных всех пользователей
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall() # возвращает списки всех строк

print("\nВсе пользователи:")
print('-'*50)
for user in all_users:
    print(f" ID: {user[0]} | Имя: {user[1]} | Email: {user[2]} | Баланс: {user[3]}")

# 2 = чтение данных определенного (по условию)
cursor.execute("SELECT * FROM users")
stok = cursor.fetchall() # возвращает Одну строку или None

if stok:
    print(f"\nНайден пользователь: {stok[1]}, баланс: {stok[3]}")
else:
    print(f"\nПользователь не найден!")

# 3 = получить только определенные столбцы
cursor.execute("SELECT username, balance FROM users WHERE balance > ?", (400,))
rich_users = cursor.fetchall()

print("\nПользователи с балансом > 400: ")
for user in rich_users:
    print(f" {user[0]}: {user[1]}")

# 4 = сортировка и ограничения
cursor.execute ("SELECT * FROM users ORDER BY balance DESC LIMIT 2")
top_2 = cursor.fetchall()

print("\nТоп-2 по балансу: ")
for user in top_2:
    print(f" {user[1]}: {user[3]}")

# Обновление данных (UPDATE)
cursor.execute(
    "UPDATE users SET balance = ? WHERE username = ?",
    (67777.00, 'artem')
)
print(f"\nБаланс artem обновлен")

# Удаление данных(DELETE)
cursor.execute(
    "DELETE FROM users WHERE username = ?",('artem',)
)

# Сохранение изменений
conn.commit()
print('Изменения сохранены в finance.db')
# Освобождаем память
conn.close()
print('Соединение с БД закрыто!')


conn = sqlite3.connect('finance.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
final_users = cursor.fetchall()

print("\n" + "=" * 50)
print("📊 Итоговое состояние таблицы 'users':")
print("=" * 50)
for user in final_users:
    print(f"  ID: {user[0]} | {user[1]:10} | {user[2]:20} | {user[3]:.2f}")

conn.close()