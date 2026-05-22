def save_student_to_file(student, filename="PYTHON_2.0.txt"):
    # сохраняет данные студента в файл
    with open(filename, 'w', encoding='utf-8') as f:
        # w - write (записать), r - read (прочесть)
        f.write(f"Имя:{student['name']}\n")
        f.write(f"Возраст:{student['age']}\n")
        f.write(f"Предметы:{','.join(student['subjects'])}\n")
        f.write(f"Оценки:{','.join(map(str, student['grades']))}\n")

        print(f"Данные сохранены в {filename}")


def load_from_file(filename="PYTHON_2.0.txt"):
    # загружает данные студента из файла
    student = {
        "name": "",
        "age": 0,
        "subjects": [],
        "grades": []
    }
    # try и except - по типу if и else
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()  # читаем все строки
    except FileNotFoundError:
        print('Файл не открывается, возникла ошибка')
        return student

    for line in lines:
        line = line.strip()

        if line.startswith("Имя:"):
            student['name'] = line.replace('Имя:', '').strip()
        elif line.startswith('Возраст:'):
            student['age'] = int(line.replace('Возраст:', '').strip())
        elif line.startswith('Предметы:'):
            subjects_str = line.replace('Предметы:', '').strip()
            if subjects_str:
                student['subjects'] = subjects_str.split(',')
        elif line.startswith('Оценки:'):
            grades_str = line.replace('Оценки:', '').strip()
            if grades_str:
                student['grades'] = [int(x) for x in grades_str.split(',')]
    print(f"Данные загружены из {filename}")
    return student


def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def get_status(average):
    if average >= 4.5:
        return "Отличник"
    elif average >= 4.0:
        return "Хорошист"
    elif average >= 3.0:
        return "Удовлетворительно"
    else:
        return "Неуспевающий"


def create_student():
    student = {
        "name": "",
        "age": 0,
        "subjects": [],
        "grades": []
    }

    print("\n--- СОЗДАНИЕ НОВОГО СТУДЕНТА ---")
    student["name"] = input("Введите имя студента: ").strip()

    # Безопасный ввод возраста
    while True:
        try:
            student["age"] = int(input("Введите возраст студента: "))
            if 16 <= student["age"] <= 60:  # разумные границы
                break
            else:
                print("Возраст должен быть от 16 до 60 лет")
        except ValueError:
            print("Введите число!")

    print("Студент создан")
    return student


def main():
    print("=== ПРОГРАММА 'СТУДЕНТ' ===")
    choice = input('Загрузить данные из файла? (да/нет): ').strip().lower()
    if choice == "да":
        student = load_from_file()
        if student['name'] == '':
            print("Создаю нового студента...")
            student = create_student()
    else:
        student = create_student()

    print("\n--- ДОБАВЛЕНИЕ ПРЕДМЕТОВ ---")
    student['subjects'] = []
    student['grades'] = []

    while True:
        subject = input("Введите предмет (или 'стоп' для завершения): ").strip()
        if subject.lower() == 'стоп':
            break
        if subject:
            student['subjects'].append(subject)

        while True:
            try:
                grade = int(input(f"Оценка за {subject}: "))
                if 2 <= grade <= 5:
                    student["grades"].append(grade)
                    print(f"Добавлен предмет: {subject} c оценкой {grade}")
                    break
                else:
                    print("Некорректно, введите заново от 2 до 5")
            except ValueError:
                print("Введите число!")

    average = calculate_average(student['grades'])
    status = get_status(average)
    print(f"Статус: {status}")

    # вывод
    print("============================")
    print("       ОТЧЁТ СТУДЕНТА       ")
    print("============================")
    print(f"Имя: {student['name']}")
    print(f"Возраст: {student['age']}")
    print("============================")
    print("ПРЕДМЕТЫ:")
    print("============================")
    print(f"Предмет: {student['subjects']}")
    print(f"Оценка: {student['grades']}")
    print("============================")

    print("ПРЕДМЕТЫ И ОЦЕНКИ")
    if student['subjects']:
        for i in range(len(student['subjects'])):
            subject = student['subjects'][i]
            # безопасно получаем оценку
            grade = student['grades'][i] if i < len(student['grades']) else 'нет оценки'
            print(f' {subject}: {grade}')
    else:
        print(" Нет предметов")
    print("=" * 40)

    if student['grades']:
        if len(student['subjects']) != len(student['grades']):
            print('Oшибка: количество предметов не соответствует количеству оценок')
        else:
            max_grade = max(student["grades"])
            index_max = student["grades"].index(max_grade)
            best_subject = student["subjects"][index_max]
            print(f"Самый успешный предмет: {best_subject}({max_grade})")
    else:
        print("Нет оценок для анализа")

    save_choice = input("\nСохранить данные в файл? (да/нет):").strip().lower()
    if save_choice == "да":
        save_student_to_file(student)
        print("Данные сохранены!")

    print("=== ПРОГРАММА ЗАВЕРШЕНА ===")


if __name__ == "__main__":
    main()