import inspect
import os
from subprocess import call
class ReceivedFileLauncherReporter(object):

    def Report(self,approved_path,received_path):
        call(['cmd', '/C', 'start', received_path, '/B'])
        
        