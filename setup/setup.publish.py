from setup_utils import get_requirements_from_file, get_version

from setup import do_the_setup

required = get_requirements_from_file("../requirements.prod.required.txt")
required += get_requirements_from_file("../requirements.prod.extras.txt")
required += [f"approval_utilities=={get_version()[1:]}"]
do_the_setup(
    package_name="approvaltests",
    package_description="Assertion/verification library to aid testing",
    required=required,
    extra_requires={},
)
