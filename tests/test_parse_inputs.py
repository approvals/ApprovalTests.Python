from typing import List, Callable, Any

from approvaltests import Options, verify_all
from approvaltests.namer.inline_comparator import InlineComparator

from typing import TypeVar, Generic

T = TypeVar("T")
T2 = TypeVar("T2")
class Parse(Generic[T]):
    def __init__(self, text: str, transformer: Callable[[str], T]) -> None:
        self.text = text
        self.transformer = transformer

    @staticmethod
    def doc_string() -> 'Parse[str]':
        return Parse(InlineComparator.get_test_method_doc_string(), lambda s: s)

    def get_inputs(self) -> List[T]:
        lines = self.text.split("\n")
        lines = list(filter(lambda line: line.strip(), lines))
        inputs = [line.split("->")[0].strip() for line in lines]
        return [self.transformer(i) for i in inputs]
    def verify_all(self, transform: Callable[[T], Any]):
        verify_all("", self.get_inputs(), lambda s: f"{s} -> {transform(s)}", options=Options().inline())

    def transform(self, transform: Callable[[T], T2]) -> 'Parse[T2]':
        return Parse(self.text, lambda s: transform(self.transformer(s)))


def test_single_strings():
    """
    Sam -> SAM
    Llewellyn -> LLEWELLYN
    """
    parse = Parse.doc_string()
    verify_all("", parse.get_inputs(), lambda s: f"{s} -> {s.upper()}", options=Options().inline())
    parse.verify_all(lambda s: s.upper())


def test_with_types_transformers_and_both():
    """
    1 -> 0b1
    9 -> 0b1001
    """
    parse = Parse.doc_string()
    verify_all("", parse.get_inputs(), lambda s: f"{s} -> {bin(int(s))}", options=Options().inline())
    parse.transform(int).verify_all(lambda i: bin(i))
    parse.transform(int).verify_all(lambda i: bin(i))
