import re
from pathlib import Path
from typing import Dict, List

from setuptools import find_packages, setup


def get_parent_directory() -> Path:
    return Path(__file__).parent


def get_version() -> str:
    _version_file_contents = (get_parent_directory() / "version.py").read_text()
    matched = re.search(r'"(.*)"', _version_file_contents)
    return matched.group(1) if matched is not None else "UNKNOWN VERSION"


def get_requirements_from_file(file: str) -> List[str]:
    with open(get_parent_directory() / file) as f:
        required = f.read().splitlines()
    return required


def do_the_setup(
    package_name: str,
    package_description: str,
    required: List[str],
    extra_requires: Dict[str, List[str]],
) -> None:
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
        long_description=(get_parent_directory() / "README.md").read_text(),
        long_description_content_type="text/markdown",
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
            "Topic :: Software Development :: Testing",
            "Topic :: Utilities",
        ],
    )
