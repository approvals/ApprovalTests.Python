from approvaltests import ApprovalException, Options, verify
from approvaltests.reporter_missing_exception import ReporterMissingException


def test_ApprovalException_repr() -> None:
    """
    ApprovalException('hello')
    """
    verify(repr(ApprovalException("hello")), options=Options().inline())


def test_ReporterMissingException_repr() -> None:
    """
    ReporterMissingException('MY_REPORTER')
    """
    verify(repr(ReporterMissingException("MY_REPORTER")), options=Options().inline())


def test_ReporterMissingException_str() -> None:
    """
    Could not find 'MY_REPORTER' in the environment, perhaps you need to configure your reporter.
    """
    verify(str(ReporterMissingException("MY_REPORTER")), options=Options().inline())
