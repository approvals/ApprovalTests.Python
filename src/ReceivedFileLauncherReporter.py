import inspect
import os
from subprocess import call
class ReceivedFileLauncherReporter(object):


    def get_command(self, approved_path,received_path):
        return ['cmd', '/C', 'start', received_path, '/B']

    def Report(self,approved_path,received_path):
        commandArray = self.get_command(approved_path, received_path)
        call(commandArray)

        