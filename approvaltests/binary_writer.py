import io

from approvaltests.core import Writer


class BinaryWriter(Writer):
    contents = ''

    def __init__(self, contents):
        self.contents = contents

    def _write_content_to_file(self, received_file):
        with io.open(
            received_file,
            mode='wb'
        ) as f:
            f.write(self.contents)

        return received_file
