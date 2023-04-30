from typing import List, Optional

from approval_utilities.approvaltests.core.executable_command import ExecutableCommand
from approval_utilities.utilities.persistence.loader import Loader, T
from approvaltests import verify, Options, Reporter, initialize_options


class Country:
    pass


class CountryLoader(ExecutableCommand, Loader[List[Country]] ):
    def load(self) -> T:
        pass

    def get_command(self) -> str:
        return 'select * from Country' 

    def execute_command(self, command: str) -> str:
        pass


class ExecutableCommandReporter(Reporter):
    def report(self, received_path: str, approved_path: str) -> bool:
        pass


def verify_executable_command(command: ExecutableCommand,
                              *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
                              options: Optional[Options] = None
                              ):
    options = initialize_options(options)
    verify(command.get_command(), options=options.with_reporter(ExecutableCommandReporter.create(command, options.reporter)))


def test_new_lines_with_empty_string():

    # verify that the two are the same using a special reporter:
    # use the executable_command command reporter -> to be created
    verify_executable_command(CountryLoader())

