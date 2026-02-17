from datetime import datetime

class Transaction:
    def __init__(self, amount, category, description, type):
        self.id = None
        self.amount = amount
        self.category = category
        self.description = description
        self.data = datetime.now()
        self.type = type

class FinanceManager:
    def __init__(self, filename="finance.json"):
        self.next_id = 1
        self.filename = filename
        self.transactions = []
        # self.load()

    def add_transaction(self, amount, category, description, type):
        transaction = Transaction(amount, category, description, type)
        transaction.id = self.next_id
        self.transactions.append(transaction)
        self.next_id += 1
        # self.save()

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.type == "income":
                balance += transaction.amount
            elif transaction.type == "expense":
                balance -= transaction.amount
        return balance

    def show_transactions(self):
        if not self.transactions:
            print('Транзакций нет!')
            return
        print(f"--- Все транзакции {len(self.transactions)} ---")
        for transaction in self.transactions:
            type_rus = "Доход" if transaction.type == "income" else "Расход"
            print(f"[{transaction.id}] {transaction.amount} руб. | {type_rus} | Категория: {transaction.category}")
        print("-"*40)

if __name__ == "__main__":
    fm = FinanceManager()
    fm.add_transaction(1000, "work", "pay", "income")
    fm.add_transaction(200, "eat", "products", "expense")
    print(f"Баланс: {fm.get_balance()}")
    fm.show_transactions()