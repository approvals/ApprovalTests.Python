import pathlib

from approval_utilities.approvaltests.core.executable_command import ExecutableCommand
from approvaltests import Reporter


class ExecutableCommandReporter(Reporter):
    def __init__(self, command: ExecutableCommand, reporter: Reporter):
        self.command = command
        self.reporter = reporter

    def report(self, received_filename: str, approved_filename: str) -> bool:
        # recieved and approved commands are not the same
        # todo run the content of the file against the executable command
        # execute(read(received))

        self.reporter.report(self.execute_result(received_filename), self.execute_result(approved_filename))
        self.reporter.report(received_filename, approved_filename)
        return True

    def execute_result(self, filename):
        path = pathlib.Path(filename)
        command = path.read_text()
        if command:
            result = self.command.execute_command(command)
        else:
            result = ""
        approved_executed_result_file = f"{path.name[:-len(path.suffix)]}.executed_results.txt"
        pathlib.Path(approved_executed_result_file).write_text(result)
        return approved_executed_result_file
