import requests
import datetime
import aiogram
from config import tg_bot_token, open_weather_token
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Enter city name")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        wind = data["wind"]["speed"]

        await message.reply(
            f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f'Weather in {city}\nTemperature {cur_weather}\nHumidity {humidity}\nWind {wind}')
    except:
        await message.reply("Check city name")


if __name__ == '__main__':
    executor.start_polling(dp)
