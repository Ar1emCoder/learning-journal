import json
import os

FILE_NAME = "notes.json"

def load_notes():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4, ensure_ascii=False)

def add_note(notes):
    text = input("Текст заметки: ").strip()
    if not text:
        print("❌ Текст не может быть пустым")
        return
    new_id = max((n["id"] for n in notes), default=0) + 1
    notes.append({"id": new_id, "text": text, "done": False})
    save_notes(notes)
    print(f"✅ Заметка {new_id} добавлена")

def list_notes(notes):
    if not notes:
        print("📭 Заметок нет")
        return
    for n in notes:
        status = "✓" if n["done"] else "◻"
        print(f"{n['id']}. [{status}] {n['text']}")

def delete_note(notes):
    list_notes(notes)
    try:
        idx = int(input("Номер заметки для удаления: "))
        for i, n in enumerate(notes):
            if n["id"] == idx:
                notes.pop(i)
                save_notes(notes)
                print(f"🗑 Заметка {idx} удалена")
                return
        print("❌ Заметка не найдена")
    except ValueError:
        print("❌ Введите число")

def toggle_done(notes):
    list_notes(notes)
    try:
        idx = int(input("Номер заметки для отметки выполнения: "))
        for n in notes:
            if n["id"] == idx:
                n["done"] = not n["done"]
                save_notes(notes)
                print(f"✅ Статус заметки {idx} изменён")
                return
        print("❌ Заметка не найдена")
    except ValueError:
        print("❌ Введите число")

def main():
    notes = load_notes()
    while True:
        print("\n📌 МЕНЮ")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Удалить заметку")
        print("4. Отметить выполненной")
        print("5. Выйти")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            add_note(notes)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            toggle_done(notes)
        elif choice == "5":
            print("👋 До встречи!")
            break
        else:
            print("❌ Неверный ввод")

if __name__ == "__main__":
    main()

