import typing
from threading import local
from typing import Optional

if typing.TYPE_CHECKING:
    from approvaltests.core import Reporter
from approvaltests.reporters.diff_reporter import DiffReporter

DEFAULT_REPORTER = local()


def set_default_reporter(reporter: "Reporter") -> None:
    DEFAULT_REPORTER.v = reporter


def get_default_reporter() -> "Reporter":
    if not hasattr(DEFAULT_REPORTER, "v") or DEFAULT_REPORTER.v is None:
        return DiffReporter()
    return DEFAULT_REPORTER.v


def get_reporter(reporter: Optional["Reporter"]) -> "Reporter":
    return reporter or get_default_reporter()
