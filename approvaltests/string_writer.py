import os

from approvaltests.core.writer import Writer


class StringWriter(Writer):
    contents = ''

    def __init__(self, contents, extension='.txt'):
        self.contents = contents or ''
        self.extension_with_dot = extension

    def write_received_file(self, received_file):
        self.create_directory_if_needed(received_file)
        with open(received_file, 'w') as f:
            f.write(self.contents)
        return received_file

    @staticmethod
    def create_directory_if_needed(received_file):
        directory = os.path.dirname(received_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
