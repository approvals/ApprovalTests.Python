import os
from dataclasses import asdict, dataclass, replace

from typing_extensions import override

from approvaltests.core.namer import Namer
from approvaltests.namer import stack_walker
from approvaltests.namer.template_fields import TemplateFields  # noqa: F401


@dataclass(frozen=True)
class TemplateFieldValues:
    approved_or_received: str
    approvals_subdirectory: str
    file_extension: str
    relative_test_source_directory: str
    test_case_name: str
    test_file_name: str
    test_source_directory: str
    additional_information: str

    def with_(
        self, approved_or_received: str, file_extension: str
    ) -> "TemplateFieldValues":
        return replace(
            self,
            approved_or_received=approved_or_received,
            file_extension=file_extension,
        )

    def with_additional_information(
        self, additional_information: str
    ) -> "TemplateFieldValues":
        return replace(self, additional_information=additional_information)


class TemplatedCustomNamer(Namer):
    DEFAULT_TEMPLATE = (
        "{test_source_directory}/{approvals_subdirectory}/"
        "{test_file_name}.{test_case_name}{additional_information}.{approved_or_received}.{file_extension}"
    )

    def __init__(self, template: str) -> None:
        self.template = template
        self.extension_with_dot = ".txt"
        self.approvals_subdirectory: str | None = None
        self.additional_information: str | None = None

    def set_extension(self, extension_with_dot: str) -> None:
        self.extension_with_dot = extension_with_dot

    @override
    def get_received_filename(self) -> str:
        return self.format_filename(self.RECEIVED_WITHOUT_DOT)

    @override
    def get_approved_filename(self) -> str:
        return self.format_filename(self.APPROVED_WITHOUT_DOT)

    def format_filename(self, approved_or_received: str) -> str:
        fields = self._get_field_values().with_(
            approved_or_received, self.extension_with_dot[1:]
        )
        return TemplatedCustomNamer.create_filename(self.template, fields)

    def get_file_name(self) -> str:
        return TemplatedCustomNamer.create_filename(
            "{test_file_name}.{test_case_name}", self._get_field_values()
        )

    def get_basename(self) -> str:
        return TemplatedCustomNamer.create_filename(
            "{test_source_directory}/{approvals_subdirectory}/{test_file_name}.{test_case_name}",
            self._get_field_values(),
        )

    def _get_field_values(self) -> TemplateFieldValues:
        fields = self.get_template_fields_from_stacktrace()
        if self.approvals_subdirectory is not None:
            fields = replace(fields, approvals_subdirectory=self.approvals_subdirectory)
        return fields.with_additional_information(
            f".{self.additional_information}" if self.additional_information else ""
        )

    @staticmethod
    def create_filename(template: str, values: TemplateFieldValues) -> str:
        return template.format_map(asdict(values)).replace("//", "/")

    @staticmethod
    def get_template_fields_from_stacktrace() -> TemplateFieldValues:
        frame = stack_walker.get_test_frame()
        directory = os.path.dirname(frame[1])
        return TemplateFieldValues(
            approved_or_received="",
            approvals_subdirectory=stack_walker.load_config(directory).get(
                "subdirectory", ""
            ),
            file_extension="",
            relative_test_source_directory=os.path.relpath(directory).replace(
                os.sep, "/"
            ),
            test_case_name=frame[3],
            test_file_name=stack_walker.get_class_name_of_frame(frame),
            test_source_directory=directory,
            additional_information="",
        )
