from importlib.metadata import version

from .weather_yz5410 import (
    celsius_to_fahrenheit,
    clean_readings,
    summarize_temperatures,
)

__version__ = version("weather_yz5410")