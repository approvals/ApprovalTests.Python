from subprocess import call
from Reporter import Reporter

class ReceivedFileLauncherReporter(Reporter):

    def get_command(self, approved_path, received_path):
        return ['cmd', '/C', 'start', received_path, '/B']

    def report(self, approved_path, received_path):
        commandArray = self.get_command(approved_path, received_path)
        call(commandArray)
