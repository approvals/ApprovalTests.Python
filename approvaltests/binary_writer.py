from typing import Union

from typing_extensions import override

from approval_utilities.utils import create_directory_if_needed
from approvaltests.core.writer import Writer

# typing.ByteString was removed in Python 3.14
_ByteString = Union[bytes, bytearray, memoryview]


class BinaryWriter(Writer):
    contents: _ByteString

    def __init__(
        self,
        contents: _ByteString,
        extension: str,
    ) -> None:
        self.contents = contents
        self.extension_with_dot = extension

    @override
    def write_received_file(self, received_file: str) -> str:
        create_directory_if_needed(received_file)
        with open(received_file, mode="wb") as file:
            file.write(self.contents)

        return received_file
