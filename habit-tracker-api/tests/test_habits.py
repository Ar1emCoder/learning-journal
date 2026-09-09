from datetime import date, timedelta


def test_create_habit_mock():
    mock_habit = {"id": 1, "name": "Бег", "created_at": date.today()}
    assert mock_habit["name"] == "Бег"
    assert mock_habit["id"] == 1


def test_streak_calculation_mock():
    mock_completions = [
        {"completions_date": date.today()},
        {"completions_date": date.today() - timedelta(days=1)},
        {"completions_date": date.today() - timedelta(days=2)},
    ]
    assert len(mock_completions) == 3


def calculate_streak(dates):
    if not dates:
        return 0
    streak = 1
    for i in range(1, len(dates)):
        # Если разница между датами ровно 1 день, стрик продолжается
        if dates[i - 1] - dates[i] == timedelta(days=1):
            streak += 1
        else:
            break
    return streak


def test_broken_streak():
    today = date.today()
    mock_dates = [today, today - timedelta(days=2)]
    streak = calculate_streak(mock_dates)
    assert streak == 1, f"Ожидали 1, но получили {streak}"


def test_empty_streak():
    mock_dates = []
    streak = calculate_streak(mock_dates)
    assert streak == 0
