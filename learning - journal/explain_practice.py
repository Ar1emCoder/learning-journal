import sqlite3

conn = sqlite3.connect('finance_tracker.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE INDEX IF NOT EXISTS indx_id
    ON transactions(amount)''')
conn.commit()

qwery = """
    EXPLAIN QUERY PLAN
        SELECT u.username, c.name, t.amount
        FROM transactions t
        INNER JOIN users u ON t.user_id = u.id
        INNER JOIN categories c ON t.category_id = c.id
        WHERE t.amount < -500
    """
cursor.execute(qwery)
plan = cursor.fetchall()
for p in plan:
    print(p)

