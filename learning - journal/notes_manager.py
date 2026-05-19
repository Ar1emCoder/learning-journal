from note_storage import load_notes, save_notes
from note_logic import add_note, delete_note, toggle_done, search_notes, sort_notes_by_date, search_by_tag

def main():
    notes = load_notes()
    while True:
        print("\n📌 МЕНЮ")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Удалить заметку")
        print("4. Отметить выполненной")
        print("5. Найти заметку по 'особенному' слову")
        print("6. Показать заметки (новые -> старые)")
        print("7. Показать заметки (старые -> новые)")
        print("8. Найти заметки по тегу")
        print("9. Выйти")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            text = input("Текст заметки: ").strip()
            if text:
                notes = add_note(notes, text)  # ← теперь передаём text
                save_notes(notes)
            else:
                print("Текст не может быть пустым")
        elif choice == "2":
            for n in notes:
                status = "✓" if n["done"] else "◻"
                print(f"{n['id']}. [{status}] {n['text']}")
                tags_str = ", ".join(n["tags"]) if n["tags"] else "без тегов"
                print(f"   Теги: {tags_str}")
        elif choice == "3":
            try:
                note_id = int(input("Номер заметки: "))
                notes = delete_note(notes, note_id)
                save_notes(notes)
            except ValueError:
                print("Ошибка! Введите число")
        elif choice == "4":
            try:
                note_id = int(input("Номер заметки: "))
                notes = toggle_done(notes, note_id)
                save_notes(notes)
            except ValueError:
                print("Ошибка! Введите число")
        elif choice == "5":
            keyword = input("Введите ключевое слово: ").strip()
            found = search_notes(notes,keyword)
            if not found:
                print("Ничего не найдено.")
            else:
                print("Результаты поиска:")
                for n in found:
                    status = "✓" if n["done"] else "◻"
                    print(f"{n['id']}. [{status}] {n['text']}")
        elif choice == "6":
            sorted_notes= sort_notes_by_date(notes, reverse=True)
            for n in sorted_notes:
                status = "✓" if n["done"] else "◻"
                print(f"{n['id']}. [{status}] {n['text']}  [{n['created_at']}]")
        elif choice == "7":
            sorted_notes = sort_notes_by_date(notes, reverse=False)
            for n in sorted_notes:
                status = "✓" if n["done"] else "◻"
                print(f"{n['id']}. [{status}] {n['text']}  [{n['created_at']}]")
        elif choice == "8":
            tags = input("Введите тег: ").strip()
            found = search_by_tag(notes, tags)
            if not found:
                print("Нет заметок с таким тегом")
            else:
                print("Результаты поиска по тегу: ")
                for n in found:
                    status = "✓" if n["done"] else "◻"
                    print(f"{n['id']}. [{status}] {n['text']}")
                    print(f"   Теги: {', '.join(n['tags']) if n['tags'] else 'без тегов'}")
        elif choice == "9":
            print("👋 До встречи!")
            break
        else:
            print("❌ Неверный ввод")

if __name__ == "__main__":
    main()

