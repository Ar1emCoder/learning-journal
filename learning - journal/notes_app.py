import json
from datetime import datetime

notes = []

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
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "tags": tags,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    notes.append(note)
    print(f"Заметка создана! Теги: {tags}")
    return note

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
    while True:
        print(f"1. Показать все заметки")
        print(f"2. Добавить заметку")
        print(f"3. Выйти")

        choice = input("Введите действие (1-3): ")

        if choice == '1':
            show_all_notes()
        elif choice == '2':
            create_note()
        elif choice == '3':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор! Введите число от 1 до 3")

if __name__ == "__main__":
    main()