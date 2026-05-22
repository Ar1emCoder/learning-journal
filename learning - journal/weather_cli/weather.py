import reguests

def get_coordinates(city):
    url = f"https//:geocoding-api.open-meteo.com/v1/search?name{city}&count=1"
    response = reguests.get(url)  # отправляем get- запрос по url
    data = response.json()  # превращаем ответ в словарь
    lat = data



def get_weather(lat, lon):
    pass
