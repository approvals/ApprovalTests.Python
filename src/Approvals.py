from ApprovalException import ApprovalException
from FileApprover import FileApprover
from Namer import Namer
from ReceivedFileLauncherReporter import ReceivedFileLauncherReporter
from StringWriter import StringWriter


def verify(data, reporter=ReceivedFileLauncherReporter()):
    approver = FileApprover()
    namer = Namer(2)
    writer = StringWriter(data)

    error = approver.verify(namer, writer, reporter)
    if(error is not None):
        raise ApprovalException(error)
