from typing import List

from approvaltests import Options, verify_all
from approvaltests.namer.inline_comparator import InlineComparator


class Parse:
    def __init__(self, text: str) -> None:
        self.text = text

    @staticmethod
    def doc_string() -> 'Parse':
        return Parse(InlineComparator.get_test_method_doc_string())

    def get_inputs(self) -> List[str]:
        lines = self.text.split("\n")
        lines = list(filter(lambda line: line.strip(), lines))
        return [line.split("->")[0].strip() for line in lines]


def test_single_strings():
    """
    Sam
    Llewellyn
    """
    inputs = Parse.doc_string().get_inputs()
    verify_all("", inputs, lambda s: s, options=Options().inline())
