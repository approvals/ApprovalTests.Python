class GenericDiffReporterConfig:
    def __init__(self, name: str, path: str, extra_args: list[str] | None = None):
        self.name = name
        self.path = path
        self.extra_args = extra_args or []

    def serialize(self) -> list[str]:
        result = [self.name, self.path]
        if self.extra_args:
            result.append(self.extra_args)
        return result


def create_config(config: list[str]) -> GenericDiffReporterConfig:
    return GenericDiffReporterConfig(*config)
