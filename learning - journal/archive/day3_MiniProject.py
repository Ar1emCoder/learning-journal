student = {
    "name": "Artyom",
    "age": 18,
    "subjects": ["Math", "Russian", "Informatics"],
    "grades": [2, 3, 4]
}
print("Введите новый предмет: ")
s = str(input())
student["subjects"].append(s)
print("Введите оценку по этому предмету: ")
while True:
    n = int(input())
# Доп задание
    if 2 <= n <= 5:
        student["grades"].append(n)
        break
    else:
        print("Некорректно, введите заново")
kol = 0
cnt = 0 # счётчик
for grades in student["grades"]:
    cnt += grades
    kol+=1
if cnt/kol >= 4.5:
    print("Отличник")
elif 4.5 > cnt/kol >= 4.0:
    print("Хорошист")
elif 4.0 > cnt/kol >= 3.0:
    print("Удовлетворительно")
else:
    print("Неуспевающий")
# вывод
print("============================")
print("       ОТЧЁТ СТУДЕНТА       ")
print("============================")
print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print("----------------------------")

print("ПРЕДМЕТЫ:")
print(f"Предмет: {student['subjects']}")
print(f"Оценка: {student['grades']}")
print("============================")

max_grade = max(student["grades"])
index_max = student["grades"].index(max_grade)
best_subject = student["subjects"][index_max]
print(f"Самый успешный предмет: {best_subject}({max_grade})")