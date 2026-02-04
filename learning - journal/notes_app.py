import json
from datetime import datetime
from json import JSONDecodeError

notes = []

def load_from_json():
    # пробуем открыть файл
    try:
        with open('notes.json', 'r', encoding='utf-8') as f:
            data = json.load(f) # загружаем json
            print(f'Загружено {len(data)} заметок')
            return data
    except FileNotFoundError:
        print('Файл не найден, начинаем с пустого списка')
        return []
    except JSONDecodeError:
        print('В файле мусор, перезапишите данные!')
        return []

def save_to_json(filename="notes.json"):
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=2)
        print(f"Данные сохранены в {filename}")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении {e}")
        return False

def create_note():
    # Заголовок и текст
    title = input("Введите заголовок: ").strip()
    content = input("Введите текст заметки: ").strip()

    # Обработка тегов
    tags_input = input("Введите теги (через запятую):").strip()
    # tags_list = tags_input.split(",") # разделение строки по запятой
    # clean_tags = []
    # for tag in tags_list:
    # clean_tag = tag.split() # Убираем пробелы в начале и конце
    # if clean_tags:
    #     clean_tags.append(clean_tag)
    tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

    note = {
        "id": get_next_id(),
        "title": title,
        "content": content,
        "tags": tags,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    notes.append(note)
    print(f"Заметка создана! Теги: {tags}")
    return note

def get_next_id():
    if not notes:
        return 1
    max_id = max(note['id'] for note in notes)
    return max_id + 1

def show_all_notes():
    if not notes:
        print("Пока нет заметок!")
    else:
        for note in notes:
            print(f"ID {note['id']}: {note['title']}")
            print(f"Теги: {','.join(note['tags'])}")
            print(f"Дата: {note['created_at']}")
            print(f"Текст: {note['content']}")
            print('-'*40)

def main():
    global notes
    notes = load_from_json()
    while True:
        print(f"1. Показать все заметки")
        print(f"2. Добавить заметку")
        print(f"3. Выйти")
        # print(f"4. Сохранить заметки в файл")

        choice = input("Введите действие (1-3): ")

        if choice == '1':
            show_all_notes()
        elif choice == '2':
            create_note()
        elif choice == '3':
            print("Выход из программы")
            save_to_json()
            break
        # elif choice == '4':
        #     save_to_json()
        else:
            print("Неверный выбор! Введите число от 1 до 3")

if __name__ == "__main__":
    main()