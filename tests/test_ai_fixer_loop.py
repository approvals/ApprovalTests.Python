import re
from pathlib import Path

import pytest

from approvaltests import Options
from approvaltests.utilities.command_line_approvals import verify_command_line

_SCRIPT_DIR = Path(__file__).parent
_REPO_ROOT = _SCRIPT_DIR.parent


@pytest.mark.skip
def test_ai_fixer_loop() -> None:
    cwd = _REPO_ROOT / "internal_documentation" / "scripts"
    verify_command_line(
        r"C:\Users\ImageBuilderAdmin\AppData\Local\Programs\Python\Python313\python.exe ai_fixer_loop.py --find test_find --fix test_fix --tcr test_tcr",
        current_working_directory=str(cwd),
        options=Options().with_scrubber(
            lambda text: re.sub(r" \[[\d\.]+s\]", " [time]", text)
        ),
    )
