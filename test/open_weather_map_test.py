# *******************************************************************************************
#  File:  open_weather_map_test.py
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

import weather_report.core.open_weather_map as owm


class TestOpenWeatherMapLocation:
    API_KEY = '6446a5397a0c3f38012e657b86f62be2'

    def test_get_location_balla(self) -> None:
        locations = owm.get_location('Balla', 'IE', TestOpenWeatherMapLocation.API_KEY)
        assert len(locations) == 3

        item = locations[0]
        assert item.city == 'Balla'
        assert item.country == 'IE'

    def test_get_location_morel(self) -> None:
        locations = owm.get_location('Mörel', 'CH', TestOpenWeatherMapLocation.API_KEY)
        assert len(locations) == 1

        item = locations[0]
        assert item.city == 'Mörel'
        assert item.state == 'Wallis'
        assert item.country == 'CH'


class TestOpenWeatherMapWeather:
    API_KEY = '6446a5397a0c3f38012e657b86f62be2'

    def test_get_location_balla(self) -> None:
        locations = owm.get_location('Balla', 'IE', TestOpenWeatherMapLocation.API_KEY)
        assert len(locations) == 3
        item = locations[0]

        weather = owm.get_weather(item, TestOpenWeatherMapWeather.API_KEY)
        assert weather

        assert weather.city == 'Balla'
        assert weather.current_weather
        assert len(weather.daily_weather) == 8

    def test_get_location_morel(self) -> None:
        locations = owm.get_location('Mörel', 'CH', TestOpenWeatherMapLocation.API_KEY)
        assert len(locations) == 1
        item = locations[0]

        weather = owm.get_weather(item, TestOpenWeatherMapWeather.API_KEY)
        assert weather

        assert weather.city == 'Mörel'
        assert weather.current_weather
        assert len(weather.daily_weather) == 8
