# 1 Пример
# students = []
#
# student1 = {'name': 'Anna', 'age': 20, 'city': 'Mockva'}
# student2 = {'name': "Ivan",  'age': 21, 'city': 'St.Peterburg'}
# student3 = {'name': 'Artyom', 'age': 18, 'city': 'Polsha'}
#
# students.append(student1)
# students.append(student2)
# students.append(student3)
#
# for student in students:
#     print(f"{student['name']}, {student['age']} лет,  {student['city']}")
#
# # вывести только имена
# for student in students:
#     print(student['name'])
#
# # поиск самого старшего
# oldest_age = 0
# oldest_name = ''
# for student in students:
#     if oldest_age < student['age']:
#         oldest_age = student['age']
#         oldest_name = student['name']
# print(f'Самый старший студент: {oldest_name}, которому {oldest_age} лет')
#
# # добавление нового через клавиатуру
# print("\n--- Добавление нового студента ---")
# new_name = input('Введите имя студента: ')
# new_age = int(input("Введите возраст студента: "))
# new_city = input('Введите город(страну): ')
# new_student = {'name': new_name, 'age': new_age, 'city': new_city}
# students.append(new_student)
# print(f'Добавлен: {new_student}')
# print(students)


# 2 Пример
products = []

product1 = {'name': 'Potato', 'price': 120, 'type': 'Овощи'}
product2 = {'name': 'Bread', 'price': 80, 'type': 'Хлебобулочные изделия'}
product3 = {'name': 'Apple', 'price': 230, 'type': 'Фрукты'}
products.append(product1)
products.append(product2)
products.append(product3)

print('=== ВСЕ ПРОДУКТЫ ===')
for product in products:
    print(product)

def add_product():
    new_name = input('Введите название продукта: ')
    new_price = int(input('Введите цену за продукт: '))
    new_type = input('Введите тип продукта')

    product = {'name': new_name, 'price': new_price, 'type': new_type}
    products.append(product)
    print(f'Добавлено: {product}')

total_price = 0
for product in products:
    total_price += product['price']
print(f'Общая стоимость: {total_price} руб.')

print("\n=== ФРУКТЫ ===")
for product in products:
    if product['type'] == 'Фрукты':
        print(f"{product['name']} - {product['price']} руб. {product['type']}")
