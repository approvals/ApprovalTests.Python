from pathlib import Path

from approvaltests import verify

from mrjob.job import MRJob


class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(self, key, values):
        yield key, sum(values)


def verify_map_reduce(map_reduction, test_data):
    storyboard = f"{ Path(test_data).read_text()}\n"
    storyboard += "\nMap reduces to:\n\n"

    with open(test_data, "rb") as test_data_file:
        map_reduction.sandbox(stdin=test_data_file)

        with map_reduction.make_runner() as runner:
            runner.run()
            for key, value in map_reduction.parse_output(runner.cat_output()):
                storyboard += f"{key}:{value}\n"

    verify(storyboard)


def test_word_count():
    test_data = "test.data"
    map_reduction = MRWordFrequencyCount(["--no-conf"])
    verify_map_reduce(map_reduction, test_data)
