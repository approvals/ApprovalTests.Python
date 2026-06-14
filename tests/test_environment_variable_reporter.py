from approvaltests.reporters.environment_variable_reporter import (
    EnvironmentVariableReporter,
)


def test_returns_false_when_no_class_name():
    assert not EnvironmentVariableReporter._report_with(None, "received.txt", "approved.txt")


def test_returns_false_when_class_name_is_empty():
    assert not EnvironmentVariableReporter._report_with("", "received.txt", "approved.txt")


def test_delegates_to_named_reporter(tmp_path):
    result = EnvironmentVariableReporter._report_with(
        "approvaltests.reporters.report_quietly.ReportQuietly",
        str(tmp_path / "r.txt"),
        str(tmp_path / "a.txt"),
    )
    assert result


def test_raises_when_class_name_does_not_exist():
    import pytest
    with pytest.raises(Exception):
        EnvironmentVariableReporter._report_with(
            "approvaltests.reporters.nonexistent.NoSuchReporter",
            "received.txt",
            "approved.txt",
        )


def test_env_var_name_is_approval_tests_use_reporter():
    assert EnvironmentVariableReporter.ENVIRONMENT_VARIABLE_NAME == "APPROVAL_TESTS_USE_REPORTER"
