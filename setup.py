from distutils.core import setup

setup(
    name='approvaltests',
    version='0.1.10',
    description='Assertion/verification library to aid testing',
    author='ApprovalTests Contributors',
    author_email='jamesrcounts@outlook.com',
    url='https://github.com/approvals/ApprovalTests.Python',
    packages=['approvaltests'],
    data_files=[('', ['approvaltests/reporters.json'])]
)
