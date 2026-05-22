import json
from datetime import datetime

class Note:
    def __init__(self, title, content, tags):
        self.title = title
        self.content = content
        self.tags = tags
        self.id = None
        self.created_at = datetime.now()
        self.updated_at = None

    def updated(self, new_title=None, new_content=None, new_tags=None):
        if new_title: self.title = new_title
        if new_content: self.content = new_content
        if new_tags: self.tags = new_tags
        self.updated_at = datetime.now()
        print(f"Данные изменены на: {self.title} - c тегом [{self.tags}]")

    def get_preview(self, length=50):
        return self.content[:length] + "..."

class NotesManager:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = []
        self.next_id = 1
        self.load()  # загрузить при создании

    def add_note(self, title, content, tags):
        note = Note(title, content, tags)
        note.id = self.next_id
        self.notes.append(note)
        self.next_id += 1
        self.save()

    def delete_note(self, note_id):
        for i, note in enumerate(self.notes):
            if note.id == note_id:
                self.notes.pop(i)
                self.save()
                print(f"Заметка {note_id} удалена")
                return True
        print(f"Заметка с ID {note_id} не найдена")
        return False

    def save(self):
        try:
            data = []
            for note in self.notes:
                # Для одной заметки
                note_dict = {
                    "id": note.id,
                    "title": note.title,
                    "content": note.content,
                    "tags": note.tags,
                    "created_at": note.created_at.isoformat(),  # ← СТРОКА
                    "updated_at": note.updated_at.isoformat() if note.updated_at else None  # ← СТРОКА или None
                }
                data.append(note_dict)

            with open(self.filename, 'w', encoding = 'utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Сохранено {len(data)} заметок")
        except Exception as e:
            print(f"Ошибка сохранения: {e}")

    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.notes = []
            for note_data in data:
                note = Note(
                    title=note_data['title'],
                    content=note_data['content'],
                    tags=note_data['tags']
                )
                note.id = note_data['id']
                note.created_at = datetime.fromisoformat(note_data['created_at'])
                if note_data.get('updated_at'):
                    note.updated_at = datetime.fromisoformat(note_data['updated_at'])
                self.notes.append(note)

            if self.notes:
                self.next_id = max(note.id for note in self.notes) + 1
            else:
                self.next_id = 1

            print(f"Загружено {len(self.notes)} заметок")

        except FileNotFoundError:
            print(f"Файл {self.filename} не найден, создаём новый")
            self.notes = []
            self.next_id = 1
        except json.JSONDecodeError:
            print(f"Файл {self.filename} повреждён, начинаем с чистого листа")
            self.notes = []
            self.next_id = 1


if __name__ == "__main__":
    print("=== ТЕСТ 1: СОЗДАНИЕ И СОХРАНЕНИЕ ===")
    manager = NotesManager()
    manager.add_note("Тест", "Это тестовая заметка", ["тест", "пример"])
    manager.add_note("Вторая", "Ещё одна заметка", ["важно"])

    print(f"Заметок в памяти: {len(manager.notes)}")

    print("\n=== ТЕСТ 2: ЗАГРУЗКА ===")
    manager2 = NotesManager()
    print(f"Загружено заметок: {len(manager2.notes)}")

    if manager2.notes:
        note = manager2.notes[0]
        print(f"Первая заметка: {note.title}")
        print(f"Preview: {note.get_preview(20)}")
        print(f"Создана: {note.created_at}")

    print("\n=== ТЕСТ 3: УДАЛЕНИЕ ===")
    if manager2.notes:
        manager2.delete_note(manager2.notes[0].id)
        print(f"После удаления: {len(manager2.notes)} заметок")