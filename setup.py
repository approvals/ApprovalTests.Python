import os
import re
from setup_utils import get_parent_directory
from pathlib import Path

from setuptools import setup, find_packages #type: ignore


_version_file_contents = (get_parent_directory() / "approvaltests" / "version.py").read_text()
matched = re.search(r'"(.*)"', _version_file_contents)
VERSION = matched.group(1) if matched is not None else "UNKNOWN VERSION"

with open(get_parent_directory() / 'requirements.prod.required.txt') as f:
    required = f.read().splitlines()
with open(get_parent_directory() / 'requirements.prod.extras.txt') as f:
    required += f.read().splitlines()

print(f"required={required}")

setup(
    name="approvaltests",
    version=VERSION,
    description="Assertion/verification library to aid testing",
    author="ApprovalTests Contributors",
    author_email="llewellyn.falco@gmail.com",
    url="https://github.com/approvals/ApprovalTests.Python",
    python_requires=">=3.6.1",
    packages=find_packages(exclude=["tests*"]),
    package_data={"approvaltests": ["reporters/reporters.json"]},
    install_requires=required,
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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
