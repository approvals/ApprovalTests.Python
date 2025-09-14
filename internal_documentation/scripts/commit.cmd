@echo off
rem Check if there are any changes to commit
git diff-index --quiet HEAD --
if errorlevel 1 (
    git commit -a -m "AI Fixer: Auto-fix"
) else (
    echo No changes to commit.
)