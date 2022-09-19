import os

from approvaltests import verify, Options
from approvaltests.reporters.file_capture_reporter import is_git_registration_needed, FileCaptureReporter


def test_is_github_actions() -> None:
    os.environ.setdefault("GITHUB_ACTIONS", "Something Not Falsely")
    assert is_git_registration_needed()
    verify("From CI",options=Options().with_reporter(FileCaptureReporter()))