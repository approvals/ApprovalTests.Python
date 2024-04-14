from typing import Generic, Callable, Tuple, Any

from approvaltests import verify_all, verify
from approvaltests.inline.types import T1, T2, T3, NT1, NT2


class Parse3(Generic[T1, T2, T3]):
    def __init__(
        self, text: str, transformer: Callable[[str], Tuple[T1, T2, int]], options
    ) -> None:
        self.text = text
        self._transformer = transformer
        self.options = options

    def verify_all(self, transform: Callable[[T1, T2,T3], Any]):
        from approvaltests.inline.parse import Parse
        
        verify_all(
            "",
            Parse.parse_inputs(self.text, self._transformer),
            lambda s: f"{s[0]}, {s[1]}, {s[2]} -> {transform(s[0], s[1],s[2])}",
            options=self.options.inline(),
        )

    def transform2(
        self, transform1: Callable[[T1], NT1], transform2: Callable[[T2], NT2]
    ) -> "Parse2[NT1, NT2]":
        def transformer(s: str) -> Tuple[NT1, NT2]:
            t1, t2 = self._transformer(s)
            return (transform1(t1), transform2(t2))

        return Parse2(self.text, transformer, self.options)
