import pytest

from approval_utilities.utilities.exceptions.exception_collector import (
    gather_all_exceptions_and_throw,
)
from approvaltests import get_scenario_namer, verify
from approvaltests.namer import NamerFactory


def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


@pytest.mark.parametrize("year", [1993, 1992, 1900, 2000])
def test_scenarios_old(year: int) -> None:
    verify(
        f"is Leap {str(year)}: {str(is_leap_year(year))}",
        namer=get_scenario_namer(year),
    )


# begin-snippet: parametrized-test-example
@pytest.mark.parametrize("year", [1993, 1992, 1900, 2000])
def test_scenarios(year: int) -> None:
    verify(
        f"is Leap {str(year)}: {str(is_leap_year(year))}",
        options=NamerFactory.with_parameters(year),
    )


# end-snippet


def test_manual_scenarios_with_blocking() -> None:
    # begin-snippet: multiple-verifies-with-blocking
    year = 1992
    verify(
        f"is Leap {str(year)}: {str(is_leap_year(year))}",
        options=NamerFactory.with_parameters(year),
    )
    year = 1993
    verify(
        f"is Leap {str(year)}: {str(is_leap_year(year))}",
        options=NamerFactory.with_parameters(year),
    )
    year = 1900
    verify(
        f"is Leap {str(year)}: {str(is_leap_year(year))}",
        options=NamerFactory.with_parameters(year),
    )
    year = 2000
    verify(
        f"is Leap {str(year)}: {str(is_leap_year(year))}",
        options=NamerFactory.with_parameters(year),
    )
    # end-snippet


def test_manual_scenarios() -> None:
    # begin-snippet: multiple-verifies-without-blocking
    years = [1993, 1992, 1900, 2000]
    gather_all_exceptions_and_throw(
        years,
        lambda y: verify(
            f"is Leap {str(y)}: {str(is_leap_year(y))}",
            options=NamerFactory.with_parameters(y),
        ),
    )
    # end-snippet
