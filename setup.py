from distutils.core import setup

setup(
    name='approvaltests',
    version='0.1.8',
    description='Assertion/verification library to aid testing',
    author='ApprovalTests Contributors',
    author_email='jamesrcounts@outlook.com',
    url='https://github.com/approvals/ApprovalTests.Python',
    packages=['approvaltests'],
    include_package_data = True,
    data_files=[('', ['reporters.json'])]
)
