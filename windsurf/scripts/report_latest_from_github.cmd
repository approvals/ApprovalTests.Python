@echo off
setlocal

if "%1"=="" (
    echo Usage: %0 YYYY-MM-DD
    echo Example: %0 2025-04-27
    exit /b 1
)

set "SINCE_DATE=%1"

gh issue list --search "created:>=%SINCE_DATE%" --json number,title,url,createdAt --template "{{range .}}#{{.number}} {{.title}} ({{.url}}) - Created: {{.createdAt | timeago}}{{end}}"
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to fetch issues. Ensure GitHub CLI is installed and configured.
)

gh pr list --search "created:>=%SINCE_DATE%" --json number,title,url,createdAt --template "{{range .}}#{{.number}} {{.title}} ({{.url}}) - Created: {{.createdAt | timeago}}{{end}}"
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to fetch pull requests. Ensure GitHub CLI is installed and configured.
)

endlocal