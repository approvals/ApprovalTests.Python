#!/usr/bin/env python3
"""
Delinter - Automated linting fix process

This script runs three scripts in sequence:
1. check_that_fix_works - Run tests
2. find_problems - Run linting  
3. run_claude - Fix issues with Claude
"""

import subprocess
import sys
import os
from pathlib import Path

_SCRIPT_DIR = Path(__file__).parent


def run_script(script_name: str) -> bool:
    """Run a script and return True if successful."""
    print(f"Running: {script_name}")
    try:
        result = subprocess.run(
            str(_SCRIPT_DIR / script_name), 
            shell=True, 
            check=True
        )
        print(f"✅ {script_name} completed successfully")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ {script_name} failed")
        return False


def main() -> None:
    """Main delinter process."""
    print("🚀 Starting delinter process...")
    
    # Change to the repository root
    repo_root = _SCRIPT_DIR.parent.parent
    os.chdir(repo_root)
    print(f"Working directory: {os.getcwd()}")
    
    scripts = ["check_that_fix_works", "find_problems", "run_claude"]
    
    for script in scripts:
        if not run_script(script):
            print(f"❌ Delinter failed at {script}")
            sys.exit(1)
    
    print("🎉 Delinter process completed successfully!")


if __name__ == "__main__":
    main()
