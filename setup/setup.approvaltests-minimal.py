import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).parent.resolve()

sys.path.insert(0, str(_SCRIPT_DIR / "setup"))
from setup_utils import do_the_setup, get_requirements_from_file, get_version

required = get_requirements_from_file("../requirements.prod.required.txt")
required += [f"approval_utilities=={get_version()}"]

extra_requires = {
    "ClipboardReporter": ["pyperclip"],
    "verify_html": ["beautifulsoup4"],
    "PairwiseCombinations": ["allpairspy"],
}

do_the_setup(
    package_name="approvaltests-minimal",
    package_description="Assertion/verification library to aid testing with the minimal required dependencies + the ability to opt in for the others ",
    required=required,
    extra_requires=extra_requires,
)
