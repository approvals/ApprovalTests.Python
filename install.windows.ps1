# To run this script directly, run this in an elevated admin PowerShell prompt:
#     Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/approvals/ApprovalTests.Python/master/install.windows.ps1 | Invoke-Expression

# This script is intended to setup a dev machine from scratch. Very useful for setting up a EC2 instance for mobbing.
#


iwr -useb https://raw.githubusercontent.com/JayBazuzi/machine-setup/main/windows.ps1 | iex
iwr -useb https://raw.githubusercontent.com/JayBazuzi/machine-setup/main/python-pycharm.ps1 | iex

choco install python --version=3.6.7 --allow-downgrade
choco install visualstudio2019buildtools
pip install tox

# Clone repo
& "C:\Program Files\Git\cmd\git.exe" clone https://github.com/approvals/ApprovalTests.Python.git C:\Code\ApprovalTests.Python
cd C:\Code\ApprovalTests.Python

tox -e dev
tox -e lint

# Done
cls
echo "Done!"
