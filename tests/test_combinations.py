import unittest

from approvaltests.approval_exception import ApprovalException
from approvaltests import (
    verify_all_combinations,
    verify_all_combinations_with_namer,
    get_default_namer,
)
from approvaltests.reporters import CommandLineReporter
from approvaltests.reporters.testing_reporter import ReporterForTesting


class VerifyAllCombinationsTests(unittest.TestCase):
    def setUp(self):
        self.reporter = None
        self.func = lambda *args: sum(args) + 1

    def test_fails_for_mismatch_with_for_func_accepting_one_arg_and_combination_of_one_arg(
        self,
    ):
        arg1_combinations = (1,)
        all_args_combinations = (arg1_combinations,)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(
                self.func, all_args_combinations, reporter=ReporterForTesting()
            )

    def test_passes_for_func_accepting_one_arg_and_combination_of_one_arg(self):
        arg1_combinations = (1,)
        all_args_combinations = (arg1_combinations,)
        verify_all_combinations(
            self.func, all_args_combinations, reporter=self.reporter
        )

    def test_fails_for_mismatch_with_for_func_accepting_one_arg_and_combination_of_two_args(
        self,
    ):
        arg1_combinations = (1, 2)
        all_args_combinations = (arg1_combinations,)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(
                self.func, all_args_combinations, reporter=ReporterForTesting()
            )

    def test_passes_for_func_accepting_one_arg_and_combination_of_two_args(self):
        arg1_combinations = (1, 2)
        all_args_combinations = (arg1_combinations,)
        verify_all_combinations(
            self.func, all_args_combinations, reporter=self.reporter
        )

    def test_fails_for_mismatch_with_for_func_accepting_two_args_and_combination_of_one_arg(
        self,
    ):
        arg1_combinations = (1,)
        arg2_combinations = (2,)
        arg_combinations = (arg1_combinations, arg2_combinations)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(
                self.func, arg_combinations, reporter=ReporterForTesting()
            )

    def test_passes_for_func_accepting_two_args_and_combination_of_one_arg(self):
        arg1_combinations = (1,)
        arg2_combinations = (2,)
        arg_combinations = (arg1_combinations, arg2_combinations)
        verify_all_combinations(self.func, arg_combinations, reporter=self.reporter)

    def test_fails_for_mismatch_with_for_func_accepting_two_args_and_combination_of_two_args(
        self,
    ):
        arg1_combinations = (1, 3)
        arg2_combinations = (2, 4)
        arg_combinations = (arg1_combinations, arg2_combinations)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(
                self.func, arg_combinations, reporter=ReporterForTesting()
            )

    def test_for_func_accepting_three_args_and_combination_of_three_args(self):
        arg1_combinations = (1, 2, 3)
        arg2_combinations = (2, 4, 6)
        arg3_combinations = (10, 11, 12)
        arg_combinations = (arg1_combinations, arg2_combinations, arg3_combinations)
        verify_all_combinations(self.func, arg_combinations, reporter=self.reporter)

    def test_when_arg_combinations_have_equal_lengths(self):
        arg1_combinations = (1, 3, 5, 7)
        arg2_combinations = (2, 4, 6)
        arg_combinations = (arg1_combinations, arg2_combinations)
        verify_all_combinations(self.func, arg_combinations, reporter=self.reporter)

    def test_records_exception_message_when_function_under_test_throws_an_exception(
        self,
    ):
        class BackwardCompatibleException(Exception):
            """Exception with repr that's the same for pre 3.7 and 3.7+.

            Python3.7 got rid of the trailing comma in the `repr` of `BaseException`: https://bugs.python.org/issue30399
            """

            def __repr__(self):
                return "Exception{}".format(self.args)

        def function_that_raises_exceptions(*args):
            raise BackwardCompatibleException(args)

        arg1_combinations = (1, 3)
        arg2_combinations = (2, 4)
        arg_combinations = (arg1_combinations, arg2_combinations)
        verify_all_combinations(
            function_that_raises_exceptions, arg_combinations, reporter=self.reporter
        )

    def test_uses_user_specified_formatter_when_supplied(self):
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


class VerifyAllCombinationsWithNamerTests(unittest.TestCase):
    def setUp(self):
        self.reporter = ReporterForTesting()
        self.reporter = CommandLineReporter()
        self.func = lambda *args: sum(args) + 1

    def test_passes_for_func_accepting_one_arg_and_combination_of_one_arg(self):
        arg1_combinations = (1,)
        all_args_combinations = (arg1_combinations,)
        namer = get_default_namer()
        verify_all_combinations_with_namer(
            self.func, all_args_combinations, namer, reporter=self.reporter
        )
