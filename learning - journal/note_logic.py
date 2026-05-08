def add_note(notes, text):
    new_id = max((n['id'] for n in notes), default=0) + 1
    notes.append({'id': new_id, 'text': text, 'done': False})
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
