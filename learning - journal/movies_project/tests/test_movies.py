import pytest
import asyncio
from fastapi.testclient import TestClient
# импорты приложения и создания бд
from movies_api import app
from init_movies_db import init_db

# Создаем "работника сцены" (фикстуру)
# scope = "session" означает: запустить 1 раз перед всеми тестами
# autouse = True означает: запустить автоматически, нам не нужно вызывать его вручную
@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    asyncio.run(init_db())

# создаем "робота-тестировщика"
client = TestClient(app)

# Пишем тест 1!
def test_get_all_movies():
    response = client.get("/movies/") # робот делает get-запрос по адресу /movies/

    #Проверка 1: Мы ожидаем, что сервер ответит кодом 200 (ок)
    assert response.status_code == 200 # (assert - утверждать)

    #Проверка 2: Мы ожидаем, что в ответе придет список (list), даже если он пока пустой []
    assert isinstance(response.json(), list)

# Пишем тест 2!
def test_get_movie_not_found():
    # Робот запрашивает фильм с заведомо несуществующим айди
    response = client.get("/movies/99999")

    #Проверка 1: Мы ожидаем код 404 (Not Found)
    assert response.status_code == 404

    #Проверка 2: Мы проверяем, что текст ошибки именно такой, как мы написали
    assert response.json()["detail"] == "Фильм не найден!"