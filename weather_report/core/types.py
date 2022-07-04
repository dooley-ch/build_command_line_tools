# *******************************************************************************************
#  File:  types.py
#
#  Created: 04-07-2022
#
#  History:
#  04-07-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['UnitOfMeasure', 'Location', 'Locations', 'WeatherData', 'Weather', 'CurrentWeather', 'DailyWeather']

import enum
import typing
import attrs
import pendulum


def _from_timestamp_to_date(value: int) -> pendulum.DateTime:
    """
    This function is used by attrs to convert timestamp values to DateTime instances
    by some DTO classes via a converter attribute on the field definition
    """
    return pendulum.from_timestamp(value)


class UnitOfMeasure(str, enum.Enum):
    """
    This enum represents the reporting unit of measure
    """
    Standard = 'standard'
    Metric = 'metric'
    Imperial = 'imperial'


class Location(typing.NamedTuple):
    """
    This class holds the geographic location of a city
    """
    city: str
    state: str
    country: str
    longitude: float
    latitude: float

    def __repr__(self):
        return f"{self.city}, {self.state}, {self.country} ({self.latitude}, {self.longitude})"


Locations = typing.NewType('Locations', list[Location])


class Temperature(typing.TypedDict):
    """
    This class represents the data structure returned by the OpenWeatherMap site for temperature
    entries
    """
    day: float
    min: float
    max: float
    night: float
    eve: float
    morn: float


class FeelsLike(typing.TypedDict):
    """
    This class represents the data structure returned by the OpenWeatherMap site for 'feels like'
    entries
    """
    day: float
    night: float
    eve: float
    morn: float


@attrs.frozen
class Weather:
    """
    This class represents the data structure returned by the OpenWeatherMap site for weather
    entries
    """
    id: int
    main: str
    description: str
    icon: str


@attrs.frozen()
class CurrentWeather:
    """
    This class represents the data structure returned by the OpenWeatherMap site for current weather entry
    """
    dt: pendulum.DateTime = attrs.field(converter=_from_timestamp_to_date)
    sunrise: pendulum.DateTime = attrs.field(converter=_from_timestamp_to_date)
    sunset: pendulum.DateTime = attrs.field(converter=_from_timestamp_to_date)
    pressure: int
    humidity: int
    dew_point: int
    uvi: float
    clouds: int
    visibility: int
    wind_speed: float
    wind_deg: float
    wind_gust: float
    weather: list[Weather] = attrs.Factory(dict)
    temp: Temperature = attrs.Factory(dict)
    feels_like: FeelsLike = attrs.Factory(dict)


@attrs.frozen
class DailyWeather:
    """
    This class represents the data structure returned by the OpenWeatherMap site for daily weather
    entries
    """
    dt: pendulum.DateTime = attrs.field(converter=_from_timestamp_to_date)
    sunrise: pendulum.DateTime = attrs.field(converter=_from_timestamp_to_date)
    sunset: pendulum.DateTime = attrs.field(converter=_from_timestamp_to_date)
    moonrise: pendulum.DateTime = attrs.field(converter=_from_timestamp_to_date)
    moonset: pendulum.DateTime = attrs.field(converter=_from_timestamp_to_date)
    moon_phase: int
    pressure: int
    humidity: int
    dew_point: int
    wind_speed: float
    wind_deg: float
    wind_gust: float
    clouds: int
    pop: float
    uvi: float
    weather: list[Weather] = attrs.Factory(dict)
    temp: Temperature = attrs.Factory(dict)
    feels_like: FeelsLike = attrs.Factory(dict)


@attrs.frozen
class WeatherData:
    """
    This class holds all the weather data returned by the OpenWeatherMap data service for a given city.
    """
    city: str
    state: str
    country: str
    longitude: float
    latitude: float
    timezone: str
    current_weather: CurrentWeather
    daily_weather: list[DailyWeather] = attrs.Factory(list)
