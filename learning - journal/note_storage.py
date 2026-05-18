import json
import os

FILE_NAME = "notes.json"

def load_notes():
    if not os.path.exists(FILE_NAME):
        return []
    else:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            notes = json.load(f)
            for note in notes:
                if "tags" not in note:
                    note["tags"] = []
            return notes

def save_notes(notes):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4, ensure_ascii=False)