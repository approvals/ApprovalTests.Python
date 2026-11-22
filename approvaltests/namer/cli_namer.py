from typing_extensions import override

from approvaltests.core.namer import Namer
from approvaltests.namer.templated_custom_namer import (
    TemplatedCustomNamer,
    TemplateFieldValues,
)


class CliNamer(Namer):
    # test_id is not a template field of its own, so it is carried in test_case_name
    TEMPLATE = "{test_case_name}.{approved_or_received}.{file_extension}"

    def __init__(self, test_id: str) -> None:
        self.test_id = test_id

    def _create_filename(
        self, approved_or_received: str, extension_with_dot: str = ".txt"
    ) -> str:
        values = TemplateFieldValues(
            approved_or_received=approved_or_received,
            approvals_subdirectory="",
            file_extension=extension_with_dot[1:],
            relative_test_source_directory="",
            test_case_name=self.test_id,
            test_file_name="",
            test_source_directory="",
            additional_information="",
        )
        return TemplatedCustomNamer.create_filename(self.TEMPLATE, values)

    @override
    def get_received_filename(self) -> str:
        return self._create_filename(Namer.RECEIVED_WITHOUT_DOT)

    @override
    def get_approved_filename(self) -> str:
        return self._create_filename(Namer.APPROVED_WITHOUT_DOT)

    def get_approved_file(self, extension_with_dot: str) -> str:
        return self._create_filename(Namer.APPROVED_WITHOUT_DOT, extension_with_dot)

    def get_received_file(self, extension_with_dot: str) -> str:
        return self._create_filename(Namer.RECEIVED_WITHOUT_DOT, extension_with_dot)

    def get_basename(self) -> str:
        return self.test_id
