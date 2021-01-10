from subprocess import call

from approvaltests.core.reporter import Reporter


class ReceivedFileLauncherReporter(Reporter):
    """
    A blocking reporter that attempts to
    open the received file using the
    system default text file viewer.

    Note: only works on Windows for now.
    """

    @staticmethod
    def get_command(approved_path, received_path):
        return ['cmd', '/C', 'start', received_path, '/B']

    def report(self, approved_path, received_path):
        command_array = self.get_command(approved_path, received_path)
        call(command_array)
