from approvaltests import ApprovalException
from approvaltests.reporter_missing_exception import ReporterMissingException


def test_ApprovalException():
    assert "ApprovalException('hello')" == repr(ApprovalException('hello'))

def test_ReporterMissingException():
    assert "ReporterMissingException('MY_REPORTER')" == repr(ReporterMissingException('MY_REPORTER'))