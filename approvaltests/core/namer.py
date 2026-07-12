from abc import ABC, abstractmethod


class Namer(ABC):
    APPROVED_WITHOUT_DOT = "approved"
    RECEIVED_WITHOUT_DOT = "received"
    APPROVED = "." + APPROVED_WITHOUT_DOT
    RECEIVED = "." + RECEIVED_WITHOUT_DOT

    @abstractmethod
    def get_received_filename(self) -> str:
        pass

    @abstractmethod
    def get_approved_filename(self) -> str:
        pass
