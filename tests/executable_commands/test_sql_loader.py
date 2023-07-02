from approvaltests.reporters.executable_command_reporter import (
    ExecutableCommandReporter,
)
from approval_utilities.approvaltests.core.executable_command import ExecutableCommand
from approvaltests import verify, verify_executable_command
from tests.executable_commands.country_loader import CountryLoader


def test_to_compare_execute_command():
    verify_executable_command(CountryLoader())


def test_to_compare_execute_command_where_we_see_the_failure():
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
