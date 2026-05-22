people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
# отсортировать по возрастанию
people_sorted_age = sorted(people, key=lambda person: person["age"])
print(people_sorted_age)
# сортировка по имени
people_sorted_name = sorted(people, key=lambda  person: person["name"])
print(people_sorted_name)

# 2)
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        time.sleep(1)
        end = time.time()
        print(f"Функция {func.__name__} выполнилась за {end - start} секунд")
        return result
    return wrapper

@timer
def add(a, b):
    time.sleep(1)
    return a + b

print(add(3,6))

# 3)
def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Вызвана функция {func.__name__} с аргументами {args} {kwargs}")
        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

multiply(4,5)