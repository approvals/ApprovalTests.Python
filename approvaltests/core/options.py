from typing import Dict, Callable

from approvaltests.core import Reporter


class FileOptions:
    def __init__(self, fields: Dict):
        self.fields = fields

    def with_extension(self, extension_with_dot: str) -> "Options":
        if not (extension_with_dot.startswith(".")):
            extension_with_dot = "." + extension_with_dot
        return Options({**self.fields, **{"extension_with_dot": extension_with_dot}})


class Options:
    def __init__(self, fields: Dict = None):
        self.fields = fields or {}

    @property
    def reporter(self) -> Reporter:
        # TODO Fix circular import
        from approvaltests import get_default_reporter

        return self.fields.get("reporter", get_default_reporter())

    def scrub(self, data):
        if "scrubber_func" in self.fields:
            return self.fields["scrubber_func"](data)
        return data

    def with_reporter(self, reporter: "Reporter") -> "Options":
        return Options({**self.fields, **{"reporter": reporter}})

    def with_scrubber(self, scrubber_func: Callable[[str], str]) -> "Options":
        return Options({**self.fields, **{"scrubber_func": scrubber_func}})

    @property
    def for_file(self) -> FileOptions:
        return FileOptions(self.fields)

    @property
    def namer(self) -> "Namer":
        from approvaltests import get_default_namer

        namer = get_default_namer()
        namer.set_extension(self.fields.get("extension_with_dot", ".txt"))
        return namer
