# To run this script directly, run this in an elevated admin PowerShell prompt:
#     Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/approvals/ApprovalTests.Python/main/install.windows.ps1 | Invoke-Expression

# This script is intended to setup a dev machine from scratch. Very useful for setting up a EC2 instance for mobbing.

if (([Security.Principal.WindowsPrincipal]::new([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    throw "This script must not be run as Administrator."
}


iwr -useb https://raw.githubusercontent.com/approvals/ApprovalTests.Python/main/windows.ps1 | iex

Start-Process -Verb RunAs choco 'install pycharm'
Start-Process -Verb RunAs choco 'install mise'
Start-Process -Verb RunAs choco 'install windsurf'
Start-Process -Verb RunAs choco 'install python'

# AI coding agents
irm https://claude.ai/install.ps1 | iex


syspin "C:\Program Files\JetBrains\PyCharm 2025.1.1.1\bin\pycharm64.exe" "Pin to taskbar"

# Clone repo
& "C:\Program Files\Git\cmd\git.exe" clone https://github.com/approvals/ApprovalTests.Python.git C:\Code\ApprovalTests.Python

cd C:\Code\ApprovalTests.Python

mise trust
mise install
./build_and_test

Write-Host -ForegroundColor Green "******* machine setup script done! *******"
