import json
from typing import Any, Iterator, Union, List

from approvaltests.reporters import Reporter
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter, GenericDiffReporterConfig, create_config
from approvaltests.utils import get_adjacent_file


class GenericDiffReporterFactory(object):
    reporters : List[Reporter] = []

    def __init__(self) -> None:
        self.load(get_adjacent_file("reporters.json"))

    def add_default_reporter_config(self, config):
        self.reporters.insert(0, config)
        self.reporters2.insert(0, create_config(config))

    def list(self) -> List[str]:
        return [r[0] for r in self.reporters]

    def list2(self) -> List[str]:
        return [r.name for r in self.reporters2]

    def get(self, reporter_name: str) -> GenericDiffReporter:
        config = next((r for r in self.reporters if r[0] == reporter_name), None)
        return self._create_reporter(config)

    def get2(self, reporter_name: str) -> Union[GenericDiffReporter, None]:
        config = next((r for r in self.reporters2 if r.name == reporter_name), None)
        if not config:
            return None
        return self._create_reporter2(config)

    @staticmethod
    def _create_reporter(config: Union[List[str], List[Union[str, List[str]]]]) -> GenericDiffReporter:
        if not config:
            return None
        return GenericDiffReporter(config)

    @staticmethod
    def _create_reporter2(config: GenericDiffReporterConfig) -> GenericDiffReporter:
        return GenericDiffReporter(config)

    def save(self, file_name: str) -> str:
        with open(file_name, "w") as f:
            json.dump(
                self.reporters, f, sort_keys=True, indent=2, separators=(",", ": ")
            )
        return file_name

    def save2(self, file_name: str) -> str:
        with open(file_name, "w") as f:
            json.dump(
                [reporter.serialize() for reporter in self.reporters2], f, sort_keys=True, indent=2, separators=(",", ": ")
            )
        return file_name

    def load(self, file_name: str) -> List[Union[List[str], List[Union[str, List[str]]]]]:
        with open(file_name, "r") as f:
            self.reporters = json.load(f)
        return self.reporters

    def load2(self, file_name: str) -> List[GenericDiffReporterConfig]:
        with open(file_name, "r") as f:
            configs = json.load(f)
        self.reporters2 = [create_config(config) for config in configs]
        return self.reporters2

    def get_first_working(self) -> GenericDiffReporter:
        working = (i for i in self.get_all_reporters() if i.is_working())
        return next(working, None)

    def get_all_reporters(self) -> Iterator[Any]:
        instances = (self._create_reporter(r) for r in self.reporters)
        return instances

    def get_all_reporters2(self) -> Iterator[GenericDiffReporter]:
        instances = (self._create_reporter2(r) for r in self.reporters2)
        return instances

    def remove(self, reporter_name: str) -> None:
        self.reporters = [r for r in self.reporters if r[0] != reporter_name]

    def remove2(self, reporter_name: str) -> None:
        self.reporters2 = [r for r in self.reporters2 if r.name != reporter_name]
