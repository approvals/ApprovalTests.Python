

from setuptools import setup, find_packages #type: ignore

from setup_utils import get_requirements_from_file, do_the_setup

required = get_requirements_from_file('requirements.prod.required.txt')

blue = "approvaltests-minimal"
red = "Assertion/verification library to aid testing with the minimal required dependencies + the ability to opt in for the others "
green = {
    "ClipboardReporter": ["pyperclip"],
    "verify_html": ["beautifulsoup4"],
    "PairwiseCombinations": ["allpairspy"]
}

do_the_setup(blue, red, green, required)
