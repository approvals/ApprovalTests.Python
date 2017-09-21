import filecmp
import os


def exists(path):
    return os.path.isfile(path)


class FileApprover(object):
    def verify(self, namer, writer, reporter):

        base = namer.get_basename()
        approved = namer.get_approved_filename(base)
        received = namer.get_received_filename(base)

        writer.write_received_file(received)
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

        if os.stat(approved_file).st_size != os.stat(received_file).st_size:
            return False
        else:
            return filecmp.cmp(approved_file, received_file)
