from datetime import datetime

class Transaction:
    def __init__(self, amount, category, opi, type):
        self.id = None
        self.amount = amount
        self.category = category
        self.opi = opi
        self.date = datetime.now()
        self.type = type # прибыль и расходы

    def add_transaction(self, amount, category, discription, type):
        pass

    def get_balance(self):
        pass
class FinanceManager:
    def __init__(self, filename="finance.json"):
        self.filename = filename
        self.next_id = 1
        self.type = [] # один список для всех записей расходов и доходов
        self.load()




