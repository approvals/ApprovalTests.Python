from setup_utils import get_requirements_from_file, do_the_setup

from setuptools import setup, find_packages #type: ignore

required = get_requirements_from_file('requirements.prod.required.txt')
required += get_requirements_from_file('requirements.prod.extras.txt')

print(f"required={required}")

package_name = "approvaltests"
package_description = "Assertion/verification library to aid testing"
green = {}

do_the_setup(package_name, package_description, green, required)
