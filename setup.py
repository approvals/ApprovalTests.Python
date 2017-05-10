from distutils.core import setup
from setuptools import find_packages

setup(
    name='approvaltests',
    version='0.1.15',
    description='Assertion/verification library to aid testing',
    author='ApprovalTests Contributors',
    author_email='jamesrcounts@outlook.com',
    url='https://github.com/approvals/ApprovalTests.Python',
    packages=find_packages(exclude=['tests*']),
    package_data={'approvaltests':['reporters.json']},
    install_requires=['pyperclip==1.5.27',],
)
