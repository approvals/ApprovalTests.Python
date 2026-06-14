import importlib
import os
from typing import cast

from typing_extensions import override

from approvaltests.core.reporter import Reporter


class EnvironmentVariableReporter(Reporter):
    ENVIRONMENT_VARIABLE_NAME = "APPROVAL_TESTS_USE_REPORTER"

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        class_name = os.environ.get(self.ENVIRONMENT_VARIABLE_NAME)
        return EnvironmentVariableReporter._report_with(
            class_name, received_path, approved_path
        )

    @staticmethod
    def _report_with(
        class_name: str | None, received_path: str, approved_path: str
    ) -> bool:
        if not class_name:
            return False
        reporter = EnvironmentVariableReporter._load_reporter(class_name)
        return reporter.report(received_path, approved_path)

    @staticmethod
    def _load_reporter(class_name: str) -> Reporter:
        module_name, _, attr = class_name.rpartition(".")
        module = importlib.import_module(module_name)
        cls = getattr(module, attr)
        return cast("Reporter", cls())
