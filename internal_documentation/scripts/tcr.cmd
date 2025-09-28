@echo off
setlocal

call mise run test

if %ERRORLEVEL% EQU 0 (
    git add -A
    git commit -F ".ignore\commit-message.txt"
    if %ERRORLEVEL% EQU 0 (
        echo ✅ tcr: committed
        exit /b 0
    ) else (
        echo ❌ tcr: commit failed
        exit /b 1
    )
) else (
    git checkout -- .
    git clean -fd
    echo ❌ tcr: reverted
    exit /b 1
)