from abc import abstractmethod, ABC


class ExecutableCommand(ABC):
    @abstractmethod
    def get_command(self) -> str:
        raise Exception("Interface member not implemented")

    @abstractmethod
    def execute_command(self, command: str) -> str:
        raise Exception("Interface member not implemented")
