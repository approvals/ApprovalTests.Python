from approvaltests.internals.logs.log_commons import APPROVAL_TESTS_TEMP_DIRECTORY


def test_temp_directory_is_setup_automatically() -> None:
    # setup happens automatically
    gitignore_path = APPROVAL_TESTS_TEMP_DIRECTORY / ".gitignore"
    contents = gitignore_path.read_text()
    assert contents == "*"
