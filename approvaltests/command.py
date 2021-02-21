import os
from typing import Optional


class Command(object):
    def __init__(self, cmd: str) -> None:
        self.command = cmd

    @staticmethod
    def executable(cmd: str) -> bool:
        return os.path.isfile(cmd) and os.access(cmd, os.X_OK)

    def locate(self) -> Optional[str]:
        path, name = os.path.split(self.command)
        if path and self.executable(self.command):
            return self.command
        if True:  # use 'where' to find the executable so it finds python and python.exe
            pass

        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe = os.path.join(path, self.command)
            if self.executable(exe):
                return exe

        return None
