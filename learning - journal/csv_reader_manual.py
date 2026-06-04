# with open('data.csv', 'r', encoding='utf-8') as f:
#     headers = f.readline().strip().split(',')
#     for line in f:
#         value = line.strip().split(',')
#         person = {}
#         for i in range(len(headers)):
#             person[headers[i]] = value[i]
#         print(f"Имя: {person['name']}, Возраст: {person['age']}, Город: {person['city']}, Почта: {person['email']}")
#
# import csv
# with open('data.csv', 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(f"Имя: {row['name']}, Возраст: {row['age']}, Город: {row['city']}, Почта: {row['email']}")

# КОНВЕРТЕР CSV -> JSON
# import csv, json
#
# with open('data.csv', 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     data = []
#     for row in reader:
#         row['age'] = int(row['age'])
#         data.append(row)
#
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)

# 3
import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    people = csv.DictReader(f)
    middle_salary = 0
    gold_salary = 0
    cnt = 0
    for p in people:
        if int(p['salary']) > int(gold_salary):
            gold_salary = int(p['salary'])
        middle_salary += int(p['salary']) # сумма
        cnt += 1 # кол-во человек
    middle = middle_salary / cnt
    print(f'Средняя зарплата: {middle} - самая высокая зарплата: {gold_salary}')

with open('data.csv', 'r', encoding='utf-8') as f:
    people = csv.DictReader(f) # заново создали DictWriter
    with open('high_earners.csv', 'w', encoding='utf-8', newline='') as n:
        writer = csv.DictWriter(n, fieldnames=['name', 'department', 'salary'])
        writer.writeheader()
        for p in people:
            if int(p['salary']) >= middle:
                writer.writerow(p)

print("\nСодержимое high_earners.csv:")
with open('high_earners.csv', 'r', encoding='utf-8') as check:
    print(check.read())