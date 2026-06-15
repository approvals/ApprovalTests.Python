import sys
from pathlib import Path

from setuptools import find_packages

_SCRIPT_DIR = Path(__file__).parent.resolve()

sys.path.insert(0, str(_SCRIPT_DIR / "setup"))
from setup_utils import setup_approvals  # pylint: disable=wrong-import-position

setup_approvals(
    name="approval_utilities",
    description="Utilities for your production code that work well with approvaltests",
    packages=find_packages(include=["approval_utilities*"]),
    install_requires=["typing_extensions>=4.12.0"],
    # long_description=(get_parent_directory() / "README.md").read_text(),
    # long_description_content_type="text/markdown",
)
