from subprocess import call

from approvaltests.core.reporter import Reporter


class ReceivedFileLauncherReporter(Reporter):

    @staticmethod
    def get_command(approved_path, received_path):
        return ['cmd', '/C', 'start', received_path, '/B']

    def report(self, approved_path, received_path):
        command_array = self.get_command(approved_path, received_path)
        call(command_array)
