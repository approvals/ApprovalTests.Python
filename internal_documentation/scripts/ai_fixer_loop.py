import argparse
import subprocess
import time
from pathlib import Path

_SCRIPT_DIR = Path(__file__).parent.resolve()

SUCCESS_EMOJI = "✅"
FAILURE_EMOJI = "❌"


def get_script_path(script_name: Path) -> Path:
    # The scripts are in the same directory as this script
    base_path = _SCRIPT_DIR / script_name
    return base_path


def run_script(script_path: Path, display_name: str) -> bool:
    start_time = time.time()
    result = subprocess.run(
        script_path.as_posix(),
        check=False,
        capture_output=True,
        text=True,
        shell=True,
        encoding="utf-8",
    )
    end_time = time.time()
    duration = end_time - start_time

    if result.returncode == 0:
        print(f"{SUCCESS_EMOJI} {display_name} [{duration:.2f}s]")
    else:
        print(f"{FAILURE_EMOJI} {display_name} [{duration:.2f}s]")
        if result.stdout:
            print("--- STDOUT ---")
            print(result.stdout)
        if result.stderr:
            print("--- STDERR ---")
            print(result.stderr)

    return result.returncode == 0


def get_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="AI-Powered Loop Fixer.", prog="ai_fixer_loop"
    )
    parser.add_argument(
        "--find",
        type=Path,
        default="find_problems",
        help="The script to run to find problems.",
    )
    parser.add_argument(
        "--fix",
        type=Path,
        default="fix_problem",
        help="The script to run to fix problems.",
    )
    parser.add_argument(
        "--tcr",
        type=Path,
        default="tcr",
        help="The script for Test && Commit || Revert.",
    )
    return parser


def main() -> None:
    parser = get_argument_parser()
    args = parser.parse_args()

    find_script = get_script_path(args.find)
    fix_script = get_script_path(args.fix)
    tcr_script = get_script_path(args.tcr)

    print("Running initial check...")
    initial_check = run_script(tcr_script, "tcr: committed")
    if not initial_check:
        print(f"{FAILURE_EMOJI} Initial build is broken. Aborting.")
        return
    print(f"{SUCCESS_EMOJI} build working")

    for i in range(1, 1001):
        print("-----------------------------")
        print(f"Run #{i}")

        find_result = run_script(find_script, "found problems")
        if not find_result:
            print("no more problems found.")
            break

        run_script(fix_script, "fix problem")

        start_time = time.time()
        tcr_result = subprocess.run(
            get_script_path(args.tcr).as_posix(),
            check=False,
            capture_output=True,
            text=True,
            shell=True,
            encoding="utf-8",
        )
        duration = time.time() - start_time
        if tcr_result.returncode == 0:
            print(f"{SUCCESS_EMOJI} tcr: committed [{duration:.2f}s]")
        else:
            print(f"{FAILURE_EMOJI} tcr: reverted [{duration:.2f}s]")

    else:  # This else belongs to the for loop
        print("Loop finished after 1000 runs. Stopping to prevent infinite loops.")


if __name__ == "__main__":
    main()
