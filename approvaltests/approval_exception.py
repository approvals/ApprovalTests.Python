class ApprovalException(Exception):
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self):
        return self.value


class FrameNotFound(ApprovalException):
    pass
