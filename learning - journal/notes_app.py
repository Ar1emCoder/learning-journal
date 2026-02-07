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
    tags_input = input("Введите теги (через запятую): ").strip()
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

def delete_note():
    if not notes:
        print('Нет заметок для удаления!')
        return

    show_all_notes()
    try:
        delete_id = int(input("Введите ID заметки, для удаления: "))
    except ValueError:
        print("Ошибка! Введите число.")
        return
    for i, note in enumerate(notes):
        if delete_id == note['id']:
            removed_note = notes.pop(i)
            print(f"Заметка '{note['title']}' {note['id']} удалена")
            return
    print(f"Заметка с ID {delete_id} не найдена!")

def edit_note():
    if not notes:
        print('Нет заметок для редактирования!')
        return
    show_all_notes()
    try:
        id_input = int(input("Введите ID заметки для редактирования: "))
    except ValueError:
        print("Введите число!")
        return

    for note in notes:
        if id_input == note['id']:
            current_title = note['title']
            current_content =  note['content']
            current_tags = note['tags']

            new_title = input(f"Введите новый заголовок заместо [{current_title}](Enter - оставить прежним): ")
            if not new_title:
                new_title = current_title
            preview = current_content[:30] + ("..." if len(current_content) > 30 else "")
            new_content = input(f"Введите новый текст заместо [{preview}] (Enter - оставить прежним): ").strip()
            if not new_content:
                new_content = current_content
            new_tags = input(f"Введите новый тег заместо [{current_tags}] (Enter - оставить прежним): ")
            if new_tags:
                new_tags = [tag.strip() for tag in new_tags.split(",") if tag.strip()]
            else:
                new_tags = current_tags

            note['title'] = new_title
            note['content'] = new_content
            note['tags'] = new_tags
            note['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M")

            print(f"Заметка ID {note['id']} обновлена")
            return
    print(f"Заметка {id_input} не найдена!")

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

def search_notes():
    if not notes:
        print("Нет заметок для поиска!")
        return
    search = input("Введите слово для поиска: ").lower().strip()
    for note in notes:
        if search in note['title'].lower():
            print(f"Совпадение в названии заметки с ID: {note['id']} ")
            return
        if search in note['content'].lower():
            print(f"Совпадение в тексте заметки с ID: {note['id']} ")
            return
        for tag in note['tags']:
            if search in tag.lower():
                print(f"Совпадение в теге заметки с ID: {note['id']} ")
                return
    print(f"Слово {search} нигде не найдено!")
    return


def show_stats():
    if not notes:
        print("Нет заметок вовсе")
        return
    cnt_notes = len(notes)
    summa = 0
    for note in notes:
        summa += len(note['tags'])

    print("="*40)
    print("\n=== СТАТУС ===")
    print(f'Количество заметок = {cnt_notes}')
    print(f'Количество тегов = {summa}')
    print("="*40)


def main():
    global notes
    notes = load_from_json()
    while True:
        print(f"1. Показать все заметки")
        print(f"2. Добавить заметку")
        print(f"3. Удалить заметку")
        print(f"4. Редактировать заметку")
        print(f"5. Выйти")
        print(f"6. Показать статус")
        print(f"7. Поиск по слову (заголовок, текст, тег)")

        choice = input("Введите действие (1-7): ")

        if choice == '1':
            show_all_notes()
        elif choice == '2':
            create_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            edit_note()
        elif choice == '5':
            print("Выход из программы")
            save_to_json()
            break
        elif choice == '6':
            show_stats()
        elif choice == '7':
            search_notes()
        else:
            print("Неверный выбор! Введите число от 1 до 7")

if __name__ == "__main__":
    main()