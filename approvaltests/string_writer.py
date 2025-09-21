from typing import Optional

from typing_extensions import override

from approval_utilities.utils import create_directory_if_needed
from approvaltests.core.writer import Writer


class StringWriter(Writer):
    contents: str = ""

    def __init__(
        self,
        contents: Optional[str],
        extension: str = ".txt",
        encoding: Optional[str] = None,
        errors: Optional[str] = None,
        newline: Optional[str] = None,
    ) -> None:
        self.contents = StringWriter.sanitize_string(contents)
        self.extension_with_dot = extension
        self.encoding = encoding or "utf-8"
        self.errors = errors
        self.newline = newline

    @staticmethod
    def sanitize_string(contents: Optional[str]) -> str:
        contents = contents or ""
        if len(contents) == 0 or contents[-1] != "\n":
            contents = contents + "\n"
        return contents

    @override
    def write_received_file(self, received_file: str) -> str:
        create_directory_if_needed(received_file)
        with open(
            received_file,
            mode="w",
            encoding=self.encoding,
            errors=self.errors,
            newline=self.newline,
        ) as file:
            file.write(self.contents)
        return received_file
