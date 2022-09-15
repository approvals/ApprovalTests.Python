import datetime
import os
from pathlib import Path

from approvaltests import verify, Options
from approvaltests.utilities.logger.simple_logger import SimpleLogger


def test_warnings():
    def scrubber(text: str) -> str:
        return text.replace(__file__, "test_simple_logger.py")

    output = SimpleLogger.log_to_string()
    SimpleLogger.logger.log_stack_traces = True
    text = "EVERYTHING IS AWFUL!!!!!!"
    try:
        raise Exception("EVERYTHING IS exceptionally AWFUL!!!!!!")
    except Exception as e:
        exception = e
    SimpleLogger.warning(text)
    SimpleLogger.warning(exception)
    SimpleLogger.warning(text, exception)
    verify(output, options=Options().with_scrubber(scrubber))


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
    SimpleLogger.warning(exception=Exception("Oh no you didn't!"))
    verify(output)


def test_variable():
    names = ["Jacqueline", "Llewellyn"]
    output = SimpleLogger.log_to_string()
    SimpleLogger.variable("names", names)
    verify(output)


def verify_toggle(toggle_name, toggle):
    SimpleLogger.show_all(True)
    SimpleLogger.event(f"Toggle Off {toggle_name}")
    toggle(False)
    log_everything()


def test_switching() -> None:
    output = SimpleLogger.log_to_string()

    verify_toggle("None", lambda a: SimpleLogger.show_all(True)),
    verify_toggle("All", SimpleLogger.show_all),
    verify_toggle("Query", SimpleLogger.show_queries),
    verify_toggle("Message", SimpleLogger.show_messages),
    verify_toggle("Variable", SimpleLogger.show_variables),
    verify_toggle("Hour Glass", SimpleLogger.show_hour_glass),
    verify_toggle("Markers", SimpleLogger.show_markers),
    verify_toggle("Events", SimpleLogger.show_events),

    verify(output)


def log_everything() -> None:
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
            SimpleLogger.warning(exception=e)
