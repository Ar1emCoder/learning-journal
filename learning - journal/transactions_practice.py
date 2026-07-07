# import sqlite3
#
# conn = sqlite3.connect('finance_tracker.db')
# cursor = conn.cursor()
#
# cursor.execute("PRAGMA foreign_keys = ON;")
# # Пример: Перевод денег между пользователями
# try:
#     cursor.execute("""
#         INSERT INTO transactions (user_id, category_id, amount, type)
#         VALUES (999, 1, -1000, 'expense')
#     """)
#
#     cursor.execute("""
#         INSERT INTO transactions (user_id, category_id, amount, type)
#         VALUES (2, 3, 1000, 'income')
#     """)
#
#     conn.commit()
#     print("Транзакция успешна!")
#
# except Exception as e:
#     conn.rollback()
#     print(f"Ошибка: {e}")
#     print("Транзакция отменена, данные не изменены")
#
# conn.close()

import sqlite3

conn = sqlite3.connect('finance_tracker.db')
cursor = conn.cursor()

cursor.execute("""PRAGMA foreign_keys = ON;""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        old_amount TEXT NOT NULL UNIQUE,
        changer_at  DATETIME DEFAULT CURRENT_TIMESTAMP)
    """)
conn.commit()

# cursor.execute("""
#     CREATE INDEX IF NOT EXISTS indx_id
#     ON transactions(id)
# """)
# conn.commit()

try:
    cursor.execute(
        "UPDATE transactions SET amount = ? WHERE id = ?",
        (-300, 1)
    )
    cursor.execute(
        "INSERT INTO audit_log (old_amount) VALUES (?)",
        (-500, )
    )
    print("Транзакция была изменена с -500 на -300")
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Ошибка: {e}")


