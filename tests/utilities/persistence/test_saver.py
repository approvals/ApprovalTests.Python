from typing_extensions import override
from approval_utilities.utilities.persistence.saver import Saver


class IncrementSaver(Saver[int]):
    @override
    def save(self, t: int) -> int:
        return t + 1


def test_save() -> None:
    saver = IncrementSaver()
    assert 42 == saver.save(41)
