import os
from distutils.core import setup

from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
print("Here:", here)
about = {}
with open(os.path.join(here, 'approvaltests', 'version.py'), 'r') as f:
    exec(f.read(), about)


setup(
    name='approvaltests',
    version= about['version_number'],
    description='Assertion/verification library to aid testing',
    author='ApprovalTests Contributors',
    author_email='jamesrcounts@outlook.com',
    url='https://github.com/approvals/ApprovalTests.Python',
    packages=find_packages(exclude=['tests*']),
    package_data={'approvaltests':['reporters/reporters.json']},
    install_requires=['pyperclip==1.5.27',],
)
