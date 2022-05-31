import pytest
from approvaltests import verify, get_scenario_namer
from approvaltests.namer import NamerFactory
from approvaltests.utilities.exceptions.exception_collector import gather_all_exceptions, \
    gather_all_exceptions_and_throw


def is_leap(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


@pytest.mark.parametrize("year", [1993, 1992, 1900, 2000])
def test_scenarios_old(year: int) -> None:
    verify(
        "is Leap " + str(year) + ": " + str(is_leap(year)),
        namer=get_scenario_namer(year),
    )


# begin-snippet: parametrized-test-example
@pytest.mark.parametrize("year", [1993, 1992, 1900, 2000])
def test_scenarios(year: int) -> None:
    verify(f"is Leap {str(year)}: {str(is_leap(year))}", options=NamerFactory.with_parameters(year))
# end-snippet


def test_manual_scenarios() -> None:
    # begin-snippet: multiple-verifies-without-blocking
    inputs = [1, 2]
    gather_all_exceptions_and_throw(inputs, lambda i: verify(f"{i}", options=NamerFactory.with_parameters(i)))
    # end-snippet
