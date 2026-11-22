from abc import ABC, abstractmethod


class Namer(ABC):
    APPROVED_WITHOUT_DOT = "approved"
    RECEIVED_WITHOUT_DOT = "received"

    @abstractmethod
    def get_approved_file(self, extension_with_dot: str) -> str:
        pass

    @abstractmethod
    def get_received_file(self, extension_with_dot: str) -> str:
        pass
