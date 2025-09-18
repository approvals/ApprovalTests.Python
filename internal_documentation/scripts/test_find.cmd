@echo off
setlocal

set COUNT_FILE=..\..\.ignore\count.txt

if not exist "%COUNT_FILE%" (
    echo 0 > "%COUNT_FILE%"
)

set /p count= < "%COUNT_FILE%"
set /a count+=1
echo %count% > "%COUNT_FILE%"

REM Return exit code 0 if problems are found (count < 4), otherwise return 1.
if %count% LSS 4 (
    exit /b 0
) else (
    exit /b 1
)
