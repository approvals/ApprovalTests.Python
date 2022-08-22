from mrjob.job import MRJob

from approvaltests.mrjob.mrjob_approvals import (
    verify_map_reduce,
    verify_templated_map_reduction,
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


def test_word_count():
    test_data = "one fish two fish red fish blue fish"
    map_reduction = MRWordFrequencyCount()
    verify_map_reduce(map_reduction, test_data)


def test_word_count():
    test_data = "one fish two fish red fish blue fish"
    map_reduction = MRWordFrequencyCount()
    verify_map_reduce(map_reduction, test_data)


def test_word_count_combinations():
    animals = ["fish", "dog", "cat"]
    colors = ["aqua", "red", "blue"]
    map_reduction = MRWordFrequencyCount()

    def input_creator(animal, color1, color2):
        return f"one {animal} two {animal} {color1} {animal} {color2} {animal}"

    verify_templated_map_reduction(
        map_reduction, input_creator, [animals, colors, colors]
    )
