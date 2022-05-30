from approvaltests import verify_exception
from approvaltests.utilities.exceptions.exception_collector import ExceptionCollector, gather_all_exceptions


def is_odd(integer):
    assert integer % 2 == 0


def test_gather_all_exceptions():
    collector = ExceptionCollector()
    for i in range(1, 6):
        collector.gather(lambda: is_odd(i))

    verify_exception(lambda: collector.release())


def test_gather_all_exceptions_from_list():
    verify_exception(lambda: gather_all_exceptions(range(1, 6), is_odd).release())
