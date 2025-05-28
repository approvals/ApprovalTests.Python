from setuptools import find_packages, setup

from setup_utils import do_the_setup, get_requirements_from_file

required = get_requirements_from_file("requirements.prod.required.txt")
required += get_requirements_from_file("requirements.prod.extras.txt")

do_the_setup(
    package_name="approvaltests",
    package_description="Assertion/verification library to aid testing",
    required=required,
    extra_requires={},
)
