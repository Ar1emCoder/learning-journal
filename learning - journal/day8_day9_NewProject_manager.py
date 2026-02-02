import json

def load_products():
    ''' Пытается загрузить продукты из файла 'products.json'. Если не получается - возвращает пустой список '''
    # пробуем открыть файл
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            data = json.load(f) # загружаем json
            return data
    except FileNotFoundError:
        print('Файл не найден, начинаем с пустого списка')
        return []

def save_products(products_list, filename='products.json'):
    '''Сохраняет список продуктов в JSON файл'''
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(products_list, f, ensure_ascii=False, indent=2) # ensure_ascii - сохраняет кириллицу правильно, indent - красивое, читабельное форматирование
        print(f"Данные сохранены в {filename}")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
        return False

def edit_product():
    show_all(with_numbers=True)
    if not products:
        print('Нет продуктов в списке для редактирования!')
        return
    while True:
        try:
            choice = int(input("Введите номер продукта для редактирования: "))
            if 1 <= choice <= len(products):
                products_index = choice - 1
                break
            else:
                print(f'Введите число от 1 до {len(products)}!')
        except ValueError:
            print('Введите число!')
    product = products[products_index]
    print("\n ===РЕДАКТИРУЕМ ПРОДУКТ===")
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Тип: {product['type']}")
    new_name = input("Введите новое название продукта (Enter - оставить текущим): ").strip()
    if new_name:
        product['name'] = new_name
    while True:
        new_price_str = input("Введите новую цену (Enter - оставить текущим): ").strip()
        if not new_price_str:
            break
        try:
            new_price = int(new_price_str)
            if new_price <= 0:
                print('Цена должна быть больше, чем 0 руб.!')
            else:
                product['price'] = new_price
                break
        except ValueError:
            print("Введите число!")
    new_type = input("Введите новый тип (Enter - оставить текущее): ").strip()
    if new_type:
        product['type'] = new_type
    save_products(products)
    print(f"\nПродукт {product['name']} успешно обновлён!")

def search_by_price_range():
    ''' Ищем продукты в указанном диапазоне Н: от min до max '''
    if not products:
        print("Нет продуктов, так как список пуст")
        return
    while True:
        try:
            min_price = int(input("Введите начало диапазона: "))
            if min_price < 0:
                print("Цена должна быть больше, чем 0 или равна 0!")
                break
            else:
                break
        except ValueError:
            print("Введите число!")
    while True:
        try:
            max_price = int(input("Введите конец диапазона: "))
            break
        except ValueError:
            print("Введите число!")
    print(f"\n ===ПРОДУКТЫ В ДИАПАЗОНЕ: {min_price} руб. - {max_price} руб.")
    for product in products:
        if min_price <= product['price'] <= max_price:
            print(f"{product['name']} по цене: {product['price']} руб.")

products = load_products() # загружаем сохранённые продукты
# Начальные продукты
if not products:
    products.append({'name': 'Potato', 'price': 120, 'type': 'Овощи'})
    products.append({'name': 'Bread', 'price': 80, 'type': 'Хлебобулочные изделия'})
    products.append({'name': 'Apple', 'price': 230, 'type': 'Фрукты'})
    save_products(products)
def add_product():
    new_name = input('Введите название продукта: ').strip()
    if not new_name:
        print('Имя не может быть пустым!')
        return

    while True:
        price_input = input("Введите цену за продукт: ").strip()
        try:
            new_price = int(price_input)
            if new_price <= 0:
                print("Цена должна быть больше, чем 0 руб.")
                continue
            break
        except ValueError:
            print("Введите число!")
    new_type = input('Введите тип продукта: ')

    product = {'name': new_name, 'price': new_price, 'type': new_type}
    products.append(product)
    save_products(products)
    print(f'Продукт {new_name} добавлен и сохранён!')

def show_all(with_numbers = False):
    print('\n=== ВСЕ ПРОДУКТЫ ===')
    if not products:
        print("Список продуктов пуст!")
        return
    for cnt, product in enumerate(products, start=1):
        if with_numbers:
            print(f"{cnt}: {product['name']} - {product['price']} руб. ({product['type']})")
        else:
            print(f"{product['name']} - {product['price']} руб. ({product['type']})")

def show_total():
    total = 0
    for product in products:
        total += product['price']
    print(f'\nОбщая стоимость: {total} руб.')

def show_fruits():
    print('\n=== ФРУКТЫ ===')
    found = False
    for product in products:
        if product['type'] == 'Фрукты':
            print(f"{product['name']} - {product['price']} руб.")
            found = True
    if not found:
        print("Фруктов нет")

def find_cheapest():
    """Находит самый дешёвый продукт"""
    if not products:
        print('Нет продуктов для сравнения')
        return
    cheapest_price = products[0]['price']
    cheapest_product = ''
    for product in products:
        if cheapest_price > product['price']:
            cheapest_price = product['price']
            cheapest_product = product['name']
    print(f"Самый дешёвый продукт: {cheapest_product}, стоящий {cheapest_price} руб.")

def find_expensive():
    """Находит самый дорогой продукт"""
    if not products:
        print('Нет продуктов для сравнения')
        return
    expensive_price = products[0]['price']
    expensive_product = ''
    for product in products:
        if expensive_price < product['price']:
            expensive_price = product['price']
            expensive_product = product['name']
    print(f"Самый дорогой продукт: {expensive_product}, стоящий {expensive_price} руб.")

def search_by_name():
    search_names = input("Введите название для поиска: ").strip().lower()
    flag = False
    for product in products:
        if product['name'] == search_names:
            print(f"Найден продукт: {product['name']} - {product['price']} руб.")
            flag = True
    if not flag:
        print("Данный продукт не найден!")

def remove_product():
    show_all()
    delete_product = input('Введите продукт для удаления: ')
    for i, product in enumerate(products):  # enumerate - даёт и индекс, и продукт
        if product['name'] == delete_product:
            removed = products.pop(i)
            print(f"Продукт {product['name']} удалён!")
            return
    print('Такого продукта нет в списке!')


# ГЛАВНОЕ МЕНЮ
while True:
    print('\n' + '=' * 30)
    print('1. Показать все продукты')
    print('2. Добавить продукт')
    print('3. Общая стоимость')
    print('4. Показать фрукты')
    print('5.1. Найти самый дешёвый продукт')
    print('5.2. Найти самый дорогой продукт')
    print('6. Выйти')
    print('7. Поиск по названию')
    print('8. Удалить продукт')
    print('9. Редактировать продукт')
    print('10. Продукты на ценовом диапазоне')

    choice = input('Выберите действие (1-10): ')

    if choice == '1':
        show_all()
    elif choice == '2':
        add_product()
    elif choice == '3':
        show_total()
    elif choice == '4':
        show_fruits()
    elif choice == '5.1':
        find_cheapest()
    elif choice == '5.2':
        find_expensive()
    elif choice == '6':
        save_products(products)
        print("Выход из программы")
        break
    elif choice == '7':
        search_by_name()
    elif choice == '8':
        remove_product()
    elif choice == '9':
        edit_product()
    elif choice == '10':
        search_by_price_range()
    else:
        print("Неверный выбор! Введите число от 1 до 10")