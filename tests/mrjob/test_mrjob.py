import sys
from typing import Any, Dict, Generator, List, Sequence, Tuple

import pytest

from approvaltests.integrations.mrjob.mrjob_approvals import (
    verify_map_reduce,
    verify_templated_map_reduce,
    verify_templated_map_reduce_with_customized_job,
    verify_templated_map_reduce_with_customized_job_with_dictionary_args,
)

if sys.version_info < (3, 13):
    from mrjob.job import MRJob
else:
    pytest.skip("mrjob tests are skipped for Python 3.13+", allow_module_level=True)
    from typing import Any

    MRJob = Any


class MRWordFrequencyCount(MRJob):
    def __init__(self, args: List[str] = ["--no-conf"]) -> None:
        super().__init__(args)

    def mapper(self, _: str, line: str) -> Generator[Tuple[str, int], None, None]:
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(
        self, key: str, values: Sequence[int]
    ) -> Generator[Tuple[str, int], None, None]:
        yield key, sum(values)


# begin-snippet: verify_map_reduce
def test_word_count() -> None:
    test_data = "one fish two fish red fish blue fish"
    map_reduction = MRWordFrequencyCount([])
    verify_map_reduce(map_reduction, test_data)


# end-snippet


# begin-snippet: verify_templated_map_reduce
def test_word_count_combinations() -> None:
    animals = ["fish", "dog", "cat"]
    colors = ["aqua", "red", "blue"]
    map_reduction = MRWordFrequencyCount()

    def input_creator(animal: str, color1: str, color2: str) -> str:
        return f"one {animal} two {animal} {color1} {animal} {color2} {animal}"

    verify_templated_map_reduce(map_reduction, input_creator, [animals, colors, colors])


# end-snippet


class BlueReducer(MRJob):
    def __init__(self, args: List[str] = ["--no-conf"]) -> None:
        super().__init__(args)

    def mapper(self, _: str, line: str) -> Generator[Tuple[str, int], None, None]:
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1
        yield "blue", 1

    def reducer(
        self, key: str, values: Sequence[int]
    ) -> Generator[Tuple[str, int], None, None]:
        yield key, sum(values)


class AquaReducer(MRJob):
    def __init__(self, args: List[str] = ["--no-conf"]) -> None:
        super().__init__(args)

    def mapper(self, _: str, line: str) -> Generator[Tuple[str, int], None, None]:
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1
        yield "aqua", 1

    def reducer(
        self, key: str, values: Sequence[int]
    ) -> Generator[Tuple[str, int], None, None]:
        yield key, sum(values)


def test_verify_templated_map_reduce_with_customized_job() -> None:
    colors = ["aqua", "blue"]
    animals = ["cat", "dog"]

    def mapreduce_creator(color: str, _: Any) -> MRJob:
        if color == "blue":
            return BlueReducer()
        return AquaReducer()

    def input_creator(_: Any, animal: str) -> str:
        return f"one {animal} two {animal} red {animal} blue {animal}"

    verify_templated_map_reduce_with_customized_job(
        mapreduce_creator, input_creator, [colors, animals]
    )


def test_verify_templated_map_reduce_with_customized_job_with_dictionary_args() -> None:
    colors = ["aqua", "blue"]
    animals = ["cat", "dog"]

    def mapreduce_creator(params: Dict[str, str]) -> MRJob:
        if params["color"] == "blue":
            return BlueReducer()
        return AquaReducer()

    def input_creator(params: Dict[str, str]) -> str:
        animal = params["animal"]
        return f"one {animal} two {animal} red {animal} blue {animal}"

    verify_templated_map_reduce_with_customized_job_with_dictionary_args(
        mapreduce_creator, input_creator, {"color": colors, "animal": animals}
    )
