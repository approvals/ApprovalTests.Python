import os

from _pytest.fixtures import FixtureRequest
from typing_extensions import override

from approvaltests.core.namer import Namer
from approvaltests.namer.template_field_values import TemplateFieldValues
from approvaltests.namer.templated_custom_namer import TemplatedCustomNamer


class PyTestNamer(Namer):
    "Pass a pytest 'request' to the constructor. You get one of those as a pytest fixture"

    def __init__(self, request: FixtureRequest) -> None:
        self.request = request
        self.filepath, self.filename = os.path.split(str(self.request.fspath))
        self.config: dict[str, str] = {}
        subdir = self.request.config.getoption(
            "approvaltests_subdirectory", default=None
        )
        if subdir:
            self.config["subdirectory"] = subdir

    def get_template_field_values(self) -> TemplateFieldValues:
        return TemplateFieldValues(
            approved_or_received="",
            approvals_subdirectory=self.get_config().get("subdirectory", ""),
            file_extension="",
            relative_test_source_directory=os.path.relpath(self.filepath).replace(
                os.sep, "/"
            ),
            test_case_name=self.request.node.name,
            test_file_name=os.path.splitext(self.filename)[0],
            test_source_directory=self.filepath,
            additional_information="",
        )

    def get_template(self) -> str:
        return TemplatedCustomNamer.DEFAULT_TEMPLATE

    def _create_filename(
        self, approved_or_received: str, extension_with_dot: str
    ) -> str:
        values = self.get_template_field_values().with_(
            approved_or_received, extension_with_dot[1:]
        )
        return os.path.normpath(
            TemplatedCustomNamer.create_filename(self.get_template(), values)
        )

    @override
    def get_approved_file(self, extension_with_dot: str) -> str:
        return self._create_filename(self.APPROVED_WITHOUT_DOT, extension_with_dot)

    @override
    def get_received_file(self, extension_with_dot: str) -> str:
        return self._create_filename(self.RECEIVED_WITHOUT_DOT, extension_with_dot)

    def get_directory(self) -> str:
        return self.filepath

    def get_config(self) -> dict[str, str]:
        return self.config
