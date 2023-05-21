from typing import List, Optional
from approvaltests.reporters.python_native_reporter import PythonNativeReporter
from approval_utilities.approvaltests.core.executable_command import ExecutableCommand
from approval_utilities.utilities.persistence.loader import Loader, T
from approvaltests import verify, Options, Reporter, initialize_options


class Country:
    pass


class CountryLoader(ExecutableCommand, Loader[List[Country]]):
    def load(self) -> T:
        pass

    def get_command(self) -> str:
        return "select * from Country"

    def execute_command(self, command: str) -> str:
        pass


class ExecutableCommandReporter(Reporter):
    def __init__(self, command: ExecutableCommand, reporter: Reporter):
        self.command = command
        self.reporter = reporter

    def report(self, received_path: str, approved_path: str) -> bool:
        self.reporter.report(received_path, approved_path)
        return True
        # todo run the content of the file against the executable command


def verify_executable_command(
    command: ExecutableCommand,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
):
    options = initialize_options(options)
    verify(
        command.get_command(),
        options=options.with_reporter(
            ExecutableCommandReporter(command, options.reporter)
        ),
    )


def test_to_compare_execute_command():
    # verify that the two are the same using a special reporter:
    # use the executable_command command reporter -> to be created
    # if same:
    #    test passes
    # if not the same:
    # 1. show a diff of the commands
    # 2. execute both commands - 1. received_command 2. approved_command
    # 3. show a diff of their results : received.executed_results vs. approved.executed_results
    verify_executable_command(
        CountryLoader(), options=Options().with_reporter(PythonNativeReporter()))


""" 
Sample recieved.executed_results.txt

        Do NOT approve
        This File will be Deleted
        it is for feedback purposes only

query: select * from Country

result:
| country_id | country | last_update |
| --- | --- | --- |
| 1 | Afghanistan | 2006-02-15 04:44:00 |
| 2 | Algeria | 2006-02-15 04:44:00 |
| 3 | American Samoa | 2006-02-15 04:44:00 |
| 4 | Angola | 2006-02-15 04:44:00 |
| 5 | Anguilla | 2006-02-15 04:44:00 |

"""

""" 
Sample recieved.txt
select * from Country

"""
