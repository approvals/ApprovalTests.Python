from approval_utilities.utilities.persistence.saver import Saver


class IncrementSaver(Saver[int]):
    def save(self, t: int) -> int:
        return t + 1


def test_save():
    saver = IncrementSaver()
    assert 42 == saver.save(41)
