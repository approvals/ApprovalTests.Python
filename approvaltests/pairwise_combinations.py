from itertools import product
from typing import Any, Callable, Optional, Tuple, Union, List, Sequence, Dict

from allpairspy import AllPairs

def get_best_covering_pairs(
        input_arguments: Sequence[Sequence[Any]],
) -> Sequence[Sequence[Any]]:
    return list(AllPairs(input_arguments))
