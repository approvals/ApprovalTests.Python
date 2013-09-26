import os
import filecmp


def exists(path):
    try:
        with open(path):
            pass
        return True
    except IOError:
        print('File does not exist ' + path)
        return False


class FileApprover(object):
    def verify(self, namer, writer, reporter):
        base = namer.get_basename()
        approved = writer.GetApprovedFileName(base)
        received = writer.write_received_file(writer.GetReceivedFileName(base))
        ok = self.verify_files(approved, received, reporter)
        if not ok:
            return "Approval Mismatch"
        return None

    def verify_files(self, approved_file, received_file, reporter):
        if self.are_files_the_same(approved_file, received_file):
            os.remove(received_file)
            return True

        reporter.report(approved_file, received_file)
        return False

    @staticmethod
    def are_files_the_same(approved_file, received_file):
        if not exists(approved_file) or not exists(received_file):
            return False

        if os.stat(approved_file).st_size != os.stat(received_file).st_size:
            return False
        else:
            return filecmp.cmp(approved_file, received_file)
