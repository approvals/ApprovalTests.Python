from approvaltests.reporters import (
    GenericDiffReporterFactory,
    DiffReporter,
    PythonNativeReporter,
)
from typing import Any, List


class FakeFactory:
    def get_all_reporters(self) -> List[Any]:
        return []


def test_fallback_reporter() -> None:
    empty_reporter_factory = FakeFactory()
    reporter = DiffReporter(empty_reporter_factory)
    # Testing implementation detail, not great but good enough for now
    assert isinstance(reporter.reporters[-1], PythonNativeReporter)
