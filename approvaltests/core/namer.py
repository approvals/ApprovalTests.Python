from abc import ABC, abstractmethod


class Namer(ABC):
    APPROVED_WITHOUT_DOT = "approved"
    RECEIVED_WITHOUT_DOT = "received"
    APPROVED = "." + APPROVED_WITHOUT_DOT
    RECEIVED = "." + RECEIVED_WITHOUT_DOT

    @abstractmethod
    def get_received_filename(self, base: str | None = None) -> str:
        pass

    @abstractmethod
    def get_approved_filename(self, base: str | None = None) -> str:
        pass
