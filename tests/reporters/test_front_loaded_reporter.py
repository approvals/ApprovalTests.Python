from typing_extensions import override

from approvaltests.core.options import Options
from approvaltests.core.reporter import Reporter
from approvaltests.reporters.default_reporter_factory import (
    get_front_loaded_reporter,
    get_reporter,
    set_front_loaded_reporter,
)


class RecordingReporter(Reporter):
    def __init__(self, works: bool) -> None:
        self.works = works
        self.called = False

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        self.called = True
        return self.works


def report_with_front_loaded(front_loaded: Reporter, passed_in: Reporter) -> None:
    old = get_front_loaded_reporter()
    set_front_loaded_reporter(front_loaded)
    try:
        get_reporter(passed_in).report("a.received.txt", "a.approved.txt")
    finally:
        set_front_loaded_reporter(old)


def test_front_loaded_reporter_overrides_a_passed_in_reporter() -> None:
    front_loaded = RecordingReporter(works=True)
    passed_in = RecordingReporter(works=True)

    report_with_front_loaded(front_loaded, passed_in)

    assert (front_loaded.called, passed_in.called) == (True, False)


def test_passed_in_reporter_runs_when_front_loaded_reporter_does_not_work() -> None:
    front_loaded = RecordingReporter(works=False)
    passed_in = RecordingReporter(works=True)

    report_with_front_loaded(front_loaded, passed_in)

    assert passed_in.called


def test_front_loaded_reporter_overrides_the_options_reporter() -> None:
    front_loaded = RecordingReporter(works=True)
    from_options = RecordingReporter(works=True)
    old = get_front_loaded_reporter()
    set_front_loaded_reporter(front_loaded)
    try:
        options = Options().with_reporter(from_options)
        options.reporter.report("a.received.txt", "a.approved.txt")
    finally:
        set_front_loaded_reporter(old)

    assert (front_loaded.called, from_options.called) == (True, False)
