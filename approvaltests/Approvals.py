import json
from threading import local


from approvaltests.ApprovalException import ApprovalException
from approvaltests.FileApprover import FileApprover
from approvaltests.Namer import Namer
from approvaltests.ReceivedFileLauncherReporter import ReceivedFileLauncherReporter
from approvaltests.StringWriter import StringWriter
from approvaltests.reporters.diff_reporter import DiffReporter

DEFAULT_REPORTER = local()


def set_default_reporter(reporter):
    global DEFAULT_REPORTER
    DEFAULT_REPORTER.v = reporter
    

def get_default_reporter():
    if not hasattr(DEFAULT_REPORTER, "v") or DEFAULT_REPORTER.v is None:
        return DiffReporter()
    return DEFAULT_REPORTER.v


def verify(data, reporter=None):
    if reporter is None:
        reporter = get_default_reporter()
    approver = FileApprover()
    namer = get_default_namer()
    writer = StringWriter(data)

    error = approver.verify(namer, writer, reporter)
    if error is not None:
        raise ApprovalException(error)


def get_default_namer():
    return Namer()


def verify_all(header, alist, formatter=None, reporter=None):
    if formatter is None:
        formatter = PrintList().print_item 
    text = header + '\n\n'
    for i in alist:
        text += formatter(i) + '\n'
    verify(text, reporter)


def verify_as_json(object, reporter=None):
    n_ = to_json(object) + "\n"
    verify(n_, reporter)

def to_json(object):
    return json.dumps(
        object,
        sort_keys=True,
        indent=4,
        separators=(',', ': '),
        default=lambda o: o.__dict__)


class PrintList(object):
    index = 0

    @classmethod
    def print_item(cls, x):
        text = str(cls.index) + ') ' + str(x)
        cls.index += 1
        return text
