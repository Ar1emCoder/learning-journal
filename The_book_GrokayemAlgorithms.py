# # 1) Бинарный поиск - O(log n)
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None
binary_search([2, 4, 6, 8, 10, 12, 14], 8)
binary_search([2, 4, 6, 8, 10, 12, 14], 5)


# Проверочное задание № 1 - выполнено
def word_frequency(text):
    t = text.split()
    ans = {}
    for word in t:
        de = word.replace('.', '').replace(',','').replace('!','').replace('?','')
        al = de.lower()
        ans[al] = ans.get(al, 0) + 1
    return ans

text = "Hello world! Hello, world. hello"
result = word_frequency(text)
print(result)
# Ожидаемый результат: {'hello': 3, 'world': 2}