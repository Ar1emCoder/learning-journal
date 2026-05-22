class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = max(0, health)
        self.damage = damage
        self.level = 1
        self.is_alive = True

    def take_damage(self, amount):
        if not self.is_alive:
            return
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} уже мёртв!")
            self.is_alive = False

    def attack(self, target):
        if not self.is_alive:
            print(f"Герой {self.name} мёртв и не может атаковать!")
            return
        if not target.is_alive:
            print(f"{target.name} уже мёртв!")
            return
        print(f"{self.name} атакует {target.name} и наносит {self.damage} урона!")
        target.take_damage(self.damage)

    def __str__(self):
        return f"Персонаж: {self.name}, Уровень: {self.level}, Здоровье: {self.health}"

    def __repr__(self):
        return f"Character('{self.name}', {self.health}, {self.damage})"

class Warrior(Character):
    def __init__(self, name, health=100, damage=25):
        super().__init__(name, health, damage)
        self.shield = 50

    def block_attack(self, damage):
        blocked = min(damage, self.shield)
        actual_damage = damage - blocked
        self.shield -= blocked
        self.take_damage(actual_damage)
        print(f"Щит поглотил {blocked} урона!")

class Mage(Character):
    def __init__(self, name, health=80, damage=15):
        super().__init__(name, health, damage)
        self.mana = 100

    def cast_spell(self, spell_name, target):
        if self.mana >= 20:
            self.mana -= 20
            extra_damage = 30
            print(f"{self.name} бросает '{spell_name}' на {target.name}!")
            target.take_damage(self.damage + extra_damage)
        else:
            print(f"Недостаточно маны у {self.name}")

def battle_round(attacker, defender):
    attacker.attack(defender)

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Предмет {item} добавлен.")

    def use_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            print(f'Предмет {item_name} использован.')
            return True
        else:
            print("Предмет не найден!")
            return False

class Adventurer(Character):
    def __init__(self, name):
        super().__init__(name, 120, 20)
        self.inventory = Inventory()

    def heal_with_potion(self):
        if self.inventory.use_item("Зелье здоровья"):
            self.health += 50
            print('Здоровье было восстановлено на 50 hp')
        else:
            print('Нет такого предмета в инвентаре')

# Тестирование
warrior = Warrior("Артём")
mage = Mage("Мерлин")

print(warrior)  # __str__
print(repr(warrior))  # __repr__

battle_round(warrior, mage)
battle_round(mage, warrior)

adventurer = Adventurer("Эльфрин")
adventurer.inventory.add_item("Зелье здоровья")
adventurer.heal_with_potion()
