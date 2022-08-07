

from setuptools import setup, find_packages #type: ignore

from setup_utils import get_requirements_from_file, do_the_setup

required = get_requirements_from_file('requirements.prod.required.txt')

package_name = "approvaltests-minimal"
package_description = "Assertion/verification library to aid testing with the minimal required dependencies + the ability to opt in for the others "
green = {
    "ClipboardReporter": ["pyperclip"],
    "verify_html": ["beautifulsoup4"],
    "PairwiseCombinations": ["allpairspy"]
}

do_the_setup(package_name, package_description, green, required)