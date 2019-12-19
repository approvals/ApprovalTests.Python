import os

import approvaltests
from approvaltests.core import Namer


class PyTestNamer(Namer):
    "Pass a pytest 'request' to the constructor. You get one of those as a pytest fixture"
    def __init__(self, request, extension=None):
        Namer.__init__(self, extension)
        self.request = request
        self.filepath, self.filename = os.path.split(str(self.request.fspath))
        self.config = {}
        subdir = self.request.config.getoption("approvaltests_subdirectory", default=None)
        if subdir:
            self.config["subdirectory"] = subdir

    def get_file_name(self):
        return os.path.splitext(self.filename)[0] + "." + self.request.node.name

    def get_directory(self):
        return self.filepath

    def get_config(self):
        return self.config



