import json
from threading import local

from approvaltests.approval_exception import ApprovalException
from approvaltests.core.namer import Namer
from approvaltests.file_approver import FileApprover
from approvaltests.reporters.diff_reporter import DiffReporter
from approvaltests.string_writer import StringWriter

DEFAULT_REPORTER = local()


def set_default_reporter(reporter):
    global DEFAULT_REPORTER
    DEFAULT_REPORTER.v = reporter
    

def get_default_reporter():
    if not hasattr(DEFAULT_REPORTER, "v") or DEFAULT_REPORTER.v is None:
        return DiffReporter()
    return DEFAULT_REPORTER.v


def verify(data, reporter=None):
    verify_with_namer(data, get_default_namer(), reporter)


def verify_with_namer(data, namer, reporter):
    reporter = get_reporter(reporter)
    approver = FileApprover()
    writer = StringWriter(data)
    error = approver.verify(namer, writer, reporter)
    if error is not None:
        raise ApprovalException(error)


def get_reporter(reporter):
    if reporter is None:
        reporter = get_default_reporter()
    return reporter


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


def verify_file(file_name, reporter=None):
    with open(file_name, 'r') as f:
        file_contents = f.read()
        verify(file_contents, reporter)


