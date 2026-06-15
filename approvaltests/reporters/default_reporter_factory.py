from threading import local

from approvaltests.core.reporter import Reporter
from approvaltests.reporters.diff_reporter import DiffReporter
from approvaltests.reporters.environment_variable_reporter import (
    EnvironmentVariableReporter,
)
from approvaltests.reporters.first_working_reporter import FirstWorkingReporter

DEFAULT_REPORTER = local()


def set_default_reporter(reporter: Reporter | None) -> None:
    DEFAULT_REPORTER.instance = reporter


def get_default_reporter() -> Reporter:
    if not hasattr(DEFAULT_REPORTER, "instance") or DEFAULT_REPORTER.instance is None:
        return FirstWorkingReporter(EnvironmentVariableReporter(), DiffReporter())
    return DEFAULT_REPORTER.instance


def get_reporter(reporter: Reporter | None) -> Reporter:
    return reporter or get_default_reporter()
