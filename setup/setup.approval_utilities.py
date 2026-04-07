import sys
from pathlib import Path
from typing import Any, Dict

from setuptools import find_packages, setup

_SCRIPT_DIR = Path(__file__).parent.resolve()

sys.path.insert(0, str(_SCRIPT_DIR / "setup"))
from setup_utils import PYTHON_VERSION_CLASSIFIERS, get_version  # pylint: disable=wrong-import-position

requires: Dict[str, Any] = {}
setup(
    name="approval_utilities",
    version=get_version(),
    description="Utilities for your production code that work well with approvaltests",
    author="ApprovalTests Contributors",
    author_email="llewellyn.falco@gmail.com",
    url="https://github.com/approvals/ApprovalTests.Python",
    python_requires=">=3.8",
    packages=find_packages(include=["approval_utilities*"]),
    package_data={},
    install_requires=[],
    # long_description=(get_parent_directory() / "README.md").read_text(),
    # long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        *PYTHON_VERSION_CLASSIFIERS,
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
