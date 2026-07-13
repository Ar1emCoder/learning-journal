# import sqlite3
#
# def get_connection():
#     conn = sqlite3.connect('finance_tracker.db')
#     conn.execute("PRAGMA foreign_keys = ON")
#     return conn
#
# def show_all_transactions():
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     cursor.execute("""
#         SELECT t.amount, t.type, u.username, c.name
#         FROM transactions t
#         JOIN users u ON t.user_id = u.id
#         JOIN categories c ON t.category_id = c.id
#     """)
#     result = cursor.fetchall()
#     for res in result:
#         print(f"Транзакция: {res[0]} руб., тип: {res[1]}, пользователь: {res[2]}, категория: {res[3]}")
#     conn.close()
#
#
# def add_transaction(user_id, category_id, amount, type):
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     cursor.execute("""
#         INSERT id FROM users WHERE id = ?
#         SELECT id FROM categories WHERE id = ?
#     """)
#     conn.close()
#
# def get_user_balance(user_id):
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     cursor.execute("""
#         SELECT SUM(amount) as balance FROM transactions WHERE user_id = ?
#     """)
#     result = cursor.fetchall()
#     balance = result[0] if result else 0
#     cursor.close()
#     return balance
#
# if __name__ == "__main__":
#     show_all_transactions()
#     add_transaction(1, 2, -200.0, 'expense')  # Должно сработать
#     add_transaction(99, 1, -100.0, 'expense')  # Должно выдать ошибку
#     print("Баланс пользователя 1: ", get_user_balance(1))

#--------------------------------------------------------------------------------------------

import sqlite3


def get_connection():
    """
    Вспомогательная функция для подключения к базе данных.
    Включает поддержку внешних ключей (foreign keys).
    """
    conn = sqlite3.connect('finance_tracker.db')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def show_all_transactions():
    """
    Выводит все транзакции с именами пользователей и категориями.
    Использует JOIN для связи трёх таблиц.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # JOIN соединяет таблицы по внешним ключам
    cursor.execute("""
        SELECT t.amount, t.type, u.username, c.name
        FROM transactions t
        JOIN users u ON t.user_id = u.id
        JOIN categories c ON t.category_id = c.id
    """)

    # Получаем все строки результата
    results = cursor.fetchall()

    # Выводим каждую транзакцию
    for row in results:
        amount, type_, username, category = row
        print(f"Транзакция: {amount} руб., тип: {type_}, пользователь: {username}, категория: {category}")

    conn.close()


def add_transaction(user_id, category_id, amount, type):
    """
    Добавляет новую транзакцию с проверкой существования пользователя и категории.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # ШАГ 1: Проверяем, существует ли пользователь
    cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
    if cursor.fetchone() is None:
        print(f"❌ Ошибка: пользователь с id={user_id} не найден")
        conn.close()
        return  # Выходим из функции, дальше не выполняем

    # ШАГ 2: Проверяем, существует ли категория
    cursor.execute("SELECT id FROM categories WHERE id = ?", (category_id,))
    if cursor.fetchone() is None:
        print(f"❌ Ошибка: категория с id={category_id} не найдена")
        conn.close()
        return

    # ШАГ 3: Вставляем транзакцию (только если обе проверки прошли)
    cursor.execute(
        "INSERT INTO transactions (user_id, category_id, amount, type) VALUES (?, ?, ?, ?)",
        (user_id, category_id, amount, type)
    )

    # ВАЖНО: сохраняем изменения!
    conn.commit()

    print(f"✅ Транзакция добавлена: пользователь {user_id}, категория {category_id}, сумма {amount}, тип {type}")
    conn.close()


def get_user_balance(user_id):
    """
    Считает баланс пользователя: сумма всех транзакций.
    (income положительный, expense отрицательный)
    """
    conn = get_connection()
    cursor = conn.cursor()

    # SUM(amount) сложит все транзакции.
    # Если expense хранится как отрицательное число (-500), то баланс посчитается правильно.
    cursor.execute(
        "SELECT SUM(amount) as balance FROM transactions WHERE user_id = ?",
        (user_id,)
    )

    # fetchone() возвращает одну строку (кортеж) или None
    result = cursor.fetchone()

    # Если транзакций нет — result будет (None,), поэтому проверяем
    balance = result[0] if result and result[0] is not None else 0

    cursor.close()
    conn.close()

    return balance


# ============================================
# ТЕСТИРОВАНИЕ
# ============================================
if __name__ == "__main__":
    print("=" * 50)
    print("📋 ВСЕ ТРАНЗАКЦИИ")
    print("=" * 50)
    show_all_transactions()

    print("\n" + "=" * 50)
    print("➕ ДОБАВЛЕНИЕ ТРАНЗАКЦИЙ")
    print("=" * 50)
    add_transaction(1, 2, -200.0, 'expense')   # Должно сработать
    add_transaction(99, 1, -100.0, 'expense')  # Должно выдать ошибку (нет пользователя 99)

    print("\n" + "=" * 50)
    print("💰 БАЛАНС ПОЛЬЗОВАТЕЛЕЙ")
    print("=" * 50)
    print(f"Баланс пользователя 1: {get_user_balance(1)} руб.")
    print(f"Баланс пользователя 2: {get_user_balance(2)} руб.")
    print(f"Баланс пользователя 3: {get_user_balance(3)} руб.")