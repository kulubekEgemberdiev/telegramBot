import requests
from tokens import open_weather, bot_token
import datetime
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=bot_token)
disp = Dispatcher(bot)

@disp.message_handler()
async def get_weather(msg):
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={msg.text}&appid={open_weather}&units=metric&lang=ru")
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
        await msg.reply(f"📆    Текущая дата: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}.\n\n"
                        f"🏘️    Название города: {city_name}.\n\n"
              f"🔆    Описание: {description}.\n\n"
              f"🌡️    Температура: {current_temp}°C.\n\n"
              f"🏋️    Атмосферное давление: {pressure} мм.рт.ст.\n\n"
              f"💦    Влажность воздуха: {humidity}%.\n\n"
              f"🌬️    Скорость ветра: {wind_speed} м/с.\n\n"
              f"🌏    Код страны: {country}.\n\n"
              f"🌞    Восход солнца: {sunrise}.\n\n"
              f"🌚    Закат солнца: {sunset}.\n\n"
              f"⏳    Длительность дня: {sunset - sunrise}")
    except Exception as ex:
        await msg.reply("Проверьте название города!")

@disp.message_handler(commands=["start"])
async def start(msg):
    await msg.reply("Привет! Напиши название города.")





if __name__ == '__main__':
    executor.start_polling(disp)
