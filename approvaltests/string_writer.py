import io
import os
import sys

from approvaltests.core.writer import Writer


class StringWriter(Writer):
    contents = ''

    def __init__(self, contents, extension='.txt', encoding=None, errors=None, newline=None):
        if sys.version_info.major == 2 and isinstance(contents, str):
            contents = contents.decode("ascii")
        self.contents = contents or u''
        self.extension_with_dot = extension
        self.encoding = encoding
        self.errors = errors
        self.newline = newline

    def _write_content_to_file(self, received_file):
        with io.open(
                received_file,
                mode='wt',
                encoding=self.encoding,
                errors=self.errors,
                newline=self.newline
        ) as f:
            f.write(self.contents)
        return received_file
