import re
import subprocess
import sys
from pathlib import Path

import pytest

from approvaltests import Options, verify

_SCRIPT_DIR = Path(__file__).parent


@pytest.mark.skip
def test_ai_fixer_loop_output() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "ai_fixer_loop.py",
            "--find",
            "test_find",
            "--fix",
            "test_fix",
            "--tcr",
            "test_tcr",
        ],
        capture_output=True,
        text=True,
        check=True,
        encoding="utf-8",
        cwd=_SCRIPT_DIR.parent / "internal_documentation/scripts",
    )

    verify(
        result.stdout,
        options=Options().with_scrubber(
            lambda text: re.sub(r" \[[\d\.]+s\]", "", text)
        ),
    )
