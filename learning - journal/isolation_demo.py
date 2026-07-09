# import sqlite3
#
# # Подключение 1 (банк)
# conn1 = sqlite3.connect('finance_tracker.db')
# cursor1 = conn1.cursor()
#
# # Подключение 2 (клиент)
# conn2 = sqlite3.connect('finance_tracker.db')
# cursor2 = conn2.cursor()
#
# # Чистим таблицу, чтоб просто было изменить данные без ошибок
# # cursor1.execute("""DELETE FROM accounts""")
#
# account = """
#     CREATE TABLE IF NOT EXISTS accounts(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         balance REAL NOT NULL
#     )
# """
# cursor1.execute(account)
#
# # Добавляем данные
# cursor1.execute("""INSERT INTO accounts (balance) VALUES (1000)""")
# conn1.commit()
#
# cursor1.execute("Begin")
# cursor1.execute("""
#     UPDATE accounts SET balance = 500 WHERE id = 1
# """)
#
# cursor2.execute("""
#     SELECT balance FROM accounts WHERE id = 1
# """)
# result = cursor2.fetchall()
# print(f"Баланс до коммита: {result}")
#
# print("-"*30)
# print("БАнк подтверждает операцию (COMMIT) ...")
# conn1.commit()
#
# print("Клиент снова проверяет баланс...")
# cursor2.execute("""SELECT balance FROM accounts WHERE id = 1""")
# result_after = cursor2.fetchall()
# print(f"Баланс после коммита: {result_after}")
#
# conn1.close()
# conn2.close()

#---------------------------------------------------------------------------------
import sqlite3

connA = sqlite3.connect('finance_tracker.db', isolation_level=None, timeout = 10)
cursorA = connA.cursor()

connB = sqlite3.connect('finance_tracker.db', isolation_level= None, timeout=10)
cursorB = connB.cursor()

# Удаляем старую таблицу, если она есть
cursorA.execute("DROP TABLE IF EXISTS transactions")
connA.commit()

lost_update = """
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        money REAL NOT NULL,
        categories TEXT
    )
"""
cursorA.execute(lost_update)

# cat_to_account = [
#     ('Eat', 'Продукты и рестораны'),
#     ('Car', 'Driving a car and бензин'),
#     ('Sports', 'Gym and приспособления')
# ]
cursorA.execute(
    """INSERT INTO transactions (money, categories) VALUES (?, ?)""",
    (1000, 'Еда')
)

# cursorA.execute("""INSERT INTO updates (money) VALUE (1000) WHERE cat_to_account (Eat)""")

cursorA.execute("Begin")
cursorA.execute(
    """UPDATE transactions SET money = 1500 WHERE id = 1"""
)
connA.commit()

cursorB.execute("Begin")
cursorB.execute("""UPDATE transactions SET categories = 'Транспорт' WHERE id = 1""")
connB.commit()

cursorA.execute("""SELECT * FROM transactions WHERE id = 1""")
result = cursorA.fetchall()
print(f"Сумма после коммита: {result}")
