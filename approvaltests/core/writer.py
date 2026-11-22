from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write_received_file(self, received_file: str) -> str:
        pass

    @abstractmethod
    def get_file_extension_with_dot(self) -> str:
        pass

    @abstractmethod
    def clean_up_received(self, received_file: str) -> None:
        pass
