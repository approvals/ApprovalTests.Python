import os
from typing import Dict

from _pytest.fixtures import FixtureRequest

from approvaltests.core import Namer


class PyTestNamer(Namer):
    "Pass a pytest 'request' to the constructor. You get one of those as a pytest fixture"

    def __init__(self, request: FixtureRequest, extension: None = None) -> None:
        Namer.__init__(self, extension)
        self.request = request
        self.filepath, self.filename = os.path.split(str(self.request.fspath))
        self.config: Dict[str, str] = {}
        subdir = self.request.config.getoption(
            "approvaltests_subdirectory", default=None
        )
        if subdir:
            self.config["subdirectory"] = subdir

    def get_file_name(self) -> str:
        return os.path.splitext(self.filename)[0] + "." + self.request.node.name

    def get_directory(self) -> str:
        return self.filepath

    def get_config(self) -> Dict[str, str]:
        return self.config
