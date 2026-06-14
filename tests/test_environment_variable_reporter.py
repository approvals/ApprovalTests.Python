import pathlib
from approvaltests.reporters.environment_variable_reporter import EnvironmentVariableReporter


def test_not_set() -> None:
    assert not EnvironmentVariableReporter._report_with(None, "received.txt", "approved.txt")


def  test_empty() -> None:
    assert not EnvironmentVariableReporter._report_with("", "received.txt", "approved.txt")


def test_valid_reporter(tmp_path: pathlib.Path) -> None:
    result = EnvironmentVariableReporter._report_with(
        "approvaltests.reporters.report_quietly.ReportQuietly",
        str(tmp_path / "r.txt"),
        str(tmp_path / "a.txt"),
    )
    assert result


def test_typo() -> None:
    import pytest
    with pytest.raises(ModuleNotFoundError):
        EnvironmentVariableReporter._report_with(
            "approvaltests.reporters.nonexistent.NoSuchReporter",
            "received.txt",
            "approved.txt",
        )

