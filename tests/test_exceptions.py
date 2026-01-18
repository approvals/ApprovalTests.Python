from approvaltests import ApprovalException
from approvaltests.reporter_missing_exception import ReporterMissingException


def test_ApprovalException_repr() -> None:
    assert "ApprovalException('hello')" == repr(ApprovalException("hello"))


def test_ReporterMissingException_repr() -> None:
    assert "ReporterMissingException('MY_REPORTER')" == repr(
        ReporterMissingException("MY_REPORTER")
    )

def test_ReporterMissingException_str() -> None:
    assert (
        "Could not find 'MY_REPORTER' in the environment, perhaps you need to configure your reporter."
        == str(ReporterMissingException("MY_REPORTER"))
    )
