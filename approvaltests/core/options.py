from typing import Dict

# from approvaltests import Reporter


class Options:
    def __init__(self, fields: Dict = None):
        self.fields = fields or {}

    @property
    def reporter(self) -> "Reporter":
        # TODO Fix circular import
        from approvaltests import get_default_reporter

        return self.fields.get("reporter", get_default_reporter())

    def with_reporter(self, reporter: "Reporter") -> "Options":
        return Options({**self.fields, **{"reporter": reporter}})
