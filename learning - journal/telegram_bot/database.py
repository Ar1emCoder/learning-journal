import sqlite3

DB_PATH = 'recipes.db'


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                instructions TEXT NOT NULL,
                type TEXT NOT NULL
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS recipe_ingredients (
                recipe_id INTEGER,
                ingredient_id INTEGER,
                FOREIGN KEY (recipe_id) REFERENCES recipes(id),
                FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
            )
        ''')

    conn.commit()
    conn.close()
    print("База рецептов готова!")


def get_all_recipes_from_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, instructions, type FROM recipes')
    rows = cursor.fetchall()
    conn.close()

    recipes = []
    for row in rows:
        recipes.append({
            'id': row[0],
            'name': row[1],
            'instructions': row[2],
            'type': row[3]
        })
    return recipes

def find_recipes_in_db(products):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Шаг 2: создаём строку с плейсхолдерами для продуктов (?, ?, ...)
    placeholders = ','.join('?' * len(products))

    query = f'''
        SELECT DISTINCT r.id, r.name, r.instructions, r.type
        FROM recipes r
        WHERE NOT EXISTS (
            SELECT 1
            FROM recipe_ingredients ri
            JOIN ingredients i ON ri.ingredient_id = i.id
            WHERE ri.recipe_id = r.id
            AND i.name NOT IN ({placeholders})
        )
    '''
    # Шаг 4: выполняем запрос, передавая список продуктов
    cursor.execute(query, products)
    # Шаг 5: получаем все строки результата
    rows = cursor.fetchall()
    conn.close()

    recipes_result = []
    for row in rows:
        recipes_result.append({
            'id': row[0],
            'name': row[1],
            'instructions': row[2],
            'type': row[3]
        })
    return recipes_result

if __name__ == '__main__':
    init_db()