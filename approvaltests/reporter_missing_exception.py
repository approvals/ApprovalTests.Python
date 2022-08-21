class ReporterMissingException(BaseException):
    def __init__(self, key):
        self.value = key

    def __str__(self):
        return f"Could not find {repr(self.value)} in the environment, perhaps you need to configure your reporter."
