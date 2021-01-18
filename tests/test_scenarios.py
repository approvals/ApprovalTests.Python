import pytest
from approvaltests import verify, get_scenario_namer


def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


@pytest.mark.parametrize("year", [1993, 1992, 1900, 2000])
def test_scenarios(year):
    verify(
        "is Leap " + str(year) + ": " + str(is_leap(year)),
        namer=get_scenario_namer(year),
    )
