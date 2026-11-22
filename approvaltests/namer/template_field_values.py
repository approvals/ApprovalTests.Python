from dataclasses import dataclass, replace


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

    def add_additional_information(self, more: str) -> "TemplateFieldValues":
        return replace(
            self, additional_information=self.additional_information + "." + more
        )
