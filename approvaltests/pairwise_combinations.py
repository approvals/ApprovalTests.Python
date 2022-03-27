from typing import Any, Sequence

from allpairspy import AllPairs


def get_best_covering_pairs(
        input_arguments: Sequence[Sequence[Any]],
) -> Sequence[Sequence[Any]]:
    return list(AllPairs(input_arguments))
