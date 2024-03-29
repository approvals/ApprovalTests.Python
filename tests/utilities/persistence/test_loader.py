from approval_utilities.utilities.persistence.loader import Loader, T


class IntegerLoader(Loader[int]):
    def load(self) -> int:
        return 42


def test_load():
    loader = IntegerLoader()
    assert 42 == loader.load()
