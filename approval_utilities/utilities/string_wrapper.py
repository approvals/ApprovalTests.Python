class StringWrapper:
    def __init__(self) -> None:
        self.string = ""

    def append(self, text: str) -> None:
        self.string += text

    def __str__(self) -> str:
        return self.string

    def __repr__(self) -> str:
        return self.string
