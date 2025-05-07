from approval_utilities.utilities.exceptions.exception_collector import (
    ExceptionCollector,
    gather_all_exceptions,
)
from approvaltests import verify_exception


def is_odd(integer: int) -> None:
    if integer % 2 != 0:
        raise ValueError(f"{integer} is not odd!")


def test_gather_all_exceptions() -> None:
    collector = ExceptionCollector()
    for i in range(1, 6):
        collector.gather(lambda: is_odd(i))

    verify_exception(lambda: collector.release())


def test_gather_all_exceptions_from_list() -> None:
    verify_exception(lambda: gather_all_exceptions(range(1, 6), is_odd).release())
