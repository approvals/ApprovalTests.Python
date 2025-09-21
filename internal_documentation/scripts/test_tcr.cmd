@echo off
setlocal


set COUNT_FILE=..\..\.ignore\count.txt
if not exist "..\..\.ignore" mkdir "..\..\.ignore"

if not exist "%COUNT_FILE%" (
    echo 0 > "%COUNT_FILE%"
)

set /p count= < "%COUNT_FILE%"

if %count% == 2 exit /b 1
if %count% == 4 (
    echo 0 > "%COUNT_FILE%"
    exit /b 1
)

exit /b 0
