import importlib
import inspect
import sys

from approvaltests import (
    DiffReporter,
    ReporterForTesting,
    approvals,
    combination_approvals,  # noqa: F401
    get_default_reporter,
    verify,
    verify_all,
)
from approvaltests.core.options import Options
from approvaltests.reporters import MultiReporter, ReportByCreatingDiffFile
from approvaltests.utilities import command_line_approvals  # noqa: F401
from approvaltests.utilities.logger import simple_logger_approvals  # noqa: F401
from approvaltests.utilities.logging import logging_approvals  # noqa: F401


def _is_approval_module(name: str) -> bool:
    return name.startswith("approvaltests.") and name.endswith("approvals")


_approvals_modules = sorted(filter(_is_approval_module, sys.modules.keys()))


def test_list_of_modules() -> None:
    verify_all("", _approvals_modules)


def test_every_function_in_approvals_with_verify_has_an_options() -> None:
    for module_name in _approvals_modules:
        assert_verify_methods_have_options(importlib.import_module(module_name))


def assert_verify_methods_have_options(module) -> None:
    for function_name, obj in module.__dict__.items():
        if "verify" not in function_name:
            continue

        if not callable(obj):
            continue

        # if it has a decorator, we need to get the original function
        if hasattr(obj, "__wrapped__"):
            obj = obj.__wrapped__

        argspec = inspect.getfullargspec(obj)
        has_options = "options" in argspec.kwonlyargs
        assert has_options, (
            f"Missing Keyword only parameter `options` in {function_name}:\n\t{argspec}"
        )


def test_empty_options_has_default_reporter() -> None:
    ##approvals.set_default_reporter(None)
    options = Options()
    assert options.reporter == get_default_reporter()


def test_with_reporter() -> None:
    testr = ReporterForTesting()
    options = Options().with_reporter(testr)
    try:
        verify("Data2", options=options)
    except:
        pass

    assert testr.called


def test_setting_reporter() -> None:
    testr = ReporterForTesting()
    options = Options().with_reporter(testr)
    assert options.reporter == testr


def test_file_extensions() -> None:
    approvals.settings().allow_multiple_verify_calls_for_this_method()
    content = "# This is a markdown header\n"
    # begin-snippet: options_with_file_extension
    verify(content, options=Options().for_file.with_extension(".md"))
    # end-snippet
    verify(content, options=Options().for_file.with_extension("md"))


def test_scrubber() -> None:
    options = Options().with_scrubber(lambda text: text.upper())
    verify("Hello, Approvals!", options=options)


def test_add_scrubber() -> None:
    options = (
        Options()
        .with_scrubber(lambda text: text.upper())
        .add_scrubber(lambda text: text.replace("!", "!!!"))
    )
    verify("Hello, Approvals!", options=options)


class MyCustomFileNamer(StackFrameNamer):
    @override
    def get_file_name(self) -> str:
        return "my_custom_file_name"


def test_namer() -> None:
    options = Options().with_namer(MyCustomFileNamer())
    verify("Hello, Approvals!", options=options)


def test_comparator() -> None:
    options = Options().with_comparator(IgnoreTrailingExclamationsComparator())
    verify("Hello, Approvals!!!", options=options)


def test_reporter() -> None:
    options = Options().with_reporter(ReportWithBeyondCompare())
    verify("Hello, Approvals!", options=options)


def test_overwrite_reporter() -> None:
    # current behaviour, override
    options0 = (
        Options()
        .with_reporter(ReportByCreatingDiffFile())
        .with_reporter(DiffReporter())
    )
    assert type(options0.reporter) == DiffReporter


def test_add_reporter() -> None:
    reporter1 = ReportByCreatingDiffFile()
    reporter2 = DiffReporter()
    handmade = MultiReporter(reporter1, reporter2)

    options0 = Options().with_reporter(reporter1).add_reporter(reporter2)
    assert str(options0.reporter) == str(handmade)

# Original Input = Hello, Approvals!
# apply scrubber = text.upper()
# Result = HELLO, APPROVALS!
# add scrubber = text.replace("!", "!!!")
# Result = HELLO, APPROVALS!!!
# use comparator = IgnoreTrailingExclamationsComparator()
# Result = True, because it compares 
#          received "HELLO, APPROVALS!!!" against
#          approved "HELLO, APPROVALS!" 
# NOTE: The trailing "!"s are stripped from both files before the compare
#          the effect is to IGNORE all trailing "!" characters

class UserSpecifiedFileNamer(StackFrameNamer):
    @override
    def get_file_name(self) -> str:
        return "test_demonstrate_available_approvaltests_options_renamed_by_user"


class IgnoreTrailingExclamationsComparator(Comparator):
    @override
    def compare(self, received_path: str, approved_path: str) -> bool:
        received = pathlib.Path(received_path).read_text().rstrip("!\n")
        approved = pathlib.Path(approved_path).read_text().rstrip("!\n")
        return received == approved

def test_demonstrate_available_approvaltests_options() -> None:
    # begin-snippet: options_with_all_options
    options = (
        Options()

        # write the .approved/.received files as Markdown instead of .txt
        .for_file.with_extension(".md")

        # uppercase the text before it is written/compared, so the effect
        # is visible in the received/approved files themselves
        .with_scrubber(lambda text: text.upper())

        # add_scrubber stacks an additional scrubber on top of any scrubbers already
        # added, instead of replacing them like with_scrubber would; here there's only
        # one scrubber (from with_scrubber above). The newly added scrubber turns "!"
        # into "!!!", which sets up the comparator below to show off what it ignores
        .add_scrubber(lambda text: text.replace("!", "!!!"))

        # use a custom namer, so the user controls the approved/received file names
        # directly, instead of having them derived from the test's own name
        .with_namer(UserSpecifiedFileNamer())

        # use a custom comparator that ignores trailing "!"s, so the mismatch
        # created by add_scrubber above still counts as approved
        .with_comparator(IgnoreTrailingExclamationsComparator())

        # launch Beyond Compare to review any mismatch
        .with_reporter(ReportWithBeyondCompare())
    )

    verify("Hello, Approvals!", options=options)
    # end-snippet
