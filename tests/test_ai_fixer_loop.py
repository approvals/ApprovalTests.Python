import re
import sys
from pathlib import Path

from approvaltests import Options
from approvaltests.utilities.command_line_approvals import verify_command_line

_SCRIPT_DIR = Path(__file__).parent
_REPO_ROOT = _SCRIPT_DIR.parent


def test_ai_fixer_loop() -> None:
    python = sys.executable
    cwd = _REPO_ROOT / "internal_documentation" / "scripts"
    verify_command_line(
        python
        + f" ai_fixer_loop.py --find test_find --fix test_fix.sh --tcr {_REPO_ROOT / 'internal_documentation/scripts/test_tcr'}",
        current_working_directory=str(cwd),
        options=Options().with_scrubber(
            lambda text: re.sub(r" \[[\d\.]+s\]", " [time]", text)
        ),
    )
