import io
import os
import sys
from typing import Optional

from approvaltests.core.writer import Writer


class StringWriter(Writer):
    contents = ""

    def __init__(
        self,
        contents: str,
        extension: str = ".txt",
        encoding: Optional[str] = None,
        errors: Optional[str] = None,
        newline: Optional[str] = None,
    ) -> None:
        self.contents = contents or u""
        self.extension_with_dot = extension
        self.encoding = encoding
        self.errors = errors
        self.newline = newline

    def write_received_file(self, received_file: str) -> str:
        self.create_directory_if_needed(received_file)
        with io.open(
            received_file,
            mode="wt",
            encoding=self.encoding,
            errors=self.errors,
            newline=self.newline,
        ) as f:
            f.write(self.contents)
        return received_file

    @staticmethod
    def create_directory_if_needed(received_file: str) -> None:
        directory = os.path.dirname(received_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
