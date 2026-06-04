# def even_numbers(limit):
#     while 0 <= limit:
#         if limit % 2 == 0:
#             yield limit
#         limit -= 1
#
# for num in even_numbers(10):
#     print(num)
#
# # генератор с нечетными цифрами
# def even_numbers(limit):
#     while limit > 0:
#         if limit % 2 != 0:
#             yield limit
#         limit -= 1
#
# for x in even_numbers(10):
#     print(x)
from idlelib.debugger_r import close_subprocess_debugger


# Генератор с числами Фибоначчи
def fibonacci(n):
    pred = 0
    curr = 1
    cnt = 0
    while cnt < n:
        if cnt == 0:
            yield pred
        elif cnt == 1:
            yield curr
        else:
            pred, curr = curr, pred + curr
            yield curr
        cnt += 1

for x in fibonacci(10):
    print(x)