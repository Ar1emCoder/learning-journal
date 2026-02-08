# # Класс - это чертёж
# class Robot:
#     # __init__ - инструкция "как создать робота"
#     def __init__(self, name, year, battery=100):
#         self.name = name # у каждого робота своё имя
#         self.battery = battery # и свой уровень заряда
#         self.year = year
#
#     # Метод - что робот Может делать
#     def introduce(self):
#         print(f"Я робот {self.name}, заряд: {self.battery}%, мне {self.year} года")
#
#     def work(self):
#         if self.battery > 20:
#             self.battery -= 10
#             print(f"{self.name} проработал. Осталось: {self.battery}%")
#         else:
#             print(f"{self.name}: нужна зарядка!")
#
# # создаём объекты по чертежу
# robot1 = Robot("R2-D2", 2, 80)
# robot2 = Robot("C-3PO", 5, 50)
# robot3 = Robot("CR-32", 4, 30)
#
# # работаем с объектами (представятся)
# print("=== ПЕРВЫЙ ЗАПУСК ===")
# robot1.introduce()
# robot2.introduce()
# robot3.introduce()
#
# print("\n=== РАБОТА ===")
# robot1.work()
# robot2.work()
# robot2.work()
# robot3.work()
# robot3.work()
#
# print("\n=== ИТОГ ===")
# robot1.introduce()
# robot2.introduce()
# robot3.introduce()

import random

class GameCharacter:
    def __init__(self, name, health, damage, level = 1):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.level = level
        self.exp = 0
        self.is_alive = True

    def attack(self, enemy):
        if not self.is_alive:
                print(f"{self.name} мёртв и не может атаковать!")
                return
        if not enemy.is_alive:
            print(f"{enemy.name} уже мёртв!")
            return
        print(f"{self.name} атакует {enemy.name} и наносит {self.damage} урона!")
        enemy.health -= self.damage

        if enemy.health <= 0:
            enemy.health = 0
            enemy.is_alive = False
            print(f"{enemy.name} повержен!")

            exp_gained = enemy.level * 30
            self.gain_exp(exp_gained)

        else:
            print(f"У {enemy.name} осталось {enemy.health} здоровья.")
        # print(f"{self.name} атакует {enemy.name}!")
        # if enemy.health > 30:
        #     enemy.health -= self.damage
        #     print(f"У {enemy.name}: {enemy.health}% здоровья")
        # else:
        #     print(f"Необходимо восстановиться! Так как {enemy.health}% здоровья")

    def heal(self, amount):
        if not self.is_alive:
            print(f"{self.name} уже мёртв, лечение невозможно!")
            return

        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} полечился. Здоровье: {self.health}")

    def gain_exp(self, amount):
        """Получить опыт и проверить уровень"""
        self.exp += amount
        print(f"{self.name} получил {amount} опыта! Всего: {self.exp} опыта")

        exp_needed = self.level * 100
        if self.exp >= exp_needed:
            self.level_up()

    def level_up(self):
        '''Повысить уровень персонажа'''
        self.level = 1
        self.max_health += 20
        self.health = self.max_health
        self.damage += 5
        self.exp = 0

        print(f"{self.name} достиг {self.level} уровня")
        print("     +20 к максимальному здоровью")
        print("     +5 к урону")
        print(f"Здоровье восстановлено до {self.health}")

    def info(self):
        status = "Жив" if self.is_alive else "Мёртв"
        exp_needed = self.level * 100
        return f"{self.name} (ур. {self.level}): {self.health}/{self.max_health} HP,опыт: {self.exp}/{exp_needed}, {status}"

hero = GameCharacter("Артём", 100, 25)
monster = GameCharacter("Гоблин", 80, 10)

# print("===НАЧАЛО БОЯ===")
# print(hero.info())
# print(monster.info())
#
# print("\n===БОЙ===")
# hero.attack(monster)
# monster.attack(hero)
# hero.heal(20)
# hero.attack(monster)
# hero.attack(monster)
# hero.attack(monster)
#
# print("\n===ПОСЛЕ БОЯ===")
# print(hero.info())
# print(monster.info())
#
# monster.attack(hero)
print("\n=== ТЕСТ СИСТЕМЫ ОПЫТА ===")
hero = GameCharacter("Артём", 100, 25)
monster1 = GameCharacter("Гоблин", 60, 10)

hero.attack(monster1)  # должен убить с 3 атак
hero.attack(monster1)
hero.attack(monster1)  # здесь должен получить опыт

print(f"\nПосле первого боя: {hero.info()}")

# Второй бой для уровня
monster2 = GameCharacter("Орк", 80, 15)
hero.attack(monster2)
hero.attack(monster2)
hero.attack(monster2)
hero.attack(monster2)  # должен повысить уровень

print(f"\nФинальный статус: {hero.info()}")