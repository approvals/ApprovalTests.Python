class ReporterMissingException(BaseException):
    def __init__(self, key):
        self.value = key

    def __str__(self):
        return (
            "Could not find %s in the environment, perhaps you need to configure your reporter."
            % repr(self.value)
        )
