import sqlite3

conn = sqlite3.connect('finance_tracker.db')
cursor = conn.cursor()

# включение проверки внешних ключей
cursor.execute("PRAGMA foreign_keys = ON;")

create_users = '''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        balance REAL DEFAULT 0.0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
cursor.execute(create_users)

create_categories = '''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT,
        color TEXT DEFAULT '#000000',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
cursor.execute(create_categories)

# связующая
create_transaction = '''
    CREATE TABLE IF NOT EXISTS transaction (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        transaction_type TEXT NOT NULL CHECK(transaction_tipe IN ('income', 'expense')),
        description TEXT,
        transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        
        -- Внешние ключи (FOREIGN KEY) - связь с другими таблицами!
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (category_id) REFERENCE categories(id) ON DELETE SET NULL
        )
    '''
cursor.execute(create_categories)

conn.commit()
print("✅ Все три таблицы созданы!")
print("   - users")
print("   - categories")
print("   - transactions")
conn.close()