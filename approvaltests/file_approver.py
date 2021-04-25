import filecmp
import os
import pathlib
from typing import Optional

from approvaltests.core.namer import Namer
from approvaltests.core.reporter import Reporter
from approvaltests.core.writer import Writer


def exists(path: str) -> bool:
    return os.path.isfile(path)


class ReporterNotWorkingException(Exception):
    def __init__(self, reporter: Reporter):
        super().__init__(f"Reporter {reporter} failed to work!")


class FileApprover(object):
    def verify(
        self,
        namer: Namer,
        writer: Writer,
        reporter: Reporter,
    ) -> Optional[str]:

        base = namer.get_basename()
        approved = namer.get_approved_filename(base)
        received = namer.get_received_filename(base)

        # The writer has the ability to change the name of the received file
        received = writer.write_received_file(received)
        ok = self.verify_files(approved, received, reporter)

        if not ok:
            return (
                f"Approval Mismatch, received != approved\n"
                f"\tApproved: {approved}\n"
                f"\tReceived: {received} "
            )
        return None

    def verify_files(
        self, approved_file: str, received_file: str, reporter: Reporter
    ) -> bool:
        if self.are_files_the_same(approved_file, received_file):
            os.remove(received_file)
            return True

        worked = reporter.report(received_file, approved_file)
        if not worked:
            raise ReporterNotWorkingException(reporter)
        return False

    @staticmethod
    def are_files_the_same(approved_file: str, received_file: str) -> bool:
        if not exists(approved_file) or not exists(received_file):
            return False
        if filecmp.cmp(approved_file, received_file):
            return True
        try:
            approved_raw = pathlib.Path(approved_file).read_text()
            approved_text = approved_raw.replace("\r\n", "\n")
            received_raw = pathlib.Path(received_file).read_text()
            received_text = received_raw.replace("\r\n", "\n")
            return approved_text == received_text
        except:
            return False
