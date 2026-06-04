class FileGuard:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.file.write(f"\nОшибка: {exc_val}")

        self.file.close()
        return True # чтобы подавить исключение

with FileGuard('log.txt') as f:
    f.write("Начинаем работу\n")
    x = 1 / 0
    f.write("Эта строка не запишется")