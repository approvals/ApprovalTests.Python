from unittest import TestCase

from typing_extensions import override

from approvaltests import approvals
from approvaltests.reporters.clipboard_reporter import CommandLineReporter
from approvaltests.reporters.diff_reporter import DiffReporter
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter
from approvaltests.reporters.multi_reporter import MultiReporter


class TestList(TestCase):
    @override
    def setUp(self) -> None:
        reporter = MultiReporter(
            GenericDiffReporter.create("diff"), CommandLineReporter()
        )
        ##approvals.set_default_reporter(reporter)

    def test(self) -> None:
        alist = ["a", "b", "c", "d", "e"]
        approvals.verify_all("letters", alist, reporter=DiffReporter())

    def test_uppercase(self) -> None:
        alist = ["a", "b", "c", "d"]
        approvals.verify_all("uppercase", alist, lambda x: f"{x} => {x.upper()}")

    def test_starting_snippet(self) -> None:
        # begin-snippet: verify_all_starting_point
        inputs = ["input.value1", "input.value2"]
        approvals.verify_all("TITLE", inputs, lambda s: f"placeholder {s}")
        # end-snippet

    def test_format_line_part1(self) -> None:
        # This is part one of a test which reproduces the issue #32
        alist = ["1", "2", "3"]
        approvals.verify_all("index", alist, reporter=DiffReporter())

    def test_format_line_part2(self) -> None:
        # This is a part two of a test that would reproduce a bug where
        # `verify_all` does not reset index when called from two different tests.
        # More details in issue #32
        alist = ["1", "2", "3"]
        approvals.verify_all("index", alist, reporter=DiffReporter())
