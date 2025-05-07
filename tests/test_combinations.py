import unittest

from typing_extensions import override

from approvaltests.approval_exception import ApprovalException
from approvaltests.combination_approvals import (
    verify_all_combinations,
    verify_all_combinations_with_labeled_input,
    verify_all_combinations_with_namer,
)
from approvaltests.reporters import CommandLineReporter
from approvaltests.reporters.testing_reporter import ReporterForTesting


class VerifyAllCombinationsTests(unittest.TestCase):
    @override
    def setUp(self) -> None:
        self.reporter = None
        self.func = lambda *args: sum(args) + 1

    def test_fails_for_mismatch_with_for_func_accepting_one_arg_and_combination_of_one_arg(
        self,
    ) -> None:
        arg1_combinations = (1,)
        all_args_combinations = (arg1_combinations,)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(
                self.func, all_args_combinations, reporter=ReporterForTesting()
            )

    def test_passes_for_func_accepting_one_arg_and_combination_of_one_arg(self) -> None:
        arg1_combinations = (1,)
        all_args_combinations = (arg1_combinations,)
        verify_all_combinations(
            self.func, all_args_combinations, reporter=self.reporter
        )

    def test_fails_for_mismatch_with_for_func_accepting_one_arg_and_combination_of_two_args(
        self,
    ) -> None:
        arg1_combinations = (1, 2)
        all_args_combinations = (arg1_combinations,)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(
                self.func, all_args_combinations, reporter=ReporterForTesting()
            )

    def test_passes_for_func_accepting_one_arg_and_combination_of_two_args(
        self,
    ) -> None:
        arg1_combinations = (1, 2)
        all_args_combinations = (arg1_combinations,)
        verify_all_combinations(
            self.func, all_args_combinations, reporter=self.reporter
        )

    def test_fails_for_mismatch_with_for_func_accepting_two_args_and_combination_of_one_arg(
        self,
    ) -> None:
        arg1_combinations = (1,)
        arg2_combinations = (2,)
        arg_combinations = (arg1_combinations, arg2_combinations)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(
                self.func, arg_combinations, reporter=ReporterForTesting()
            )

    def test_passes_for_func_accepting_two_args_and_combination_of_one_arg(
        self,
    ) -> None:
        arg1_combinations = (1,)
        arg2_combinations = (2,)
        arg_combinations = (arg1_combinations, arg2_combinations)
        verify_all_combinations(self.func, arg_combinations, reporter=self.reporter)

    def test_fails_for_mismatch_with_for_func_accepting_two_args_and_combination_of_two_args(
        self,
    ) -> None:
        arg1_combinations = (1, 3)
        arg2_combinations = (2, 4)
        arg_combinations = (arg1_combinations, arg2_combinations)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(
                self.func, arg_combinations, reporter=ReporterForTesting()
            )

    def test_for_func_accepting_three_args_and_combination_of_three_args(self) -> None:
        arg1_combinations = (1, 2, 3)
        arg2_combinations = (2, 4, 6)
        arg3_combinations = (10, 11, 12)
        arg_combinations = [arg1_combinations, arg2_combinations, arg3_combinations]
        verify_all_combinations(self.func, arg_combinations, reporter=self.reporter)

    def test_when_arg_combinations_have_equal_lengths(self) -> None:
        arg1_combinations = (1, 3, 5, 7)
        arg2_combinations = (2, 4, 6)
        arg_combinations = (arg1_combinations, arg2_combinations)
        verify_all_combinations(self.func, arg_combinations, reporter=self.reporter)

    def test_records_exception_message_when_function_under_test_throws_an_exception(
        self,
    ) -> None:
        def function_that_raises_exceptions(*args: object) -> None:
            raise Exception(args)

        arg1_combinations = (1, 3)
        arg2_combinations = (2, 4)
        arg_combinations = (arg1_combinations, arg2_combinations)
        verify_all_combinations(
            function_that_raises_exceptions, arg_combinations, reporter=self.reporter
        )

    def test_uses_user_specified_formatter_when_supplied(self) -> None:
        arg1_combinations = (1, 3)
        arg2_combinations = (2, 4)
        arg_combinations = (arg1_combinations, arg2_combinations)
        verify_all_combinations(
            self.func,
            arg_combinations,
            formatter=lambda args, output: "inputs="
            + str(args)
            + ", outputs="
            + str(output)
            + "\n",
            reporter=self.reporter,
        )

    def test_with_labeled_input(self) -> None:
        # begin-snippet: named_combinations
        verify_all_combinations_with_labeled_input(
            self.func,
            arg1=(1, 3),
            arg2=(2, 4),
        )
        # end-snippet


class VerifyAllCombinationsWithNamerTests(unittest.TestCase):
    @override
    def setUp(self) -> None:
        self.reporter = CommandLineReporter()
        self.func = lambda *args: sum(args) + 1

    def test_passes_for_func_accepting_one_arg_and_combination_of_one_arg(self) -> None:
        arg1_combinations = (1,)
        all_args_combinations = (arg1_combinations,)
        verify_all_combinations_with_namer(
            self.func, all_args_combinations, reporter=self.reporter
        )


def test_example_for_combinations() -> None:
    # begin-snippet: combination_introduction
    verify_all_combinations(is_awake, [["Monday", "Sunday"], ["7:00", "9:00", "11:00"]])
    # end-snippet


def test_starting_snippet() -> None:
    # begin-snippet: combinations_starting_point
    inputs1 = ["input1.value1", "input1.value2"]
    inputs2 = ["input2.value1", "input2.value2", "input2.value3"]
    verify_all_combinations(lambda a, b: "placeholder", [inputs1, inputs2])
    # end-snippet


def is_awake(day: str, time) -> str:
    weekdays = ["Monday"]
    is_weekday = day in weekdays
    time = int(time.replace(":00", ""))
    if is_weekday and time > 8:
        return "Yes"
    elif not is_weekday and time < 10:
        return "No"
    else:
        return "Maybe"
