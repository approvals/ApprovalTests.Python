from typing import Dict, Callable

from .namer import Namer
from .reporter import Reporter
from .comparator import Comparator
from approvaltests.file_approver import FileComparator



class FileOptions:
    def __init__(self, fields: Dict):
        self.fields = fields

    def with_extension(self, extension_with_dot: str,
                       *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/,
                       no_override= False
                        ) -> "Options":
        if not (extension_with_dot.startswith(".")):
            extension_with_dot = f".{extension_with_dot}"
        if no_override and "extension_with_dot" in self.fields:
            extension_with_dot = self.fields["extension_with_dot"]
        return Options({**self.fields, **{"extension_with_dot": extension_with_dot}})


class Options:
    def __init__(self, fields: Dict = None):
        self.fields = fields or {}

    @property
    def reporter(self) -> Reporter:
        from approvaltests.reporters.default_reporter_factory import get_default_reporter

        return self.fields.get("reporter", get_default_reporter())

    @property
    def comparator(self) -> Comparator:
        return self.fields.get("comparator", FileComparator())

    def with_comparator(self, comparator: Comparator) -> "Options":
        return Options({**self.fields, **{"comparator": comparator}})

    def scrub(self, data):
        return self.fields["scrubber_func"](data) if self.has_scrubber() else data

    def with_scrubber(self, scrubber_func: Callable[[str], str]) -> "Options":
        return Options({**self.fields, **{"scrubber_func": scrubber_func}})

    def has_scrubber(self):
        return "scrubber_func" in self.fields


    def with_reporter(self, reporter: "Reporter") -> "Options":
        return Options({**self.fields, **{"reporter": reporter}})

    @property
    def for_file(self) -> FileOptions:
        return FileOptions(self.fields)

    @property
    def namer(self) -> Namer:
        from approvaltests.namer.default_namer_factory import get_default_namer

        namer = get_default_namer()
        namer.set_extension(self.fields.get("extension_with_dot", ".txt"))
        return namer


