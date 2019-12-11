from threading import local
import xml.dom.minidom

from approvaltests import to_json
from approvaltests.approval_exception import ApprovalException
from approvaltests.core.namer import Namer
from approvaltests.core.scenario_namer import ScenarioNamer
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
    return reporter or get_default_reporter()


def get_default_namer():
    return Namer()


def verify(data, reporter=None, namer=None):
    reporter_to_use = reporter or get_default_reporter()
    namer_to_use = namer or get_default_namer()
    verify_with_namer(data, namer_to_use, reporter_to_use)


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


def verify_xml(xml_string, reporter=None):
    try:
        dom = xml.dom.minidom.parseString(xml_string)
        pretty_xml = dom.toprettyxml()
    except Exception:
        pretty_xml = xml_string
    verify_with_namer(pretty_xml, Namer(extension='.xml'), reporter)


def verify_file(file_name, reporter=None):
    with open(file_name, 'r') as f:
        file_contents = f.read()
    verify(file_contents, reporter)


def verify_all(header, alist, formatter=None, reporter=None):
    text = format_list(alist, formatter, header)
    verify(text, reporter)


def get_scenario_namer(scenario_name):
    return ScenarioNamer(get_default_namer(), scenario_name)