from typing import List, Callable

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

    def verify_all(self, transform: Callable[[str], str]):
        verify_all("", self.get_inputs(), lambda s: f"{s} -> {transform(s)}", options=Options().inline())


def test_single_strings():
    """
    Sam -> SAM
    Llewellyn -> LLEWELLYN
    """
    parse = Parse.doc_string()
    verify_all("", parse.get_inputs(), lambda s: f"{s} -> {s.upper()}", options=Options().inline())
    parse.verify_all(lambda s: s.upper())
