import json

from approvaltests.ApprovalException import ApprovalException
from approvaltests.FileApprover import FileApprover
from approvaltests.Namer import Namer
from approvaltests.ReceivedFileLauncherReporter import ReceivedFileLauncherReporter
from approvaltests.StringWriter import StringWriter


def verify(data, reporter=ReceivedFileLauncherReporter()):
    approver = FileApprover()
    namer = Namer()
    writer = StringWriter(data)

    error = approver.verify(namer, writer, reporter)
    if error is not None:
        raise ApprovalException(error)

def verify_as_json(object, reporter=ReceivedFileLauncherReporter()):
    n_ = to_json(object) + "\n"
    verify(n_, reporter)

def to_json(object):
    return json.dumps(
        object,
        sort_keys=True,
        indent=4,
        separators=(',', ': '),
        default=lambda o: o.__dict__)
