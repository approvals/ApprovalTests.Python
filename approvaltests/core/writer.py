import os


class Writer(object):
    # interface

    def write_received_file(self, received_file):
        self.create_directory_if_needed(received_file)
        self._write_content_to_file(received_file)

    def _write_content_to_file(self, received_file):
        raise Exception("Interface member not implemented")

    @staticmethod
    def create_directory_if_needed(received_file):
        directory = os.path.dirname(received_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
