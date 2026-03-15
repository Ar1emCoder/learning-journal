# import json
# import os
from flask import Flask, render_template, url_for, redirect, request
from datetime import date, datetime, timedelta
from database import get_all_habits, init_bd, add_habit_to_db, update_habit_in_db, delete_habit_from_db
import sys
import os
sys.path.append(os.path.dirname(__file__))

app = Flask(__name__)
init_bd()


# def load_habits():
#     """Загружает привычки из JSON файла"""
#     with open(JSON_PATH, 'r', encoding='utf-8') as f:
#         return json.load(f)

# def save_habits(habits):
#     """Сохраняет привычки в JSON файл"""
#     with open(JSON_PATH, 'w', encoding='utf-8') as f:
#         json.dump(habits, f, ensure_ascii=False, indent=2)

def calculate_new_streak(last_completed, current_streak):
    ''' Принимает дату последнего выполнения и текущий streak. '''
    today = date.today()
    last = datetime.strptime(last_completed, '%Y-%m-%d').date()

    if last == today:
        if current_streak == 0:
            return 1, True
        else:
            return current_streak, False
    elif last == today - timedelta(days=1):
        return current_streak + 1, True
    else:
        return 1, True

@app.route('/')
def index():
    """Главная страница со списком привычек"""
    habits = get_all_habits()
    return render_template('index.html', habits=habits)


@app.route('/complete/<int:habit_id>', methods=['POST'])
def complete(habit_id):
    """Отмечает привычку как выполненную"""
    habits = get_all_habits()

    # Ищем привычку по id, а не по индексу
    for habit in habits:
        if habit.get('id') == habit_id:
            new_streak, should_update = calculate_new_streak(habit['last_completed'], habit['streak'])
            # habit['streak'] = habit.get('streak', 0) + 1

            if should_update:
                update_habit_in_db(habit_id, new_streak, date.today().isoformat())
            else:
                print("Уже выполнено сегодня")
            break
    # save_habits(habits)
    return redirect(url_for('index'))


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']

    add_habit_to_db(name)

    return redirect(url_for('index'))
    # name = request.form['name']
    # habits = get_all_habits()
    # existing_ids = [habit['id'] for habit in habits]
    # if existing_ids:
    #     new_id = max(existing_ids) + 1
    # else:
    #     new_id = 1
    # today = date.today().isoformat()
    # new_habit = {
    #     'id': new_id,
    #     'name': name,
    #     'streak': 0,
    #     'last_completed': today
    # }
    # habits.append(new_habit)
    # save_habits(habits)
    # return redirect(url_for('index')) # перенаправить на главную

@app.route('/delete/<int:habit_id>', methods=['POST'])
def delete(habit_id):
    # habits = get_all_habits()
    delete_habit_from_db(habit_id)
    # for i, habit in enumerate(habits):
    #     if habit['id'] == habit_id:
    #         del habits[i]
    #         break
    #
    # save_habits(habits)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)