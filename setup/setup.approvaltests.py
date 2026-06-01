import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).parent.resolve()

sys.path.insert(0, str(_SCRIPT_DIR / "setup"))
from setup_utils import get_requirements_from_file, setup_approvaltests

required = get_requirements_from_file("../requirements.txt")
required += get_requirements_from_file("../requirements.extras.txt")

setup_approvaltests(
    package_name="approvaltests",
    package_description="Assertion/verification library to aid testing",
    required=required,
    extra_requires={},
)
