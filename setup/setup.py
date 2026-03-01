import sys
from pathlib import Path

_setup_dir = Path(__file__).resolve().parent / "setup"
if _setup_dir.is_dir():
    sys.path.insert(0, str(_setup_dir))
from setup_utils import do_the_setup, get_requirements_from_file  # pylint: disable=wrong-import-position

required = get_requirements_from_file("../requirements.prod.required.txt")
required += get_requirements_from_file("../requirements.prod.extras.txt")

do_the_setup(
    package_name="approvaltests",
    package_description="Assertion/verification library to aid testing",
    required=required,
    extra_requires={},
)
