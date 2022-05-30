from approvaltests import verify_exception
from approvaltests.utilities.exceptions.exception_collector import ExceptionCollector


def test_gather_all_exceptions():
    def is_odd(integer):
        assert integer % 2 == 0

    collector = ExceptionCollector()
    for i in range(1, 6):
        collector.gather(lambda: is_odd(i))

    verify_exception(lambda: collector.release())
