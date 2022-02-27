import shutil

from approvaltests.core import Options
from approvaltests.core import Writer


class ExistingFileWriter(Writer):
    def __init__(self, file_name: str, options: Options) -> None:
        self.file_name = file_name
        self.options = options

    def write_received_file(self, received_file: str) -> str:
        if not self.options.has_scrubber():
            shutil.copyfile(self.file_name, received_file)
        else:
            with open(self.file_name, mode="r") as file:
                text = file.read()
            text = self.options.scrub(text)
            with open(received_file, mode="w") as file:
                file.write(text)
        return received_file
