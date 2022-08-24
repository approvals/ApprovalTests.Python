from itertools import product

from mrjob.job import MRJob

from approvaltests import verify
from approvaltests.mrjob.mrjob_approvals import (
    verify_map_reduce,
    verify_templated_map_reduce,
    print_map_reduce_job,
)


class MRWordFrequencyCount(MRJob):
    def __init__(self, args=["--no-conf"]):
        super().__init__(args)

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(self, key, values):
        yield key, sum(values)


# begin-snippet: verify_map_reduce
def test_word_count():
    test_data = "one fish two fish red fish blue fish"
    map_reduction = MRWordFrequencyCount([])
    verify_map_reduce(map_reduction, test_data)


# end-snippet

# begin-snippet: verify_templated_map_reduce
def test_word_count_combinations():
    animals = ["fish", "dog", "cat"]
    colors = ["aqua", "red", "blue"]
    map_reduction = MRWordFrequencyCount()

    def input_creator(animal, color1, color2):
        return f"one {animal} two {animal} {color1} {animal} {color2} {animal}"

    verify_templated_map_reduce(map_reduction, input_creator, [animals, colors, colors])


# end-snippet


def verify_created_map_reduce(map_reduce_creator, input_creator, params):
    inputs = product(*params)
    storyboard = ""
    for input in inputs:
        storyboard += f"===================\n\n{input} =>\n"
        data = input_creator(*input)
        map_reduction = map_reduce_creator(*input)

        storyboard += f"{print_map_reduce_job(map_reduction, data)}\n"
    verify(storyboard)


class BlueReducer(MRJob):
    def __init__(self, args=["--no-conf"]):
        super().__init__(args)

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1
        yield "blue", 1

    def reducer(self, key, values):
        yield key, sum(values)


class AquaReducer(MRJob):
    def __init__(self, args=["--no-conf"]):
        super().__init__(args)

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1
        yield "aqua", 1

    def reducer(self, key, values):
        yield key, sum(values)


def test_command_line_arguements():
    colors = ["aqua", "blue"]
    animals = ["cat","dog"]
    def mapreduce_creator(color: str, _ ) -> MRJob:
        if color == "blue":
            return BlueReducer()
        return AquaReducer()

    def input_creator(_,animal ):
        return f"one {animal} two {animal} red {animal} blue {animal}"

    verify_created_map_reduce(mapreduce_creator, input_creator, [colors, animals])
    # for each mapreducor created by the
