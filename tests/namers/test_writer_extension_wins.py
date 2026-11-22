import os

from approvaltests import Options, verify_all
from approvaltests.file_approver import FileApprover
from approvaltests.namer.stack_frame_namer import StackFrameNamer
from approvaltests.reporters.testing_reporter import ReporterForTesting
from approvaltests.string_writer import StringWriter


def test_writer_extension_wins_over_namer_extension() -> None:
    namer = StackFrameNamer()
    writer = StringWriter("hello", extension=".xml")
    error = FileApprover.verify(namer, writer, ReporterForTesting(), Options().comparator)
    assert error is not None
    lines = [os.path.basename(line.strip()) for line in error.splitlines()[1:]]
    verify_all("Names used by FileApprover.verify", lines)
    os.remove(namer.get_received_file(".xml"))
