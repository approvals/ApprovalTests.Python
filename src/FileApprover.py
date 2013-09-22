import os
import filecmp

class FileApprover(object):
    def verify(self, namer, writer, reporter):
        base = namer.get_basename()
        approved = writer.GetApprovedFileName(base)
        received = writer.WriteReceivedFile(writer.GetReceivedFileName(base))
        self.verify_files(approved, received, reporter)

    def verify_files(self, approved_file, received_file, reporter):
        if(self.are_files_the_same(approved_file, received_file)):
            os.remove(received_file)
        else:
            reporter.report(approved_file, received_file)

    def are_files_the_same(self, approved_file, received_file):
        if(not self.FileExists(approved_file) or not self.FileExists(received_file)):
            return False

        if(os.stat(approved_file).st_size != os.stat(received_file).st_size):
            return False
        else:
            return filecmp.cmp(approved_file, received_file)

    def FileExists(self, path):
        try:
            with open(path): pass
            return True
        except IOError:
            print ('File does not exist ' + path)
            return False
