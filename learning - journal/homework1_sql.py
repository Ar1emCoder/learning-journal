import sqlite3

conn = sqlite3.connect('home_sql.db')
cursor = conn.cursor()

categories_create = '''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT NOT NULL,
        color TEXT DEFAULT '#000000',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
cursor.execute(categories_create)

# Добавление категорий
cat_to_add = [
    ('Еда', 'Продукты и рестораны', '#FF6B6B'),
    ('Транспорт', 'Такси, бензин, метро', '#4ECDC4'),
    ('Развлечения', 'Кино, игры , хобби', '#95E1D3'),
    ('Зарплата', 'Доходы', '#2ECC71')
]

cursor.executemany(
    "INSERT INTO categories (name, description, color) VALUES (?, ?, ?)",
    cat_to_add
)

print("\nВсе категории: ")
cursor.execute("SELECT * FROM categories")
catteg = cursor.fetchall()
for cat in catteg:
    print(f"ID: {cat[0]} | Имя: {cat[1]} | Описание: {cat[2]} | Цвет: {cat[3]}")

cursor.execute(
    "SELECT * FROM categories WHERE name = ?",
    ('Еда',)
)
descrit_in_name = cursor.fetchall()
if descrit_in_name:
    print(f"Найдено описание: {descrit_in_name[0]}")
else:
    print("Ничего не найдено!")

cursor.execute(
    "UPDATE categories SET color = ? WHERE name = ?",
    ('#FF5733', 'Транспорт')
)

cursor.execute(
    "DELETE FROM categories WHERE name = ? ", ('Развлечения',)
)

conn.commit()
conn.close()

# -----------------------------

conn = sqlite3.connect('home_sql.db')
cursor = conn.cursor()

print("\n" + "=" * 50)
print("📊 Итоговое состояние таблицы 'categories':")

cursor.execute("SELECT * FROM categories")
categor = cursor.fetchall()
for c in categor:
    print(f" ID: {c[0]} | Имя: {c[1]} | Описание: {c[2]} | Цвет: {c[3]}")
