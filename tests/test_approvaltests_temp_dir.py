import os

from approvaltests.internals.logs.log_commons import (
    APPROVAL_TESTS_TEMP_DIRECTORY,
    LogCommons,
)


def test_temp_directory_is_setup_automatically() -> None:
    # setup happens automatically
    gitignore_path = APPROVAL_TESTS_TEMP_DIRECTORY / ".gitignore"
    contents = gitignore_path.read_text()
    assert contents == "*"


def test_script_download_disabled_when_env_var_set() -> None:
    os.environ["APPROVALTESTS_DISABLE_SCRIPT_DOWNLOADS"] = "1"

    result = LogCommons.download_script_from_common_repo_if_needed("test_script.py")

    assert result is False
