# To run this script directly, run this in an elevated admin PowerShell prompt:
#     Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/approvals/ApprovalTests.Python/master/install.windows.ps1 | Invoke-Expression

# This script is intended to setup a dev machine from scratch. Very useful for setting up a EC2 instance for mobbing.
#


iwr -useb https://raw.githubusercontent.com/JayBazuzi/machine-setup/main/windows.ps1 | iex
# iwr -useb https://raw.githubusercontent.com/JayBazuzi/machine-setup/main/python-pycharm.ps1 | iex

iwr -useb cin.st | iex
choco feature enable --name=allowGlobalConfirmation
choco install beyondcompare
choco install python --version=3.8
choco install pip
choco install pycharm
choco install ditto
choco install mise

# Keyboard rotation for Dvorak
Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/LearnWithLlew/MobTime.keyboardswitching/main/install.windows.ps1 | Invoke-Expression

syspin "C:\Program Files (x86)\JetBrains\PyCharm 2020.3.2\bin\pycharm64.exe" "Pin to taskbar"

# Clone repo
& "C:\Program Files\Git\cmd\git.exe" clone https://github.com/approvals/ApprovalTests.Python.git C:\Code\ApprovalTests.Python
cd C:\Code\ApprovalTests.Python


# Done
cls
echo "Done!"
