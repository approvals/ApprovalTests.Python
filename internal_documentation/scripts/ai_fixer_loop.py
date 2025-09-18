import subprocess
import time
import argparse
import platform
import os


def get_script_path(script_name):
    # Go up two directories to get to the project root from the script's location
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    base_path = os.path.join(project_root, script_name)
    if platform.system() == "Windows":
        return f"{base_path}.cmd"
    else:
        return base_path


def run_script(script_path, display_name):
    start_time = time.time()
    script_dir = os.path.dirname(script_path)
    # We use shell=True for Windows to correctly execute .cmd files
    use_shell = platform.system() == "Windows"
    result = subprocess.run(os.path.basename(script_path), capture_output=True, text=True, shell=use_shell, cwd=script_dir)
    end_time = time.time()
    duration = end_time - start_time

    if result.returncode == 0:
        print(f"✅ {display_name} [{duration:.2f}s]")
    else:
        print(f"❌ {display_name} [{duration:.2f}s]")
        if result.stdout:
            print("--- STDOUT ---")
            print(result.stdout)
        if result.stderr:
            print("--- STDERR ---")
            print(result.stderr)

    return result


def main():
    parser = argparse.ArgumentParser(description="AI-Powered Loop Fixer.")
    parser.add_argument("--find", default="find_problems", help="The script to run to find problems.")
    parser.add_argument("--fix", default="fix_problem", help="The script to run to fix problems.")
    parser.add_argument("--tcr", default="tcr", help="The script for Test && Commit || Revert.")
    args = parser.parse_args()

    find_script = get_script_path(args.find)
    fix_script = get_script_path(args.fix)
    tcr_script = get_script_path(args.tcr)

    print("Running initial check...")
    initial_check = run_script(tcr_script, "tcr: committed")
    if initial_check.returncode != 0:
        print("❌ Initial build is broken. Aborting.")
        return
    print("✅ build working")

    for i in range(1, 1001):
        print(f"-----------------------------")
        print(f"Run #{i}")

        find_result = run_script(find_script, "found problems")
        if find_result.returncode != 0:
            print("no more problems found.")
            break

        run_script(fix_script, "fix problem")
        
        start_time = time.time()
        tcr_result = subprocess.run(get_script_path(args.tcr), capture_output=True, text=True, shell=platform.system() == "Windows", cwd=os.path.dirname(get_script_path(args.tcr)))
        duration = time.time() - start_time
        if tcr_result.returncode == 0:
            print(f"✅ tcr: committed [{duration:.2f}s]")
        else:
            print(f"❌ tcr: reverted [{duration:.2f}s]")

    else: # This else belongs to the for loop
        print("Loop finished after 1000 runs. Stopping to prevent infinite loops.")

if __name__ == "__main__":
    main()
