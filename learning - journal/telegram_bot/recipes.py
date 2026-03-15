# База рецептов
from zoneinfo import available_timezones

recipes = [
    {
        "name": "Яичница с помидорами",
        "ingredients": ["яйца", "помидоры", "соль", "масло"],
        "instructions": "1. Нарежь помидоры.\n2. Взбей яйца.\n3. Пожарь всё на сковороде.",
        "type": "обычный"
    },
    {
        "name": "Гречка по-студенчески",
        "ingredients": ["гречка", "вода", "соль", "масло"],
        "instructions": "1. Залей гречку водой 1:2.\n2. Вари 15 минут.\n3. Добавь масло.",
        "type": "обычный"
    },
    {
        "name": "Бабушкины блины",
        "ingredients": ["мука", "молоко", "яйца", "сахар", "соль", "масло"],
        "instructions": "1. Смешай всё.\n2. Жарь на сковороде.\n3. Секрет: добавляй ванилин!",
        "type": "бабушкин"
    }
]

def find_recipes(products):
    found = []
    for recipe in recipes:
        needed = set(recipe['ingredients'])
        available = set(products)
        if needed.issubset(available):
            found.append(recipe)
    return found

def get_babushka_recipes():
    result = []
    for recipe in recipes:
        if recipe['type'] == 'бабушкин':
            result.append(recipe)
    return result