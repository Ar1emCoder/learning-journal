# 1)
numbers = [10, 20, 30, 40, 50]
print("First элемент: ", numbers[0])
print("Последний элемент: ", numbers[-1])
numbers.append(100)
print("После добавление 100: ", numbers)
remove = numbers.pop(1)
print(f"Удалили элемент {remove}. Список теперь: ", numbers)
print("Длина итогового списка = ", len(numbers))

# 2)
student = {
    "name": "Иван",
    "age": 20,
    "subjects": ["математика", "физика"]
}
print(student["name"])
student["subjects"].append("Информатика")
for subjects in student["subjects"]:
    print(subjects)
student["year"] = 2026
print(student)
del student["age"]
print(student)

# 3)
print("Введите число: ")
n = int(input())
if n%2==0:
    for x in range(0,n+1):
        if x%3==0:
            print(x)
else:
    for x in range(n-1,0,-1):
        print(x)