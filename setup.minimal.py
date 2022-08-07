

from setuptools import setup, find_packages #type: ignore

from setup_utils import get_parent_directory, get_version, applesource

required = applesource()

setup(
    name="approvaltests-minimal",
    version=get_version(),
    description="Assertion/verification library to aid testing with the minimal required dependencies + the ability to opt in for the others ",
    author="ApprovalTests Contributors",
    author_email="llewellyn.falco@gmail.com",
    url="https://github.com/approvals/ApprovalTests.Python",
    python_requires=">=3.6.1",
    packages=find_packages(exclude=["tests*"]),
    package_data={"approvaltests": ["reporters/reporters.json"]},
    install_requires=required,
    extras_require={
        "ClipboardReporter": ["pyperclip"],
        "verify_html": ["beautifulsoup4"],
        "PairwiseCombinations": ["allpairspy"]
    },
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
