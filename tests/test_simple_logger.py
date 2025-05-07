import datetime
import threading
from contextlib import contextmanager
from typing import Callable, Generator

from approval_utilities.utilities.logger.simple_logger import SimpleLogger
from approval_utilities.utilities.time_utilities import use_utc_timezone
from approvaltests import (
    Options,
    approvals,
    run_all_combinations,
    verify,
    verify_logging_for_all_combinations,
)
from approvaltests.utilities.logger.simple_logger_approvals import verify_simple_logger


def test_warnings() -> None:
    def scrubber(text: str) -> str:
        return text.replace(__file__, "test_simple_logger.py")

    output = SimpleLogger.log_to_string()
    SimpleLogger._wrapper.get().log_stack_traces = True
    text = "EVERYTHING IS AWFUL!!!!!!"
    try:
        raise Exception("EVERYTHING IS exceptionally AWFUL!!!!!!")
    except Exception as e:
        exception = e
    SimpleLogger.warning(text)
    SimpleLogger.warning(exception)
    SimpleLogger.warning(text, exception)
    verify(output, options=Options().with_scrubber(scrubber))


def log_from_inner_method() -> None:
    with SimpleLogger.use_markers():
        name = "Example"
        SimpleLogger.variable("name", name)
        for _ in range(0, 142):
            SimpleLogger.hour_glass()


def test_standard_logger() -> None:
    with verify_simple_logger():
        with SimpleLogger.use_markers() as m:
            log_from_inner_method()


def test_timestamps() -> None:
    with use_utc_timezone():
        with verify_simple_logger():
            count = -1

            def create_applesauce_timer() -> datetime.datetime:
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

            SimpleLogger._wrapper.get().timer = create_applesauce_timer
            SimpleLogger.show_timestamps(True)
            SimpleLogger.event("1")
            SimpleLogger.event("2")
            SimpleLogger.event("3")
            SimpleLogger.event("4")
            SimpleLogger.warning(exception=Exception("Oh no you didn't!"))


# begin-snippet: verify_simple_logger_example
def test_variable() -> None:
    with verify_simple_logger():
        SimpleLogger.variable("dalmatians", 101, show_types=True)
        SimpleLogger.variable("dalmatians", 101, show_types=False)


# end-snippet


# begin-snippet: verify_simple_logger_long_example
def test_variable_explict() -> None:
    output = SimpleLogger.log_to_string()
    SimpleLogger.variable("dalmatians", 101, show_types=True)
    SimpleLogger.variable("dalmatians", 101, show_types=False)
    verify(output)


# end-snippet


def test_variable_with_list() -> None:
    output = SimpleLogger.log_to_string()
    with SimpleLogger.use_markers():
        names = ["Jacqueline", "Llewellyn"]
        SimpleLogger.variable("names", names, show_types=True)
        SimpleLogger.variable("names", names, show_types=False)
    verify(output)


def verify_toggle(toggle_name: str, toggle: Callable[[bool], None]) -> None:
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
    with SimpleLogger.use_markers():
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


def function_to_run(color: str, number: str) -> None:
    with SimpleLogger.use_markers():
        SimpleLogger.variable("color", color)
        SimpleLogger.variable("number", number)
        if number == "brie":
            raise Exception("AHHHHHH!")


def test_use_markers_with_raised_exception() -> None:
    def throw_exception() -> None:
        with SimpleLogger.use_markers():
            raise Exception("Everything is awflu!!?")

    output = SimpleLogger.log_to_string()
    try:
        throw_exception()
    except BaseException as e:
        SimpleLogger.warning(e)
    verify(output)


def test_run_combinations() -> None:
    with verify_simple_logger():
        run_all_combinations(function_to_run, [["red", "blue"], ["one", "two", "brie"]])


def test_run_combinations_with_exception_handler() -> None:
    approvals.settings().allow_multiple_verify_calls_for_this_method()

    with verify_simple_logger():
        run_all_combinations(
            function_to_run,
            [["red"], ["one", "brie"]],
            exception_handler=lambda e: SimpleLogger.warning(exception=e),
        )
    with verify_simple_logger():
        run_all_combinations(
            function_to_run,
            [["red"], ["one", "brie"]],
            exception_handler=lambda e: SimpleLogger.warning(e),
        )
    with verify_simple_logger():
        run_all_combinations(
            function_to_run,
            [["red"], ["one", "brie"]],
            exception_handler=SimpleLogger.warning,
        )


def test_verify_logging_for_all_combinations() -> None:
    verify_logging_for_all_combinations(
        function_to_run, [["red", "blue"], ["one", "two", "brie"]]
    )


# begin-snippet: method_with_inputs
def method_with_inputs(number: int, name: str) -> None:
    with SimpleLogger.use_markers(f"number = {number}, name = {name}"):
        # end-snippet
        print(f"{number}) {name}")


def test_markers_with_signature() -> None:
    output = SimpleLogger.log_to_string()
    method_with_inputs(1, "Susan")
    verify(output)


# begin-snippet: method_with_inputs_and_outputs
def method_with_inputs_and_outputs(number: int, announcement: str) -> None:
    with SimpleLogger.use_markers(
        lambda: f"number = {number}, announcement = {announcement}"
    ):
        # end-snippet
        for number in range(number, 0, -1):
            print(number)
        print(announcement)


def test_markers_with_signature_in_and_out() -> None:
    output = SimpleLogger.log_to_string()
    method_with_inputs_and_outputs(10, "Blast off")
    verify(output)


def test_race_condition() -> None:
    whose_turn = 0

    @contextmanager
    def wait_for(number: int) -> Generator[None, None, None]:
        nonlocal whose_turn
        while whose_turn < number:
            pass
        yield
        whose_turn += 1

    log1 = "Log1"

    def thread_1() -> None:
        nonlocal log1
        with wait_for(0):
            log1 = SimpleLogger.log_to_string(True)
        with wait_for(2):
            SimpleLogger.event("event_a")
        with wait_for(4):
            SimpleLogger.event("event_b")

    log2 = "Log2"

    def thread_2() -> None:
        nonlocal log2
        with wait_for(1):
            log2 = SimpleLogger.log_to_string(True)
        with wait_for(3):
            SimpleLogger.event("event_a")
        with wait_for(5):
            SimpleLogger.event("event_b")

    threading.Thread(target=thread_1).start()
    threading.Thread(target=thread_2).start()

    with wait_for(6):
        assert f"'{log1}'" == f"'{log2}'"
