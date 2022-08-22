from mrjob.job import MRJob

from approvaltests.mrjob.mrjob_approvals import (
    verify_map_reduce,
    verify_map_reduction_for_combinations_of,
)


class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(self, key, values):
        yield key, sum(values)


def test_word_count():
    test_data = "one fish two fish red fish blue fish"
    map_reduction = MRWordFrequencyCount(["--no-conf"])
    verify_map_reduce(map_reduction, test_data)


def test_word_count_combinations():
    animals = ["fish"]
    # animals = ["fish", "dog", "cat"]
    colors = ["magenta", "chartreuse", "aqua", "red", "blue"]
    map_reduction = MRWordFrequencyCount(["--no-conf"])

    def input_creator(animal, color1, color2):
        return f"one {animal} two {animal} {color1} {animal} {color2} {animal}"

    verify_map_reduction_for_combinations_of(
        map_reduction, input_creator, [animals, colors, colors]
    )
