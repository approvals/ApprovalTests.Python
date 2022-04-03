import os
from typing import Optional


class Namer(object):
    APPROVED = ".approved"
    RECEIVED = ".received"

    def __init__(self, extension: Optional[str] = None) -> None:
        self.extension_with_dot = extension or ".txt"

    def get_file_name(self):
        raise Exception("This class is abstract, override this method in a subclass")

    def get_directory(self):
        raise Exception("This class is abstract, override this method in a subclass")

    def get_config(self):
        raise Exception("This class is abstract, override this method in a subclass")

    def get_basename(self) -> str:
        file_name = self.get_file_name()
        subdirectory = self.get_config().get("subdirectory", "")
        return str(os.path.join(self.get_directory(), subdirectory, file_name))

    def get_received_filename(self, basename: Optional[str] = None) -> str:
        basename = basename or self.get_basename()
        return basename + Namer.RECEIVED + self.extension_with_dot

    def get_approved_filename(self, basename: Optional[str] = None) -> str:
        basename = basename or self.get_basename()
        return basename + Namer.APPROVED + self.extension_with_dot

    def set_extension(self, extension):
        self.extension_with_dot = extension


