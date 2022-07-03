from abc import abstractmethod, ABC
from typing import Optional


class Namer(ABC):
    APPROVED = ".approved"
    RECEIVED = ".received"

    @abstractmethod
    def get_received_filename(self, base: Optional[str] = None) -> str:
        pass

    @abstractmethod
    def get_approved_filename(self, base: Optional[str] = None) -> str:
        pass
