import time, json

def logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        abc = {"function": func.__name__, "args": args, "kwargs": kwargs, "result": result, "timestamp": time.time()}
        with open('log.json', 'a', encoding='utf-8') as f:
            json.dump(abc, f, indent=4, ensure_ascii=False)
        print(f"Функция {func.__name__} выполнила работу за {finish - start} секунд; c аргументами {args, kwargs}")
        return result
    return wrapper

@logger
def add(a, b):
    time.sleep(2)
    return a + b

print(add(3, 5))


