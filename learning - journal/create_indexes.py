import sqlite3

conn = sqlite3.connect('finance_tracker.db')
cursor = conn.cursor()

query1 = '''
    CREATE INDEX IF NOT EXISTS idx_user_date
        ON transactions(user_id, date);
'''
query2 = '''
    CREATE INDEX IF NOT EXISTS idx_transaction_date
        ON transactions(date);
'''
query3 = '''
    CREATE INDEX IF NOT EXISTS idx_user_id
        ON transactions(user_id);
'''
query4 = '''
    CREATE INDEX IF NOT EXISTS idx_category_id 
        ON transactions(category_id);
'''
cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)
cursor.execute(query4)

conn.commit()

answer = '''
    SELECT name, tbl_name
    FROM sqlite_master
    WHERE type = 'index';
'''
cursor.execute(answer)
ans = cursor.fetchall()
for a in ans:
    print(f" {a[0]} - {a[1]}")
conn.close()