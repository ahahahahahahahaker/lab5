import requests
import json
from translate import Translator


translator = Translator(from_lang="English", to_lang="russian")
url = "https://rickandmortyapi.com/api/character/5"
api_key = '6edbef19306b0194a04f248f0bc6921c'
city = 'Saint Petersburg'
url1 = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

try:
    response = requests.get(url)
    data = response.json()

    if "name" in data:
        character_name = translator.translate(data["name"])
        species = translator.translate(data["species"])
        status = translator.translate(data["status"])

        print(f"Персонаж: {character_name}")
        print(f"Вид: {species}")
        print(f"Статус: {status}")

    else:
        print("Данные не найдены.")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")

except json.JSONDecodeError as e:
    print(f"Ошибка при декодировании JSON: {e}")


try:
    response = requests.get(url1)
    data = response.json()

    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    print(f'Погода в {city}: {weather_description}')
    print(f'Влажность: {humidity}%')
    print(f'Давление: {pressure} гПа')

except requests.exceptions.RequestException as e:
    print(f'Ошибка при выполнении запроса: {e}')
