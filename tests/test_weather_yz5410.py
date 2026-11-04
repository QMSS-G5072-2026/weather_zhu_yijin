"""Tests for the weather station functions."""

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from weather_yz5410 import (
    celsius_to_fahrenheit,
    clean_readings,
    summarize_temperatures,
)


@pytest.mark.parametrize("celsius, expected", [
    (0, 32.0),
    (100, 212.0),
    (-40, -40.0),
    (37, 98.6),
    (-273.15, -459.67),
])
def test_celsius_to_fahrenheit(celsius, expected):
    """Check temperature conversion for five known values."""
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)


@pytest.mark.parametrize("bad_input, expected_error", [
    ("37", TypeError),
    (None, TypeError),
    ([37], TypeError),
    (-273.16, ValueError),
])
def test_celsius_to_fahrenheit_invalid(bad_input, expected_error):
    """Check that invalid inputs raise the expected errors."""
    with pytest.raises(expected_error):
        celsius_to_fahrenheit(bad_input)


def test_summarize_temperatures():
    """Check all four summary values when one reading is missing."""
    temps = [10.0, float("nan"), 20.0, 30.0]

    result = summarize_temperatures(temps)

    assert result["mean"] == pytest.approx(20.0)
    assert result["min"] == pytest.approx(10.0)
    assert result["max"] == pytest.approx(30.0)
    assert result["n_missing"] == 1


@pytest.fixture
def raw_readings():
    """Provide five raw readings with one missing and one implausible temperature."""
    return pd.DataFrame({
        "station": ["JFK", "CPK", "JFK", "CPK", "LGA"],
        "date": [
            "2026-07-02",
            "2026-07-01",
            "2026-07-01",
            "2026-07-02",
            "2026-07-01",
        ],
        "temp_c": [30.0, 25.0, float("nan"), 999.0, 28.0],
    })


def test_raw_readings_fixture(raw_readings):
    """Check the fixture's columns, row count, and missing values."""
    assert raw_readings.columns.tolist() == ["station", "date", "temp_c"]
    assert len(raw_readings) == 5
    assert raw_readings.isna().sum().to_dict() == {
        "station": 0,
        "date": 0,
        "temp_c": 1,
    }


def test_clean_readings(raw_readings):
    """Check that cleaning removes invalid readings, converts temperatures, and sorts rows."""
    expected = pd.DataFrame({
        "station": ["CPK", "JFK", "LGA"],
        "date": ["2026-07-01", "2026-07-02", "2026-07-01"],
        "temp_c": [25.0, 30.0, 28.0],
        "temp_f": [77.0, 86.0, 82.4],
    })

    result = clean_readings(raw_readings)

    assert_frame_equal(result, expected)
