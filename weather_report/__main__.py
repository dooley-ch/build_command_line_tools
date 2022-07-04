# *******************************************************************************************
#  File:  __main__.py
#
#  Created: 04-07-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  04-07-2022: Initial version
#
# *******************************************************************************************

import datetime
import click
import inquirer
import pyfiglet
import requests
from tabulate import tabulate
from yaspin import yaspin

_API_KEY = '6446a5397a0c3f38012e657b86f62be2'


def minMaxTemp(data, unit):
    return "{}{} to {}{}".format(round(data["temp"]["min"]), units[unit], round(data["temp"]["max"]), units[unit])


units = dict(
    metric="°C",
    imperial="°F"
)


def weatherDataToTable(data, unit):
    day = datetime.datetime.fromtimestamp(data['dt'])
    return [f"{day:%d.%m.%Y}", minMaxTemp(data, unit)]


def fetchWeeklyWeather(lon, lat, unit):
    params = dict(
        lon=lon,
        lat=lat,
        units=unit,
        exclude="current,hourly,minutely,alerts",
        appid=_API_KEY
    )
    API_URL = "http://api.openweathermap.org/data/2.5/onecall"
    response = requests.get(url=API_URL, params=params)
    return response.json()["daily"]


@yaspin(text="Fetching weather data...")
def fetch_weather(city: str, country: str, unit: str):
    params = dict(
        q=f"{city},{country}",
        units=unit,
        appid=_API_KEY
    )
    API_URL = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url=API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        lon = data['coord']["lon"]
        lat = data['coord']["lat"]
    return fetchWeeklyWeather(lon, lat, unit)


@click.command()
@click.option('--city', prompt='Enter the city: ', help='City for which weather report is required')
@click.option('--country', prompt='Enter the country: ', help='The country where the city is located')
def main(city: str, country: str) -> None:
    """
    This program reports the weather for a requested city
    """
    unit = 'metric'  # inquirer.list_input("Metric or imperial?", choices=['metric', 'imperial'])
    weatherData = fetch_weather(city, country, unit)
    print(pyfiglet.figlet_format(minMaxTemp(weatherData[0], unit)))
    tabledata = map(lambda x: weatherDataToTable(x, unit), weatherData)
    headers = ["Date", "Temperature range"]
    print(tabulate(tabledata, headers, tablefmt="fancy_grid"))


if __name__ == '__main__':
    main()
