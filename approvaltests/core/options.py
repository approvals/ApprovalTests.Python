from typing import Dict, Callable

from approvaltests.core import Reporter


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
            return self.fields['scrubber_func'](data)
        return data

    def with_reporter(self, reporter: "Reporter") -> "Options":
        return Options({**self.fields, **{"reporter": reporter}})

    def with_scrubber(self, scrubber_func: Callable[[str],str]) -> "Options":
        return Options({**self.fields, **{"scrubber_func": scrubber_func}})
