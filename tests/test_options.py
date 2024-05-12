import inspect

from approvaltests import (
    get_default_reporter,
    approvals,
    verify,
    ReporterForTesting,
    combination_approvals,
)
from approvaltests.core.options import Options
from approvaltests.mrjob import mrjob_approvals
from approvaltests.reporters import ReportByCreatingDiffFile, MultiReporter
from approvaltests.reporters.report_with_beyond_compare import ReportWithPycharm
from approvaltests.utilities import command_line_approvals
from approvaltests.utilities.logger import simple_logger_approvals


def test_every_function_in_approvals_with_verify_has_an_options():
    assert_verify_methods_have_options(approvals)
    assert_verify_methods_have_options(combination_approvals)
    assert_verify_methods_have_options(simple_logger_approvals)
    assert_verify_methods_have_options(command_line_approvals)
    assert_verify_methods_have_options(mrjob_approvals)


def assert_verify_methods_have_options(module):
    for function_name, obj in module.__dict__.items():
        if "verify" not in function_name:
            continue

        if not callable(obj):
            continue

        argspec = inspect.getfullargspec(obj)
        has_options = "options" in argspec.kwonlyargs
        assert (
            has_options
        ), f"Missing Keyword only parameter `options` in {function_name}:\n\t{argspec}"


def test_empty_options_has_default_reporter():
    ##approvals.set_default_reporter(None)
    options = Options()
    assert options.reporter == get_default_reporter()


def test_with_reporter():
    testr = ReporterForTesting()
    options = Options().with_reporter(testr)
    try:
        verify("Data2", options=options)
    except:
        pass

    assert testr.called


def test_setting_reporter():
    testr = ReporterForTesting()
    options = Options().with_reporter(testr)
    assert options.reporter == testr


def test_file_extensions():
    approvals.settings().allow_multiple_verify_calls_for_this_method()
    content = "# This is a markdown header\n"
    # begin-snippet: options_with_file_extension
    verify(content, options=Options().for_file.with_extension(".md"))
    # end-snippet
    verify(content, options=Options().for_file.with_extension("md"))


def test_add_reporter():
    # current behaviour, override
    options0 = (
        Options()
        .with_reporter(ReportByCreatingDiffFile())
        .with_reporter(ReportWithPycharm())
    )
    assert type(options0.reporter) == ReportWithPycharm

    # current work around, create a MultiReporter
    options_multi = Options().with_reporter(
        MultiReporter(ReportByCreatingDiffFile(), ReportWithPycharm())
    )
    assert (
        str(options_multi.reporter)
        == "MultiReporter(ReportByCreatingDiffFile, ReportWithPycharm)"
    )

    # new behaviour, append
    options0 = (
        Options()
        .with_reporter(ReportByCreatingDiffFile())
        .add_reporter(ReportWithPycharm())
    )
    assert (
        str(options_multi.reporter)
        == "MultiReporter(ReportByCreatingDiffFile, ReportWithPycharm)"
    )
