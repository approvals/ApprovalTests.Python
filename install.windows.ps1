# To run this script directly, run this in an elevated admin PowerShell prompt:
#     Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/approvals/ApprovalTests.Python/main/install.windows.ps1 | Invoke-Expression

# This script is intended to setup a dev machine from scratch. Very useful for setting up a EC2 instance for mobbing.
#


iwr -useb https://raw.githubusercontent.com/approvals/ApprovalTests.Python/main/windows.ps1 | iex


choco install beyondcompare
choco install pycharm
choco install mise
choco install windsurf
choco install python

# AI coding agents
irm https://claude.ai/install.ps1 | iex


syspin "C:\Program Files\JetBrains\PyCharm 2025.1.1.1\bin\pycharm64.exe" "Pin to taskbar"

# Clone repo
& "C:\Program Files\Git\cmd\git.exe" clone https://github.com/approvals/ApprovalTests.Python.git C:\Code\ApprovalTests.Python

# We cloned as admin; make the repo usable by everyone on this (shared mobbing) box
icacls C:\Code\ApprovalTests.Python /grant "Users:(OI)(CI)F" /T

cd C:\Code\ApprovalTests.Python

# Let mise provision the toolchain (python from .python-version, uv from .mise.toml) and run the build
mise trust
mise install
mise run build_and_test


# Done
cls
echo "Done!"