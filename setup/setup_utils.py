import sys
from pathlib import Path
from typing import Any

from setuptools import find_packages, setup

_SCRIPT_DIR = Path(__file__).parent

PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13", "3.14"]


PYTHON_VERSION_CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
] + [f"Programming Language :: Python :: {version}" for version in PYTHON_VERSIONS]


def get_version() -> str:
    sys.path.append(str(_SCRIPT_DIR.parent))
    from version import version_number

    return version_number


def get_requirements_from_file(file: str) -> list[str]:
    with open(_SCRIPT_DIR / file) as f:
        required = f.read().splitlines()
    return required


def setup_approvaltests(
    package_name: str,
    package_description: str,
    required: list[str],
    extra_requires: dict[str, list[str]],
) -> None:
    required += [f"approval_utilities=={get_version()}"]

    # Ensure build directory exists for egg-info
    build_dir = _SCRIPT_DIR / "build"
    build_dir.mkdir(exist_ok=True)

    setup_approvals(
        name=package_name,
        description=package_description,
        packages=find_packages(include=["approvaltests*"]),
        package_data={"approvaltests": ["reporters/reporters.json"]},
        entry_points={
            "pytest11": [
                "approvaltests_pytest = approvaltests.integrations.pytest.pytest_plugin",
            ],
        },
        install_requires=required,
        extra_requires=extra_requires,
        long_description=(_SCRIPT_DIR.parent / "README.md").read_text(),
        long_description_content_type="text/markdown",
        additional_classifiers=[
            "Topic :: Software Development :: Testing",
            "Topic :: Utilities",
        ],
    )


def setup_approvals(
    additional_classifiers: list[str] = [],
    **kwargs: Any,
) -> None:
    setup(
        version=get_version(),
        license="Apache-2.0",
        author="ApprovalTests Contributors",
        author_email="llewellyn.falco@gmail.com",
        url="https://github.com/approvals/ApprovalTests.Python",
        python_requires=">=3.10",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Operating System :: POSIX",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS :: MacOS X",
            *PYTHON_VERSION_CLASSIFIERS,
            "Topic :: Software Development :: Libraries",
            *additional_classifiers,
        ],
        **kwargs,
    )
