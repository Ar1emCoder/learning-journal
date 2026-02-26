import json
from datetime import datetime, timedelta

class Habit:
    def __init__(self, name, description):
        self.id = None
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.last_completed = None
        self.streak = 0

class HabitManager:
    def __init__(self, habits = None, next_id = 1, filename="habit_tracker.json"):
        if habits is None:
            habits = []
        self.filename = filename
        self.habits = habits
        self.next_id = next_id

    def add_habit(self, name, description):
        habit = Habit(name, description)
        habit.id = self.next_id
        self.habits.append(habit)
        self.next_id += 1

    def completed_habit(self, habit_id):
        today = datetime.now().date()

        for habit in self.habits:
            if habit == habit_id:
                if habit.last_completed in None:
                    habit.streak = 1
                else:
                    last = habit.last_completed
                    if isinstance(last, datetime):
                        last = last.date()

                    if last == today:
                        print(f"Привычка '{habit.name}' уже выполнена сегодня!")
                        return

                    elif last == today - timedelta(days=1):
                        habit.streak += 1

                    else:
                        habit.streak = 1

                habit.last_completed = today
                print('Выполнена')

    # def complete_habit(self, habit_id):
    #     # Получаем сегодняшнюю дату (без времени)    #     today = datetime.now().date()
    #
    #     # Ищем привычку по ID
    #     for habit in self.habits:
    #         if habit.id == habit_id:
    #             # Если привычка никогда не выполнялась
    #             if habit.last_completed is None:
    #                 habit.streak = 1
    #             else:
    #                 # Преобразуем last_completed в дату (если это datetime)
    #                 last = habit.last_completed
    #                 if isinstance(last, datetime):
    #                     last = last.date()
    #
    #                 # Сравниваем с сегодня и вчера
    #                 if last == today:
    #                     print(f"Привычка '{habit.name}' уже выполнена сегодня!")
    #                     return
    #                 elif last == today - timedelta(days=1):
    #                     habit.streak += 1
    #                 else:
    #                     habit.streak = 1
    #
    #             # Обновляем дату последнего выполнения
    #             habit.last_completed = today
    #             print(f"Привычка '{habit.name}' выполнена! Текущий streak: {habit.streak}")
    #             return
    #
    #     # Если привычка не найдена
    #     print(f"Привычка с ID {habit_id} не найдена")


if __name__ == "__main__":
    manager = HabitManager()
    print("Add habit...")
    manager.add_habit("Sport", "Gim a morning")
    manager.add_habit("Read the book", "10 страниц in day")
    print(f"\nВсего привычек: {len(manager.habits)}")
    print("Отмечаем выполнение...")
    manager.complete_habit(1)
    manager.complete_habit(1)
    manager.complete_habit(2)
    manager.complete_habit(999)
    for habit in manager.habits:
        print(f"Привычка: {habit.name} - {habit.description}. streak: {habit.streak}")