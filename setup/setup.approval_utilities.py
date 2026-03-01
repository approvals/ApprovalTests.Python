import sys
from pathlib import Path
from typing import Any, Dict

_setup_dir = Path(__file__).resolve().parent / "setup"
if _setup_dir.is_dir():
    sys.path.insert(0, str(_setup_dir))
from setup_utils import get_version
from setuptools import find_packages, setup

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
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
