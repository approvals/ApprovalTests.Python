import os

from _pytest.fixtures import FixtureRequest
from typing_extensions import override

from approvaltests.namer.namer_base import NamerBase
from approvaltests.namer.templated_custom_namer import (
    TemplatedCustomNamer,
    TemplateFieldValues,
)


class PyTestNamer(NamerBase):
    "Pass a pytest 'request' to the constructor. You get one of those as a pytest fixture"

    def __init__(self, request: FixtureRequest, extension: None = None) -> None:
        NamerBase.__init__(self, extension)
        self.request = request
        self.filepath, self.filename = os.path.split(str(self.request.fspath))
        self.config: dict[str, str] = {}
        subdir = self.request.config.getoption(
            "approvaltests_subdirectory", default=None
        )
        if subdir:
            self.config["subdirectory"] = subdir

    @override
    def get_file_name(self) -> str:
        return f"{os.path.splitext(self.filename)[0]}.{self.request.node.name}"

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

    def get_basename(self) -> str:
        return TemplatedCustomNamer.create_filename(
            "{test_source_directory}/{approvals_subdirectory}/{test_file_name}.{test_case_name}",
            self.get_template_field_values(),
        )

    def _create_filename(self, approved_or_received: str) -> str:
        values = self.get_template_field_values().with_(
            approved_or_received, self.extension_with_dot[1:]
        )
        return TemplatedCustomNamer.create_filename(self.get_template(), values)

    @override
    def get_approved_filename(self) -> str:
        return self._create_filename(self.APPROVED_WITHOUT_DOT)

    @override
    def get_received_filename(self) -> str:
        return self._create_filename(self.RECEIVED_WITHOUT_DOT)

    @override
    def get_directory(self) -> str:
        return self.filepath

    def get_config(self) -> dict[str, str]:
        return self.config
