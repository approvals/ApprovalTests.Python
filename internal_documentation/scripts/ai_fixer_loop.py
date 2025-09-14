import subprocess
import os
import sys
from subprocess import CompletedProcess

if sys.platform == "win32":
    import winsound

# Script Names
CHECK_SCRIPT = "check_that_fix_works"
FIND_PROBLEMS_SCRIPT = "find_problems"
FIX_PROBLEM_SCRIPT = "fix_problem"
COMMIT_SCRIPT = "commit"





def run_command(command: str, check: bool = True) -> CompletedProcess:
    print(f"-> Running: {command}")
    return subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=check, shell=True
    )



def play_chime() -> None:
    print("-> Playing success chime.")
    if sys.platform == "win32":
        winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)
    elif sys.platform == "darwin":
        run_command("afplay /System/Library/Sounds/Glass.aiff")


def perform_initial_check() -> bool:
    print("\nStep 1: Performing initial system check...")
    result = run_command(CHECK_SCRIPT, check=False)
    if result.returncode == 0:
        print("Initial check passed. System is stable.")
        return True
    else:
        print("Initial 'check_that_fix_works' failed. Aborting.")
        print(result.stdout)
        return False


def find_problems() -> bool:
    print("Step 2: Finding problems...")
    result = run_command(FIND_PROBLEMS_SCRIPT, check=False)
    if result.returncode != 0:
        print(f"Problem found: {result.stdout.strip()}")
    return result.returncode == 0

def fix_and_verify() -> bool:
    print("Step 3: Attempting to fix the problem...")
    run_command(FIX_PROBLEM_SCRIPT)

    print("Step 4: Verifying the fix...")
    try:
        run_command(CHECK_SCRIPT)
        print("Verification passed.")
        return True
    except subprocess.CalledProcessError:
        print("Verification failed. Reverting changes.")
        run_command("git reset --hard")
        print("Changes have been reverted.")
        return False


def commit_changes() -> None:
    print("Step 5: Committing the changes...")
    run_command(COMMIT_SCRIPT)
    print("Commit successful.")
    play_chime()


def main_loop() -> None:
    print("Starting AI Fixer Loop...")
    if not perform_initial_check():
        return

    for i in range(1000):
        print(f"\n--- Iteration {i + 1} ---")
        if find_problems():
            print("No problems found. All done!")
            break

        if fix_and_verify():
            commit_changes()
    else:
        print("\nReached maximum number of iterations (1000). Stopping.")


if __name__ == "__main__":
    main_loop()
