import approvaltests
from pathlib import Path
from approvaltests.internals.logs.log_commons import APPROVAL_TESTS_TEMP_DIRECTORY

def test__gitignore():
    gitignore_path = Path(APPROVAL_TESTS_TEMP_DIRECTORY)/".gitignore"

    contents = gitignore_path.read_text()
    assert contents=="*"
