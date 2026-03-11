import sqlite3
from datetime import date

DB_PATH = 'habits.db'

def get_all_habits():
    ''' Возвращает список всех привычек из БД '''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM habits")
    rows = cursor.fetchall()
    conn.close()

    habits = []
    for row in rows:
        habit = {
            'id': row[0],
            'name': row[1],
            'streak': row[2],
            'last_completed': row[3]
        }
        habits.append(habit)

    return habits

def add_habit_to_db(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    today = date.today().isoformat()
    conn.execute("INSERT INTO habits (name, last_completed) VALUES(?, ?)",
                 (name,today)
                )
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return new_id

def init_bd():
    ''' Создаёт таблицу habits, если её нет '''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            streak INTEGER DEFAULT 0,
            last_completed TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print('База данных готова!')

def update_habit_in_db(habit_id, new_streak, new_date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("UPDATE habits SET streak = ?, last_completed = ? WHERE id = ?",
                   (new_streak, new_date, habit_id))
    conn.commit()
    conn.close()


def delete_habit_from_db(habit_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM habits WHERE id = ?",
                   (habit_id,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_bd()
    print(get_all_habits())