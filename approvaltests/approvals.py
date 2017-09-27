import codecs
import json
import tempfile
from itertools import product
from threading import local


from approvaltests.approval_exception import ApprovalException
from approvaltests.file_approver import FileApprover
from approvaltests.core.namer import Namer
from approvaltests.string_writer import StringWriter
from approvaltests.reporters.diff_reporter import DiffReporter

DEFAULT_REPORTER = local()


def assert_equal_with_reporter(expected, actual, reporter=None):
    if actual == expected:
        return

    name = get_default_namer().get_file_name()
    expected_file = write_to_temporary_file(expected, name + '.expected.')
    actual_file = write_to_temporary_file(actual, name + '.actual.')
    get_reporter(reporter).report(actual_file, expected_file)
    raise AssertionError('expected != actual\n  actual: "{}"\nexpected: "{}"'.format(actual, expected))


def write_to_temporary_file(expected, name):
    with tempfile.NamedTemporaryFile(mode='w+b', suffix='.txt', prefix=name, delete=False) as temp:
        temp.write(expected.encode('utf-8-sig'))
        return temp.name


def set_default_reporter(reporter):
    global DEFAULT_REPORTER
    DEFAULT_REPORTER.v = reporter
    

def get_default_reporter():
    if not hasattr(DEFAULT_REPORTER, "v") or DEFAULT_REPORTER.v is None:
        return DiffReporter()
    return DEFAULT_REPORTER.v


def verify(data, reporter=None):
    reporter = get_reporter(reporter)
    approver = FileApprover()
    namer = get_default_namer()
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


def verify_all_combinations(function_under_test, input_arguments, formatter=None, reporter=None):
    """Run func with all possible combinations of args and verify outputs against the recorded approval file.

    Args:
        function_under_test (function): function under test.
        input_arguments: list of values to test for each input argument.  For example, a function f(product, quantity)
            could be tested with the input_arguments [['water', 'cola'], [1, 4]], which would result in outputs for the
            following calls being recorded and verified: f('water', 1), f('water', 4), f('cola', 1), f('cola', 4).
        formatter (function): function for formatting the function inputs/outputs before they are recorded to an
            approval file for comparison.
        reporter (approvaltests.reporter.Reporter): an approval reporter.

    Raises:
        ApprovalException: if the results to not match the approved results.
    """
    if formatter is None:
        formatter = args_and_result_formatter
    approval_strings = []
    for args in product(*input_arguments):
        try:
            result = function_under_test(*args)
        except Exception as e:
            result = e
        approval_strings.append(formatter(args, result))
    verify(''.join(approval_strings), reporter=reporter)


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


def args_and_result_formatter(args, result):
    return 'args: {} => {}\n'.format(repr(args), repr(result))

  
def verify_file(file_name, reporter=None):
    with open(file_name, 'r') as f:
        file_contents = f.read()
        verify(file_contents, reporter)
