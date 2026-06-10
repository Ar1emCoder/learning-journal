import sqlite3

conn = sqlite3.connect('finance_tracker.db')
cursor = conn.cursor()

qwery = '''
    WITH category_totals AS (
        SELECT
            c.name,
            SUM(t.amount) as total_sum
        FROM transactions t
        INNER JOIN categories c
            ON t.category_id = c.id
        WHERE t.type = 'expense'
        GROUP BY c.name
        )

        SELECT name, total_sum
        FROM category_totals
        WHERE total_sum > (SELECT AVG(total_sum) FROM category_totals)
'''
cursor.execute(qwery)
res = cursor.fetchall()
for r in res:
    print(f"{r[0]}: {r[1]}")
conn.close()