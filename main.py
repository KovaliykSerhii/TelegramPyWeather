import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        wind = data["wind"]["speed"]

        print(
            f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f'Weather in {city}\nTemperature {cur_weather}\nHumidity {humidity}\nWind {wind}')

    except Exception as ex:
        print(ex)
        print("Check city name")


def main():
    city = input("Enter city name:")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
