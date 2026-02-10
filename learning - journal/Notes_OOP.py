import json
from datetime import datetime
from json import JSONDecodeError

class Note:
    def __init__(self, title, content, tags):
        self.title = title
        self.content = content
        self.tags = tags
        self.id = None
        self.created_at = datetime.now()
        self.update_at = None

    def update(self, new_title=None, new_content=None, new_tags=None):
        if new_title: self.title = new_title
        if new_content: self.content = new_content
        if new_tags: self.tags = new_tags
        self.update_at = datetime.now()
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
        print('временно не работает')
        # # Для одной заметки
        # note_dict = {
        #     "id": note.id,
        #     "title": note.title,
        #     "content": note.content,
        #     "tags": note.tags,
        #     "created_at": note.created_at,
        #     "updated_at": note.update_at
        # }
        # # Для всех заметок
        # notes_data = []
        # for note in self.notes:
        #     note_dict = {...}
        #     notes_data.append(note_dict)
        #
        # with open(self.filename, 'w', encoding = 'utf-8') as f:
        #     json.dump(notes_data, f, ensure_ascii=False, indent=2)

    def load(self):
        print('пока не работает')
        self.notes = []
        # try:
        #     with open(self.filename, 'r', encoding='utf-8') as f:
        #         data = json.load(f)
        # except FileNotFoundError:
        #     print(f"Файл {self.filename} не найден, начинаем с чистого листа")
        # except JSONDecodeError:
        #     print(f"Файл {self.filename} повреждён")
        #     return
        #
        # for note_data in data:
        #     note_data = Note(
        #         title=note_data['title'],
        #         content=note_data['content'],
        #         tags= note_data['tags']
        #     )
        #     note.id = note_data['id']
        #     note.created_at = note_data['created_at']
        #     self.notes.append(note)
        #
        # if self.notes:
        #     self.next_id = max(note.id for note in self.notes) + 1
        # else:
        #     self.next_id = 1

if __name__ == "__main__":
    manager = NotesManager()
    # добавление
    manager.add_note("Тест", "Это тестовая заметка", ["тест", "пример"])

    print(f"Заметок: {len(manager.notes)}")
    if manager.notes:
        note = manager.notes[0]
        print(f"Первая заметка: {note.title}")
        print(f"Preview: {note.get_preview()}")

    # удаление
    if manager.notes:
        manager.delete_note(manager.notes[0].id)
        print(f"После удаления: {len(manager.notes)} заметок")





