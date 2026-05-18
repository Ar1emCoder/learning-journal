from datetime import datetime

def add_note(notes, text):
    new_id = max((n['id'] for n in notes), default=0) + 1
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tags = []
    text_tags = input('Введите теги (через запятую) -> Enter (если не хотите): ').strip()
    if text_tags:
        tags = [t.strip().lower() for t in text_tags.split(",")]
    else:
        tags = []
    notes.append({'id': new_id, 'text': text, 'done': False, 'created_at': created_at, 'tags': tags})
    return notes

def delete_note(notes, note_id):
    return [n for n in notes if n['id'] != note_id]

def toggle_done(notes, note_id):
    for n in notes:
        if n['id'] == note_id:
            n['done'] = not n['done']
        return notes

def search_notes(notes, keyword):
    result = []
    for n in notes:
        if keyword.lower() in n['text'].lower():
            result.append(n)
    return result

def sort_notes_by_date(notes, reverse=False): # True - новые сверху, False - старые сверху
    return sorted(notes, key=lambda x: x['created_at'], reverse=reverse)