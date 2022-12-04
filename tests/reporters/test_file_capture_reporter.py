import os

from approvaltests.reporters.file_capture_reporter import (
    is_git_registration_needed_for_github,
)


def test_is_github_actions() -> None:
    os.environ.setdefault("GITHUB_ACTIONS", "Something Not Falsely")
    assert is_git_registration_needed_for_github()
