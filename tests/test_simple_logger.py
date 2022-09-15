import datetime

import pytest

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
            datetime.datetime.fromtimestamp(1052),
        ]
        nonlocal count
        count = count + 1
        return dates[count]

    SimpleLogger.logger.timer = create_applesauce_timer
    SimpleLogger.show_timestamps(True)
    SimpleLogger.event("1")
    SimpleLogger.event("2")
    SimpleLogger.event("3")
    SimpleLogger.event("4")
    SimpleLogger.warning(Exception("Oh no you didn't!"))
    verify(output)


def test_switching() -> None:
    output = SimpleLogger.log_to_string()
    log_everything("None")

    # switches , message, variable, event, hourglass, markers
    toggles = [
        ("Query", SimpleLogger.show_query),
        ("Message", SimpleLogger.show_message),
        ("Variable", SimpleLogger.show_variable),
        ("Hour Glass", SimpleLogger.show_hour_glass),
        ("Markers", SimpleLogger.show_markers),
        # ("Events", SimpleLogger.show_events),
        ]
    for toggle_name, toggle in toggles:
        SimpleLogger.show_all(True)
        toggle(False)
        log_everything(toggle_name)
    # cycle through the switches and log everything
    verify(output)


def log_everything(message_type: str) -> None:
    SimpleLogger.event(f"Toggle Off {message_type}")
    with SimpleLogger.use_markers() as m:
        SimpleLogger.query("Select * from people")
        SimpleLogger.variable("Nonsense", "foo")
        SimpleLogger.event("Testing")
        SimpleLogger.message("Something random")
        for a in range(1, 13):
            SimpleLogger.hour_glass()
        try:
            infinity = 1 / 0
        except Exception as e:
            SimpleLogger.warning(e)
