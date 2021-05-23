import xml.dom.minidom
from threading import local
from typing import Callable, List, Optional, Any

from approvaltests import to_json
from approvaltests.approval_exception import ApprovalException
from approvaltests.core import Reporter, Writer
from approvaltests.core.namer import StackFrameNamer, Namer
from approvaltests.core.options import Options
from approvaltests.core.scenario_namer import ScenarioNamer
from approvaltests.existing_file_writer import ExistingFileWriter
from approvaltests.file_approver import FileApprover
from approvaltests.list_utils import format_list
from approvaltests.reporters.diff_reporter import DiffReporter
from approvaltests.reporters.multi_reporter import MultiReporter
from approvaltests.string_writer import StringWriter

__unittest = True
__tracebackhide__ = True
DEFAULT_REPORTER = local()


def set_default_reporter(reporter: MultiReporter) -> None:
    global DEFAULT_REPORTER
    DEFAULT_REPORTER.v = reporter


def get_default_reporter() -> Reporter:
    if not hasattr(DEFAULT_REPORTER, "v") or DEFAULT_REPORTER.v is None:
        return DiffReporter()
    return DEFAULT_REPORTER.v


def get_reporter(reporter: Optional[Reporter]) -> Reporter:
    return reporter or get_default_reporter()


def get_default_namer(extension: Optional[str] = None) -> StackFrameNamer:
    return StackFrameNamer(extension)


def verify(
    data: Any,
    reporter: Optional[Reporter] = None,
    namer: Optional[Namer] = None,
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
    newline: Optional[str] = None,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
) -> None:
    """Verify string data against a previously approved version of the string.

    Args:
        data: A string containing the data to be compared with approved data from a previous run.
            On Python 2 this can be a bytes, str, or unicode object. On Python 3 this should be
            a str object.

        reporter: An optional Reporter. If None (the default), the default reporter
            will be used; see get_default_reporter().

        encoding: An optional encoding to be used when serialising the data to a byte stream for
            comparison. If None (the default) a locale-dependent encoding will be used; see
            locale.getpreferredencoding().

        errors: An optional string that specifies how encoding and decoding errors are to be handled
            If None (the default) or 'strict', raise a ValueError exception if there is an encoding
            error. Pass 'ignore' to ignore encoding errors. Pass 'replace' to use a replacement
            marker (such as '?') when there is malformed data.

        newline: An optional string that controls how universal newlines work when comparing data.
            It can be None, '', '\n', '\r', and '\r\n'. If None (the default) universal newlines are
            enabled and any '\n' characters are translated to the system default line separator
            given by os.linesep. If newline is '', no translation takes place. If newline is any of
            the other legal values, any '\n' characters written are translated to the given string.

    Raises:
        ApprovalException: If the verification fails because the given string does not match the
            approved string.

        ValueError: If data cannot be encoded using the specified encoding when errors is set to
            None or 'strict'.
    """
    options = initialize_options(options, reporter)
    namer_to_use = namer or options.namer
    verify_with_namer(
        data,
        namer_to_use,
        encoding=encoding,
        errors=errors,
        newline=newline,
        options=options,
    )


def initialize_options(
    options: Optional[Options], reporter: Optional[Reporter]
) -> Options:
    if options is None:
        options = Options()
    if reporter is not None:
        options = options.with_reporter(reporter)
    return options


def verify_with_namer(
    data: Any,
    namer: Namer,
    reporter: Optional[Reporter] = None,
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
    newline: Optional[str] = None,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
) -> None:
    """Verify string data against a previously approved version of the string.

    Args:
        data: A string containing the data to be compared with approved data from a previous run.
            On Python 2 this can be a bytes, str, or unicode object. On Python 3 this should be
            a str object.

        namer: A Namer instance used for naming approved and received data files.

        reporter: An optional Reporter. If None (the default), the default reporter
            will be used; see get_default_reporter().

        encoding: An optional encoding to be used when serialising the data to a byte stream for
            comparison. If None (the default) a locale-dependent encoding will be used; see
            locale.getpreferredencoding().

        errors: An optional string that specifies how encoding and decoding errors are to be handled
            If None (the default) or 'strict', raise a ValueError exception if there is an encoding
            error. Pass 'ignore' to ignore encoding errors. Pass 'replace' to use a replacement
            marker (such as '?') when there is malformed data.

        newline: An optional string that controls how universal newlines work when comparing data.
            It can be None, '', '\n', '\r', and '\r\n'. If None (the default) universal newlines are
            enabled and any '\n' characters are translated to the system default line separator
            given by os.linesep. If newline is '', no translation takes place. If newline is any of
            the other legal values, any '\n' characters written are translated to the given string.

    Raises:
        ApprovalException: If the verification fails because the given string does not match the
            approved string.

        ValueError: If data cannot be encoded using the specified encoding when errors is set to
            None or 'strict'.
    """
    options = initialize_options(options, reporter)
    writer = StringWriter(
        options.scrub(str(data)), encoding=encoding, errors=errors, newline=newline
    )
    verify_with_namer_and_writer(namer, writer, options.reporter)


def verify_with_namer_and_writer(
    namer: Namer,
    writer: Writer,
    reporter: Optional[Reporter],
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
) -> None:
    options = initialize_options(options, reporter)
    approver = FileApprover()
    error = approver.verify(namer, writer, options.reporter)
    if error:
        raise ApprovalException(error)


def verify_as_json(
    object,
    reporter=None,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
):
    options = initialize_options(options, reporter)
    n_ = to_json(object) + "\n"
    verify(n_, None, encoding="utf-8", newline="\n", options=options)


def verify_xml(
    xml_string: str,
    reporter: None = None,
    namer: Namer = None,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
) -> None:
    options = initialize_options(options, reporter)
    try:
        dom = xml.dom.minidom.parseString(xml_string)
        pretty_xml = dom.toprettyxml()
    except Exception:
        pretty_xml = xml_string

    verify(pretty_xml, options=options.for_file.with_extension(".xml"))


def verify_file(
    file_name: str,
    reporter: Reporter = None,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
) -> None:
    """Verify the contents of a text file against previously approved contents.

    Args:
        file_name: The path to a file. The file will be opened in text mode.

        reporter: An optional Reporter. If None (the default), the default reporter
            will be used; see get_default_reporter().


    Raises:
        ApprovalException: If the verification fails because the given string does not match the
            approved string.

        ValueError: If data cannot be encoded using the specified encoding when errors is set to
            None or 'strict'.
    """
    options = initialize_options(options, reporter)
    verify_with_namer_and_writer(
        get_default_namer(), ExistingFileWriter(file_name), None, options=options
    )


def verify_file_with_encoding(
    file_name,
    reporter=None,
    encoding=None,
    errors=None,
    newline=None,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
):
    """Deprecated. See verify_file. This function is functionally identical."""
    options = initialize_options(options, reporter)
    verify_file(file_name, None, encoding, errors, newline, options=options)


def verify_all(
    header: str,
    alist: List[str],
    formatter: Optional[Callable] = None,
    reporter: Optional[DiffReporter] = None,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
) -> None:
    """Verify a collection of items against a previously approved collection.

    Args:
        header: A header line string to be included before the list of items.

        alist: An iterable series of objects, a string representation of each of which will be
            included in an aggregated string for comparison.

        formatter: An optional object which must have a print_item(x) method such that
            formatter.print_item(x) will return a string representation of a single item from alist.

        reporter: An optional Reporter. If None (the default), the default reporter
            will be used; see get_default_reporter().

        encoding: An optional encoding to be used when serialising the data to a byte stream for
            comparison. If None (the default) a locale-dependent encoding will be used; see
            locale.getpreferredencoding().

        errors: An optional string that specifies how encoding and decoding errors are to be handled
            If None (the default) or 'strict', raise a ValueError exception if there is an encoding
            error. Pass 'ignore' to ignore encoding errors. Pass 'replace' to use a replacement
            marker (such as '?') when there is malformed data.

        newline: An optional string that controls how universal newlines work when comparing data.
            It can be None, '', '\n', '\r', and '\r\n'. If None (the default) universal newlines are
            enabled and any '\n' characters are translated to the system default line separator
            given by os.linesep. If newline is '', no translation takes place. If newline is any of
            the other legal values, any '\n' characters written are translated to the given string.

    Raises:
        ApprovalException: If the verification fails because the given string does not match the
            approved string.

        ValueError: If data cannot be encoded using the specified encoding when errors is set to
            None or 'strict'.
    """
    options = initialize_options(options, reporter)
    text = format_list(alist, formatter, header)
    verify(
        text, None, encoding=encoding, errors=errors, newline=newline, options=options
    )


def get_scenario_namer(scenario_name: int) -> ScenarioNamer:
    return ScenarioNamer(get_default_namer(), scenario_name)
