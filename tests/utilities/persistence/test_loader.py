from typing_extensions import override

from approval_utilities.utilities.persistence.loader import Loader, T


class IntegerLoader(Loader[int]):
    @override
    def load(self) -> int:
        return 42


def test_load() -> None:
    loader = IntegerLoader()
    assert 42 == loader.load()
