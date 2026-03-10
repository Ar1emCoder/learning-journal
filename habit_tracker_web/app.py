import json
import os
from flask import Flask, render_template, url_for, redirect, request
from datetime import date, datetime, timedelta
from database import get_all_habits, init_bd, add_habit_to_db

app = Flask(__name__)
init_bd()

# Указываем полный путь к файлу
JSON_PATH = os.path.join(os.path.dirname(__file__), 'habit_tracker.json')


def load_habits():
    """Загружает привычки из JSON файла"""
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_habits(habits):
    """Сохраняет привычки в JSON файл"""
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(habits, f, ensure_ascii=False, indent=2)


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
            # habit['streak'] = habit.get('streak', 0) + 1
            today = date.today()
            last = datetime.strptime(habit['last_completed'], '%Y-%m-%d').date()
            delta = today - last
            if last == today:
                if habit['streak'] == 0:
                    habit['streak'] = 1
                else:
                    print('Цель выполнена сегодня, возвращайтесь завтра!')
                    break
            elif last == today - timedelta(days=1):
                habit['streak'] += 1
                habit['last_completed'] = today.isoformat()
                break
            else:
                habit['streak'] = 1
                habit['last_completed'] = today.isoformat()
                print(f"Увы, вы пропустили {delta} дней")
                break


    save_habits(habits)
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']

    add_habit_to_db()

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
    habits = get_all_habits()
    for i, habit in enumerate(habits):
        if habit['id'] == habit_id:
            del habits[i]
            break

    save_habits(habits)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)