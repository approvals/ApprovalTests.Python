from threading import local

from approvaltests import to_json
from approvaltests.approval_exception import ApprovalException
from approvaltests.core.namer import Namer
from approvaltests.file_approver import FileApprover
from approvaltests.list_utils import format_list
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

def get_reporter(reporter):
    if reporter is None:
        reporter = get_default_reporter()
    return reporter


def get_default_namer():
    return Namer()


def verify(data, reporter=None):
    verify_with_namer(data, get_default_namer(), reporter)


def verify_with_namer(data, namer, reporter):
    reporter = get_reporter(reporter)
    approver = FileApprover()
    writer = StringWriter(data)
    error = approver.verify(namer, writer, reporter)
    if error is not None:
        raise ApprovalException(error)


def verify_as_json(object, reporter=None):
    n_ = to_json(object) + "\n"
    verify(n_, reporter)


def verify_file(file_name, reporter=None):
    with open(file_name, 'r') as f:
        file_contents = f.read()
    verify(file_contents, reporter)

def verify_all(header, alist, formatter=None, reporter=None):
    text = format_list(alist, formatter, header)
    verify(text, reporter)


