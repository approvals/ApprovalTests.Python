from typing import Optional

from approvaltests.reporters.executable_command_reporter import (
    ExecutableCommandReporter,
)
from approval_utilities.approvaltests.core.executable_command import ExecutableCommand
from approvaltests import verify, Options, initialize_options
from tests.executable_commands.country_loader import CountryLoader


def verify_executable_command(
    command: ExecutableCommand,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None,
):
    options = initialize_options(options)
    verify(
        command.get_command(),
        options=options.with_reporter(
            ExecutableCommandReporter(command, options.reporter)
        ),
    )


def test_to_compare_execute_command():
    verify_executable_command(CountryLoader())


def test_to_compare_execute_command_where_we_see_the_failure():
    # verify that the two are the same using a special reporter:
    # use the executable_command command reporter -> to be created
    # if same:
    #    test passes
    # if not the same:
    # 1. show a diff of the commands
    # 2. execute both commands - 1. received_command 2. approved_command
    # 3.
    # 3. show a diff of their results : received.executed_results vs. approved.executed_results
    verify_executable_command(CountryLoader())


def test_result_formatting_for_results_with_indentation():
    executed_command = "select * from foo"

    class DummyExecutableCommand(ExecutableCommand):
        def get_command(self) -> str:
            return None

        def execute_command(self, command: str) -> str:
            return "result of the query\nstuff that breaks indentation"

    result = ExecutableCommandReporter.execute_command_and_format_result(
        executed_command, DummyExecutableCommand()
    )
    verify(result)


def test_result_formatting_for_non_empty_command():
    executed_command = "select * from foo"

    class DummyExecutableCommand(ExecutableCommand):
        def get_command(self) -> str:
            return None

        def execute_command(self, command: str) -> str:
            return "result of the query"

    result = ExecutableCommandReporter.execute_command_and_format_result(
        executed_command, DummyExecutableCommand()
    )
    verify(result)


def test_result_formatting_for_empty():
    # ApprovalTests doesn't try to execute empty commands
    assert "" == ExecutableCommandReporter.execute_command_and_format_result(None, None)


"""
1. actually query database from country loader
1. refactor duplication
1. make a video and documentation
"""
