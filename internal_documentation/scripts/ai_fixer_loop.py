import subprocess
import sys
import os

def get_script_path(script_name):
    """Gets the absolute path to the script, adding .cmd for Windows."""
    base_path = os.path.join(os.path.dirname(__file__), script_name)
    if sys.platform == "win32":
        return f"{base_path}.cmd"
    return base_path

def run_command(command, check=True):
    """Runs a command and returns its output."""
    print(f"-> Running: {' '.join(command)}")
    process = subprocess.run(command, capture_output=True, text=True, check=False)
    if check and process.returncode != 0:
        print(f"Error running command: {' '.join(command)}")
        print(process.stdout)
        print(process.stderr)
        raise subprocess.CalledProcessError(process.returncode, command, process.stdout, process.stderr)
    return process

def play_chime():
    """Plays a system sound to indicate a successful operation."""
    print("-> Playing success chime.")
    if sys.platform == "win32":
        import winsound
        winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)
    elif sys.platform == "darwin":
        subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])
    # No default sound for Linux

def main_loop():
    """Main loop to find, fix, and commit problems."""
    print("Starting AI Fixer Loop...")

    # 1. Initial check
    print("\nStep 1: Performing initial system check...")
    initial_check_script = get_script_path("check_that_fix_works")
    if not os.path.exists(initial_check_script):
        print(f"Error: Script not found at {initial_check_script}")
        return
        
    try:
        run_command([initial_check_script])
        print("Initial check passed. System is stable.")
    except subprocess.CalledProcessError:
        print("Initial 'check_that_fix_works' failed. Aborting.")
        return

    # 2. Main loop
    for i in range(1000):
        print(f"\n--- Iteration {i + 1} ---")
        # Find problems
        print("Step 2: Finding problems...")
        find_problems_script = get_script_path("find_problems")
        result = run_command([find_problems_script], check=False)

        if not result.stdout.strip():
            print("No problems found. All done!")
            break

        print(f"Problem found: {result.stdout.strip()}")

        # Fix problem
        print("Step 3: Attempting to fix the problem...")
        fix_problem_script = get_script_path("fix_problem")
        run_command([fix_problem_script])

        # Check if the fix worked
        print("Step 4: Verifying the fix...")
        try:
            run_command([initial_check_script])
            print("Verification passed.")

            # Commit the fix
            print("Step 5: Committing the changes...")
            commit_script = get_script_path("commit")
            run_command([commit_script])
            print("Commit successful.")
            play_chime()

        except subprocess.CalledProcessError:
            print("Verification failed. Reverting changes.")
            run_command(["git", "reset", "--hard"])
            print("Changes have been reverted.")
    else:
        print("\nReached maximum number of iterations (1000). Stopping.")

if __name__ == "__main__":
    main_loop()
