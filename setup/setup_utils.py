import re
import sys
from pathlib import Path
from typing import Dict, List

from setuptools import find_packages, setup

_SCRIPT_DIR = Path(__file__).parent
_VERSIONS_FILE = (
    _SCRIPT_DIR.parent
    / "tests/approved_files/test_workflow_matrix.test_workflow_matrix_python_versions.approved.txt"
)


def _get_workflow_matrix_python_version_classifiers() -> List[str]:
    versions = re.findall(r"3\.\d+", _VERSIONS_FILE.read_text())
    return ([f"Programming Language :: Python :: {v}" for v in versions],)


PYTHON_VERSION_CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    *_get_workflow_matrix_python_version_classifiers(),
]


def get_version() -> str:
    sys.path.append(str(_SCRIPT_DIR.parent))
    from version import version_number

    return version_number


def get_requirements_from_file(file: str) -> List[str]:
    with open(_SCRIPT_DIR / file) as f:
        required = f.read().splitlines()
    return required


def do_the_setup(
    package_name: str,
    package_description: str,
    required: List[str],
    extra_requires: Dict[str, List[str]],
) -> None:
    # Ensure build directory exists for egg-info
    build_dir = _SCRIPT_DIR / "build"
    build_dir.mkdir(exist_ok=True)

    setup(
        name=package_name,
        version=get_version(),
        description=package_description,
        author="ApprovalTests Contributors",
        author_email="llewellyn.falco@gmail.com",
        url="https://github.com/approvals/ApprovalTests.Python",
        python_requires=">=3.8",
        packages=find_packages(include=["approvaltests*"]),
        package_data={"approvaltests": ["reporters/reporters.json"]},
        entry_points={
            "pytest11": [
                "approvaltests_pytest = approvaltests.integrations.pytest.pytest_plugin",
            ],
        },
        install_requires=required,
        extras_require=extra_requires,
        long_description=(_SCRIPT_DIR.parent / "README.md").read_text(),
        long_description_content_type="text/markdown",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: POSIX",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS :: MacOS X",
            *PYTHON_VERSION_CLASSIFIERS,
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Testing",
            "Topic :: Utilities",
        ],
    )
