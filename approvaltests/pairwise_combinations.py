from itertools import product
from typing import Any, Callable, Optional, Tuple, Union, List, Sequence

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



def get_best_covering_pairs(
    input_arguments: Sequence[Sequence[Any]],
) -> Sequence[Sequence[Any]]:

    p = product(*input_arguments)
    return list(p)#[20:]
