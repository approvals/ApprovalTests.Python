import shutil

from approvaltests.core import Writer


class ExistingFileWriter(Writer):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def write_received_file(self, received_file: str) -> str:
        shutil.copyfile(self.file_name, received_file)
        return received_file
