from itertools import product
from typing import Any, Callable, Optional, Tuple, Union, List, Sequence, Dict

from approvaltests import (
    verify_with_namer,
    get_default_namer,
    Reporter,
    initialize_options,
    Options,
    verify,
)
from approvaltests.core.namer import StackFrameNamer
from approvaltests.reporters.testing_reporter import ReporterForTesting


# [[5?],[2?],[3?],[]]
# given inputs = {int[], string[], bool[]}
# output = {{int, string, bool}[]}
def get_best_covering_pairs(
        input_arguments: Sequence[Sequence[Any]],
) -> Sequence[Sequence[Any]]:
    all = list(product(*input_arguments))
    minimal = []
    pairs = {}
    # go through each line of all and if it adds a new pair add it to the minimal set
    for params in all:
        pair_length = len(pairs)
        add_all_pairs_from(pairs, params)
        if len(pairs) > pair_length:
            minimal.append(params)
    return minimal


def add_all_pairs_from(pairs, params):
    for i1 in range(len(params) - 1):
        for i2 in range(i1 + 1, len(params)):
            in1 = params[i1]
            in2 = params[i2]
            add_pair(in1, in2, pairs)


def get_key(in1: Any, in2: Any) -> str:
    return f"({in1},{in2})"


def add_pair(in1: Any, in2: Any, all_pairs_with_index: Dict[str, int]) -> None:
    key = get_key(in1, in2)
    all_pairs_with_index.setdefault(key, len(all_pairs_with_index))
