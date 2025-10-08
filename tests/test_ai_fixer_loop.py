import re
import sys
from pathlib import Path

from approvaltests import Options, verify_argument_parser
from approvaltests.utilities.command_line_approvals import verify_command_line

_SCRIPT_DIR = Path(__file__).parent
_REPO_ROOT = _SCRIPT_DIR.parent
sys.path.insert(0, _REPO_ROOT.joinpath("internal_documentation/scripts").as_posix())
from ai_fixer_loop import (  # pylint: disable=wrong-import-position,wrong-import-order
    get_argument_parser,
)


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


def test_argument_parser() -> None:
    """
    usage: ai_fixer_loop [-h] [--find FIND] [--fix FIX] [--tcr TCR]

    AI-Powered Loop Fixer.

    <optional header>:
      -h, --help   show this help message and exit
      --find FIND  The script to run to find problems.
      --fix FIX    The script to run to fix problems.
      --tcr TCR    The script for Test && Commit || Revert.
    """
    verify_argument_parser(get_argument_parser(), options=Options().inline())
