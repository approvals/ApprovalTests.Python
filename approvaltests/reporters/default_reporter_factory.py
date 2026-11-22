from collections.abc import Iterator
from contextlib import contextmanager
from threading import local

from approvaltests.core.reporter import Reporter
from approvaltests.reporters.default_front_loaded_reporter import (
    DefaultFrontLoadedReporter,
)
from approvaltests.reporters.diff_reporter import DiffReporter
from approvaltests.reporters.first_working_reporter import FirstWorkingReporter

DEFAULT_REPORTER = local()
FRONT_LOADED_REPORTER = local()


def set_default_reporter(reporter: Reporter | None) -> None:
    DEFAULT_REPORTER.instance = reporter


def get_default_reporter() -> Reporter:
    instance = getattr(DEFAULT_REPORTER, "instance", None)
    return instance or DiffReporter()


def set_front_loaded_reporter(reporter: Reporter | None) -> None:
    FRONT_LOADED_REPORTER.instance = reporter


def get_front_loaded_reporter() -> Reporter | None:
    if not hasattr(FRONT_LOADED_REPORTER, "instance"):
        return DefaultFrontLoadedReporter()
    return FRONT_LOADED_REPORTER.instance


@contextmanager
def disabled_front_reporter() -> Iterator[None]:
    old = get_front_loaded_reporter()
    set_front_loaded_reporter(None)
    try:
        yield
    finally:
        set_front_loaded_reporter(old)


def get_reporter(reporter: Reporter | None) -> Reporter:
    normal = reporter or get_default_reporter()
    front_loaded = get_front_loaded_reporter()
    if front_loaded is None:
        return normal
    return FirstWorkingReporter(front_loaded, normal)
