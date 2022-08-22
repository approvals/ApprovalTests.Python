from mrjob.job import MRJob

from approvaltests.mrjob.mrjob_approvals import verify_map_reduce


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
