import filecmp
import os
import pathlib


def exists(path):
    return os.path.isfile(path)


class FileApprover(object):
    def verify(self, namer, writer, reporter):

        base = namer.get_basename()
        approved = namer.get_approved_filename(base)
        received = namer.get_received_filename(base)

        # The writer has the ability to change the name of the received file
        received = writer.write_received_file(received)
        ok = self.verify_files(approved, received, reporter)
        if not ok:
            return "Approval Mismatch"
        return None

    def verify_files(self, approved_file, received_file, reporter):
        if self.are_files_the_same(approved_file, received_file):
            os.remove(received_file)
            return True

        reporter.report(received_file, approved_file)
        return False

    @staticmethod
    def are_files_the_same(approved_file, received_file):
        if not exists(approved_file) or not exists(received_file):
            return False
        if filecmp.cmp(approved_file,received_file):
            return True
        try:
            approved_raw = pathlib.Path(approved_file).read_text()
            approved_text = approved_raw.replace("\r\n", "\n")
            received_raw = pathlib.Path(received_file).read_text()
            received_text = received_raw.replace("\r\n", "\n")
            return approved_text == received_text
        except:
            return False
