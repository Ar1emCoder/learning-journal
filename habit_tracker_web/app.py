import json
from flask import Flask, render_template

app = Flask(__name__)

def load_habits():
    with open('habit_tracker.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    habits = load_habits()
    return render_template('index.html', habits=habits)

if __name__ == "__main__":
    app.run(debug=True)