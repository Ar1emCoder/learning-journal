# import sqlite3
#
# conn = sqlite3.connect('finance_tracker.db')
# cursor = conn.cursor()
#
# query = '''
#     SELECT
#         t.id,
#         u.username,
#         c.name,
#         t.amount,
#         t.transaction_type
#     FROM transactions t
#     INNER JOIN users u ON t.user_id = u.id
#     INNER JOIN categories c ON t.category_id = c.id
# '''
#
# cursor.execute(query)
# results = cursor.fetchall()
#
# print("Все транзакции:")
# print('-' * 50)
# for res in results:
#     print(f"ID: {res[0]} | Пользователь: {res[1]} | Категория: {res[2]} | Сумма: {res[3]} | Тип: {res[4]}")
#
# # 2 - Цель: Посчитать, сколько транзакций сделал каждый пользователь.
# qwery = '''
#     SELECT
#         u.username,
#     COUNT(*) as total_transactions
#     FROM transactions t
#     INNER JOIN users u
#         ON t.user_id = u.id
#     GROUP BY u.username
# '''
# cursor.execute(qwery)
# answer = cursor.fetchall()
# for ans in answer:
#     print(f"Пользователь: {ans[0]} | Количество транзакций: {ans[1]}")
#
# # 3 - суммировать, а не кол-во
# qwerys = '''
#     SELECT
#         u.username,
#     SUM(t.amount) as total_transactions
#     FROM transactions t
#     INNER JOIN users u
#         ON t.user_id = u.id
#     GROUP BY u.username
# '''
# cursor.execute(qwerys)
# answer = cursor.fetchall()
# for ans in answer:
#     print(f"Пользователь: {ans[0]} | Общие расходы: {ans[1]}")
#
# cursor.close()
# conn.close()
#
# # 4 - Задача: найти пользователей, у которых сумма расходов выше средней по всем пользователям
WITH user_totals AS (
    -- Здесь идёт обычный SELECT, который создаёт таблицу
    SELECT
        u.username,
        SUM(t.amount) as total_spent
    FROM transactions t
    INNER JOIN users u ON t.user_id = u.id
    WHERE t.transaction_type = 'expense'
    GROUP BY u.username
)
-- А здесь ты используешь эту временную таблицу
SELECT username, total_spent
FROM user_totals
WHERE total_spent > (SELECT AVG(total_spent) FROM user_totals)