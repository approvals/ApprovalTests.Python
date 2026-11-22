from abc import abstractmethod

from approvaltests.core.namer import Namer


class NamerBase(Namer):
    def __init__(self, extension: str | None = None) -> None:
        self.extension_with_dot = extension or ".txt"

    @abstractmethod
    def get_file_name(self) -> str:
        raise Exception("This class is abstract, override this method in a subclass")

    @abstractmethod
    def get_directory(self) -> str:
        raise Exception("This class is abstract, override this method in a subclass")

    def set_extension(self, extension: str) -> None:
        self.extension_with_dot = extension
