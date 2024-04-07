from typing import List, Callable, Any, Tuple

from approvaltests import Options, verify_all
from approvaltests.namer.inline_comparator import InlineComparator

from typing import TypeVar, Generic

from build.lib.approvaltests.reporters import ReporterThatAutomaticallyApproves

T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
NT1 = TypeVar("NT1")
NT2 = TypeVar("NT2")


class Parse2(Generic[T1, T2]):
    def __init__(self, text: str, transformer: Callable[[str], Tuple[T1, T2]], options) -> None:
        self.text = text
        self._transformer = transformer
        self.options = options
        
    def verify_all(self, transform: Callable[[T1, T2], Any]):
        verify_all(
            "",
            Parse.parse_inputs(self.text, self._transformer),
            lambda s: f"{s[0]}, {s[1]} -> {transform(s[0], s[1])}",
            options=self.options.inline(),
        )

    def transform2(self, transform1: Callable[[T1], NT1], transform2: Callable[[T2], NT2]) -> "Parse2[NT1, NT2]":
        def transformer(s: str) -> Tuple[NT1, NT2]:
            t1, t2 = self._transformer(s)
            return (transform1(t1), transform2(t2))
        
        return Parse2(self.text, transformer, self.options)

class Parse(Generic[T]):
    def __init__(self, text: str, transformer: Callable[[str], T], options) -> None:
        self.text = text
        self._transformer = transformer
        self.options = options

    @staticmethod
    def doc_string(*, auto_approve=False) -> "Parse[str]":
        options = Options()
        if auto_approve:
            options = options.with_reporter(ReporterThatAutomaticallyApproves())
            
        return Parse(InlineComparator.get_test_method_doc_string(), lambda s: s, options=options)

    def get_inputs(self) -> List[T]:
        return Parse.parse_inputs(self.text, self._transformer)

    @staticmethod
    def parse_inputs(text, transformer):
        lines = text.split("\n")
        lines = list(filter(lambda line: line.strip(), lines))
        inputs = [line.split("->")[0].strip() for line in lines]
        return [transformer(i) for i in inputs]

    def verify_all(self, transform: Callable[[T], Any]):
        verify_all(
            "",
            self.get_inputs(),
            lambda s: f"{s} -> {transform(s)}",
            options=self.options.inline(),
        )

    def transform(self, transform: Callable[[T], T2]) -> "Parse[T2]":
        return Parse(self.text, lambda s: transform(self._transformer(s)), self.options)

    def transform2(self, transform1: Callable[[str], T1], transform2: Callable[[str], T2]) -> "Parse2[T1, T2]":
        def transformer(s: str) -> Tuple[T1, T2]:
            parts = s.split(",")
            parts = list(map(lambda p: p.strip(), parts))
            return (transform1(parts[0]), transform2(parts[1]))
        
        return Parse2(self.text, transformer, self.options)


def test_single_strings():
    """
    Sam -> SAM
    Llewellyn -> LLEWELLYN
    """
    parse = Parse.doc_string()
    verify_all(
        "",
        parse.get_inputs(),
        lambda s: f"{s} -> {s.upper()}",
        options=Options().inline(),
    )
    parse.verify_all(lambda s: s.upper())


def test_with_types_transformers_and_both():
    """
    1 -> 0b1
    9 -> 0b1001
    """
    parse = Parse.doc_string()
    verify_all(
        "",
        parse.get_inputs(),
        lambda s: f"{s} -> {bin(int(s))}",
        options=Options().inline(),
    )
    parse.transform(int).verify_all(lambda i: bin(i))
    parse.transform(lambda a: int(a)).verify_all(lambda i: bin(i))


# parse.transform(int).transform(str).transform(int).verify_all(lambda i: bin(i), options= Options().with_reporter(ReporterThatAutomaticallyApproves())


def test_with_2_types_transformers_and_both():
    """
    1, 5.0 -> 5.0
    4, 0.5 -> 2.0
    """
    parse = Parse.doc_string(auto_approve=True)
    parse.transform2(int, float).verify_all(lambda i,f: i * f)
    parse.transform2(str, str).transform2(int, float).verify_all(lambda i,f: i * f)

