import json
from datetime import datetime, timedelta
from pydoc import describe


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
        self.save()


    def complete_habit(self, habit_id):
        # Получаем сегодняшнюю дату (без времени)    #     today = datetime.now().date()
        today = datetime.now().date()
        # Ищем привычку по ID
        for habit in self.habits:
            if habit.id == habit_id:
                # Если привычка никогда не выполнялась
                if habit.last_completed is None:
                    habit.streak = 1
                else:
                    # Преобразуем last_completed в дату (если это datetime)
                    last = habit.last_completed
                    if isinstance(last, datetime):
                        last = last.date()

                    # Сравниваем с сегодня и вчера
                    if last == today:
                        print(f"Привычка '{habit.name}' уже выполнена сегодня!")
                        return
                    elif last == today - timedelta(days=1):
                        habit.streak += 1
                    else:
                        habit.streak = 1

                # Обновляем дату последнего выполнения
                habit.last_completed = today
                print(f"Привычка '{habit.name}' выполнена! Текущий streak: {habit.streak}")
                return

        # Если привычка не найдена
        print(f"Привычка с ID {habit_id} не найдена")
        self.save()

    def save(self):
        try:
            data = []
            for habit in self.habits:
                data_dict = {
                    "id": habit.id,
                    "name": habit.name,
                    "description": habit.description,
                    "created_at": habit.created_at.isoformat(),
                    "last_completed": habit.last_completed.isoformat() if habit.last_completed else None,
                    "streak": habit.streak
                }
                data.append(data_dict)
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Сохранено {len(data)} привычек")
        except Exception as e:
            print(f"Ошибка сохранения: {e}")

            # with open(self.filename, 'w', encoding='utf-8') as f:
            #     data = json.load(f)
            #     self.habits = []
            #     for item in data:
            #         habit = Habit(
            #             name = item['name'],
            #             description  = item['description']
            #             # streak = item['streak']
            #         )
            #         habit.id = item['id']
            #         habit.streak = item['streak']
            #         self.habits.append(habit)
            #
            #     if self.habits:
            #         self.next_id = max(t.id for t in self.habits) + 1
            #     else:
            #         self.next_id = 1
            #     print(f"Загружено {len(self.habits)} транзакций")
        # except FileNotFoundError:
        #     print("Файл не найден, начинаем с начала!")
        #     self.habits = []
        #     self.next_id = 1
        # except Exception as e:
        #     print(f"Ошибка загрузки: {e}")

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