import requests
from tokens import open_weather
import datetime


def get_weather(city, open_weather):
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather}&units=metric&lang=ru")
        data = req.json()
        city_name = data["name"]
        description = data["weather"][0]["description"]
        current_temp = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        country = data["sys"]["country"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        print(f"Название города: {city_name}.\n"
              f"Описание: {description}.\n"
              f"Температура: {current_temp}°C.\n"
              f"Атмосферное давление: {pressure} мм.рт.ст.\n"
              f"Влажность воздуха: {humidity}%.\n"
              f"Скорость ветра: {wind_speed} м/с.\n"
              f"Код страны: {country}.\n"
              f"Восход солнца: {sunrise}.\n"
              f"Закат солнца: {sunset}.")
    except Exception as ex:
        print("Проверьте название города!")


def main():
    city = input("Напишите название города: ")
    get_weather(city, open_weather)


if __name__ == '__main__':
    main()
