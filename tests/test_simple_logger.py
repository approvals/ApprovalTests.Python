import datetime

from approvaltests import verify
from approvaltests.utilities.logger.simple_logger import SimpleLogger


def log_from_inner_method():
    with SimpleLogger.use_markers() as m:
        name = "Example"
        SimpleLogger.variable("name", name)
        for _ in range(0, 142):
            SimpleLogger.hour_glass()


def test_standard_logger():
    output = SimpleLogger.log_to_string()
    with SimpleLogger.use_markers() as m:
        log_from_inner_method()

    verify(output)


def test_timestamps():
    output = SimpleLogger.log_to_string()
    count = -1

    def create_applesauce_timer():
        dates = [
            datetime.datetime.fromtimestamp(0.0),
            datetime.datetime.fromtimestamp(0.5),
            datetime.datetime.fromtimestamp(2.0),
            datetime.datetime.fromtimestamp(1050),
        ]
        nonlocal count
        count = count + 1
        return dates[count]

    SimpleLogger.logger.timer = create_applesauce_timer
    SimpleLogger.logger.timestamp = True
    SimpleLogger.event("1")
    SimpleLogger.event("2")
    SimpleLogger.event("3")
    SimpleLogger.event("4")
    verify(output)
