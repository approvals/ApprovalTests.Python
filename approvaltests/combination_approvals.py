from itertools import product
from typing import Any, Callable, Optional, Tuple, Union, List, Sequence

from approvaltests import (
    verify_with_namer,
    get_default_namer,
    Reporter,
    initialize_options,
    Options,
)
from approvaltests.core.namer import StackFrameNamer
from approvaltests.reporters.testing_reporter import ReporterForTesting


def verify_all_combinations(
    function_under_test: Callable,
    input_arguments: Sequence[Sequence[Any]],
    formatter: Optional[Callable] = None,
    reporter: Optional[ReporterForTesting] = None,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
) -> None:
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
    namer = get_default_namer()
    options = initialize_options(options, reporter)
    verify_all_combinations_with_namer(
        function_under_test, input_arguments, namer, formatter, None, options=options
    )


def verify_all_combinations_with_namer(
    function_under_test: Callable,
    input_arguments: Sequence[Sequence[Any]],
    namer: StackFrameNamer,
    formatter: Optional[Callable] = None,
    reporter: Optional[Reporter] = None,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Optional[Options] = None
) -> None:
    """Run func with all possible combinations of args and verify outputs against the recorded approval file.

    Args:
        function_under_test (function): function under test.
        input_arguments: list of values to test for each input argument.  For example, a function f(product, quantity)
            could be tested with the input_arguments [['water', 'cola'], [1, 4]], which would result in outputs for the
            following calls being recorded and verified: f('water', 1), f('water', 4), f('cola', 1), f('cola', 4).
        namer (approvaltests.Namer): A namer that defines the name of received and approved files.
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
    options = initialize_options(options, reporter)
    verify_with_namer("".join(approval_strings), namer=namer, options=options)


def args_and_result_formatter(args: List[Any], result: int) -> str:
    return "args: {} => {}\n".format(repr(args), repr(result))
