from typing import List, Optional

from approvaltests.reporters.executable_command_reporter import (
    ExecutableCommandReporter,
)
from approvaltests.reporters.python_native_reporter import PythonNativeReporter
from approval_utilities.approvaltests.core.executable_command import ExecutableCommand
from approval_utilities.utilities.persistence.loader import Loader, T
from approvaltests import verify, Options, initialize_options


class Country:
    pass


class CountryLoader(ExecutableCommand, Loader[List[Country]]):
    def load(self) -> T:
        pass

    def get_command(self) -> str:
        return "select * from Country"

    def execute_command(self, command: str) -> str:
        return f"""
        
| country_id | country | last_update |
| --- | --- | --- |
| 1 | Afghanistan | 2006-02-15 04:44:00 |
| 2 | Algeria | 2006-02-15 04:44:00 |        
        """
        pass


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


def ptest_to_compare_execute_command():
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


    result = ExecutableCommandReporter.execute_command_and_format_result(executed_command, DummyExecutableCommand())
    verify(result)


def test_result_formatting_for_non_empty_command():
    executed_command = "select * from foo"

    class DummyExecutableCommand(ExecutableCommand):
        def get_command(self) -> str:
            return None

        def execute_command(self, command: str) -> str:
            return "result of the query"


    result = ExecutableCommandReporter.execute_command_and_format_result(executed_command, DummyExecutableCommand())
    verify(result)


"""
1. actually query database from country loader
1. refactor duplication
"""
