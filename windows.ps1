# This script
# iwr -useb https://raw.githubusercontent.com/JayBazuzi/machine-setup/main/windows.ps1 | iex

Start-Process -Verb RunAs powershell 'Invoke-WebRequest -UseBasicParsing -Uri "https://cin.st" | Invoke-Expression'
Start-Process -Verb RunAs powershell 'Import-Module "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"; refreshenv'

Start-Process -Verb RunAs choco 'feature enable  --name=allowGlobalConfirmation'
Start-Process -Verb RunAs choco 'feature disable --name=showDownloadProgress'

Start-Process -Verb RunAs choco 'install win-no-annoy'

Start-Process -Verb RunAs choco 'install googlechrome --ignore-checksums'
Start-Process -Verb RunAs choco 'install setdefaultbrowser'
SetDefaultBrowser.exe chrome

Start-Process -Verb RunAs choco 'install powershell-core'

Start-Process -Verb RunAs choco 'install git poshgit github-desktop'
Set-Alias github $env:LOCALAPPDATA\GitHubDesktop\bin\github.bat

Start-Process -Verb RunAs choco 'install beyondcompare'

# delete annoying Windows notification sounds
Remove-Item -ErrorAction SilentlyContinue -Recurse HKCU:\AppEvents\Schemes
Set-Service Audiosrv -StartupType Automatic

# Show seconds in the clock so screen sharing latency is obvious to all
Set-ItemProperty HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced ShowSecondsInSystemClock 1
# Open new explorer windows to This PC instead of Quick Access
Set-ItemProperty HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced LaunchTo 1

Start-Process -Verb RunAs choco 'install vscode'
@(
    'wmaurer.change-case'
    'streetsidesoftware.code-spell-checker'
    'ryu1kn.partial-diff'
    'ms-vscode.powershell'
    'mohsen1.prettify-json'
    'vscode-icons-team.vscode-icons'
) | % { & "C:\Program Files\Microsoft VS Code\bin\code.cmd" --install-extension $_ }

@'
{
    "diffEditor.ignoreTrimWhitespace": true,
    "diffEditor.renderSideBySide": false,

    "editor.minimap.enabled": true,
    "editor.renderControlCharacters": true,
    "editor.renderWhitespace": "all",
    "editor.bracketPairColorization.enabled": true,

    "git.autofetch": true,
    "git.autofetchPeriod": 1,
    "git.enableSmartCommit": true,
    "git.fetchOnPull": true,

    "workbench.iconTheme": "vscode-icons",
    "workbench.startupEditor": "newUntitledFile",

    "files.autoSaveDelay": 100,
    "files.autoSave": "afterDelay"
}
'@ | Out-File -Encoding ASCII $env:APPDATA\Code\User\settings.json

$ProgressPreference = 'SilentlyContinue'
$mobtimeMsiUrl = (Invoke-RestMethod https://api.github.com/repos/GreatWebGuy/MobTime/releases/latest).assets |
    Where-Object { $_.name -like '*.msi' } | Select-Object -First 1 -ExpandProperty browser_download_url
Invoke-WebRequest $mobtimeMsiUrl -O MobTime.msi
./MobTime.msi /qr

& "${env:ProgramFiles}\Google\Chrome\Application\chrome.exe" https://app.mindmup.com/map/new

# Clean up the task bar
Start-Process -Verb RunAs choco 'install syspin --ignore-checksums'
syspin "C:\Program Files\Google\Chrome\Application\chrome.exe" "Pin to taskbar"
syspin "C:\Users\Administrator\AppData\Local\GitHubDesktop\GitHubDesktop.exe" "Pin to taskbar"
syspin  "C:\Users\Administrator\AppData\Local\MobTime\MobTime.exe" "Pin to taskbar"
syspin "C:\Program Files\internet explorer\iexplore.exe" "Unpin from taskbar"

Start-Process -Verb RunAs choco 'install taskbar-winconfig --params "'/CORTANA:no /INK:no /PEOPLE:no /TASKVIEW:no /KEYBOARD:no'"'
Start-Process -Verb RunAs choco 'uninstall taskbar-winconfig'

