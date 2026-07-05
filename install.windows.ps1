# To run this script directly, run this in an elevated admin PowerShell prompt:
#     Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/approvals/ApprovalTests.Python/master/install.windows.ps1 | Invoke-Expression

# This script is intended to setup a dev machine from scratch. Very useful for setting up a EC2 instance for mobbing.
#


iwr -useb https://raw.githubusercontent.com/approvals/approvaltests.python/main/windows.ps1 | iex


winget install -e --id ScooterSoftware.BeyondCompare --accept-package-agreements --accept-source-agreements
winget install -e --id JetBrains.PyCharm.Professional --accept-package-agreements --accept-source-agreements
winget install -e --id jdx.mise --accept-package-agreements --accept-source-agreements
winget install -e --id OpenJS.NodeJS --accept-package-agreements --accept-source-agreements
# Python and uv are managed by mise (see .python-version and .mise.toml), so we don't install them separately.

# AI coding agents
npm install -g @anthropic-ai/claude-code   # `claude`

# Instructions for AI agents:
# install devin


syspin "C:\Program Files\JetBrains\PyCharm 2025.1.1.1\bin\pycharm64.exe" "Pin to taskbar"

# Clone repo
& "C:\Program Files\Git\cmd\git.exe" clone https://github.com/approvals/ApprovalTests.Python.git C:\Code\ApprovalTests.Python
cd C:\Code\ApprovalTests.Python

# Let mise provision the toolchain (python from .python-version, uv from .mise.toml) and run the build
mise trust
mise install
mise run build_and_test


# Done
cls
echo "Done!"