import os


class Command(object):

    def __init__(self, cmd):
        self.command = cmd

    @staticmethod
    def executable(cmd):
        return os.path.isfile(cmd) and os.access(cmd, os.X_OK)

    def locate(self):
        path, name = os.path.split(self.command)
        if path and self.executable(self.command):
            return self.command
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                path=path.strip('"')
                exe = os.path.join(path, self.command)
                if self.executable(exe):
                    return exe

        return None