import unittest

from approvaltests.ApprovalException import ApprovalException
from approvaltests.Approvals import verify, verify_as_json, verify_all_combinations
from approvaltests.GenericDiffReporterFactory import GenericDiffReporterFactory
from approvaltests.TestingReporter import TestingReporter


class VerifyTests(unittest.TestCase):
    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get('BeyondCompare4Mac')

    def test_verify(self):
        verify("Hello World.", self.reporter)

    def test_verify_fail(self):
        reporter = TestingReporter()
        try:
            verify("Hello World.", reporter)
            self.assertFalse(True, "expected exception")
        except ApprovalException as e:
            self.assertTrue("Approval Mismatch", e.value)

    def test_verify_as_json(self):
        class Bag(object):
            def __init__(self):
                self.stuff = 1
                self.json = None

        o = Bag()
        o.json = {
            "a": 0,
            "z": 26
        }
        verify_as_json(o, self.reporter)


class VerifyAllCombinationsTests(unittest.TestCase):
    def setUp(self):
        self.reporter = TestingReporter()
        self.func = lambda *args: sum(args) + 1

    def test_fails_for_mismatch_with_for_func_accepting_one_arg_and_combination_of_one_arg(self):
        arg1_combinations = (1,)
        all_args_combinations = (arg1_combinations,)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(self.func, all_args_combinations, reporter=self.reporter)

    def test_passes_for_func_accepting_one_arg_and_combination_of_one_arg(self):
        arg1_combinations = (1,)
        all_args_combinations = (arg1_combinations,)
        verify_all_combinations(self.func, all_args_combinations, reporter=self.reporter)

    def test_fails_for_mismatch_with_for_func_accepting_one_arg_and_combination_of_two_args(self):
        arg1_combinations = (1, 2)
        all_args_combinations = (arg1_combinations,)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(self.func, all_args_combinations, reporter=self.reporter)

    def test_passes_for_func_accepting_one_arg_and_combination_of_two_args(self):
        arg1_combinations = (1, 2)
        all_args_combinations = (arg1_combinations,)
        verify_all_combinations(self.func, all_args_combinations, reporter=self.reporter)

    def test_fails_for_mismatch_with_for_func_accepting_two_args_and_combination_of_one_arg(self):
        arg1_combinations = (1,)
        arg2_combinations = (2,)
        arg_combinations = (arg1_combinations, arg2_combinations)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(self.func, arg_combinations, reporter=self.reporter)

    def test_passes_for_func_accepting_two_args_and_combination_of_one_arg(self):
        arg1_combinations = (1,)
        arg2_combinations = (2,)
        arg_combinations = (arg1_combinations, arg2_combinations)
        verify_all_combinations(self.func, arg_combinations, reporter=self.reporter)

    def test_fails_for_mismatch_with_for_func_accepting_two_args_and_combination_of_two_args(self):
        arg1_combinations = (1, 3)
        arg2_combinations = (2, 4)
        arg_combinations = (arg1_combinations, arg2_combinations)
        with self.assertRaises(ApprovalException):
            verify_all_combinations(self.func, arg_combinations, reporter=self.reporter)

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

    def test_records_exception_message_when_function_under_test_throws_an_exception(self):
        def function_that_raises_exceptions(*args):
            raise Exception(args)
        arg1_combinations = (1, 3)
        arg2_combinations = (2, 4)
        arg_combinations = (arg1_combinations, arg2_combinations)
        verify_all_combinations(function_that_raises_exceptions, arg_combinations, reporter=self.reporter)

    def test_uses_user_specified_formatter_when_supplied(self):
        arg1_combinations = (1, 3)
        arg2_combinations = (2, 4)
        arg_combinations = (arg1_combinations, arg2_combinations)
        verify_all_combinations(
            self.func,
            arg_combinations,
            formatter=lambda args, output: "inputs=" + str(args) + ", outputs=" + str(output) + "\n",
            reporter=self.reporter
        )
