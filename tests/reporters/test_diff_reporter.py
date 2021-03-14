from typing import List

from approvaltests.reporters import (
    DiffReporter,
    PythonNativeReporter, Reporter,
)


class FakeFactory:
    def get_all_reporters(self) -> List[Reporter]:
        return []


def test_fallback_reporter() -> None:
    empty_reporter_factory = FakeFactory()
    reporter = DiffReporter(empty_reporter_factory)
    # Testing implementation detail, not great but good enough for now
    assert isinstance(reporter.reporters[-1], PythonNativeReporter)
