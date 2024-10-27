import os
import argparse
import pathlib
from typing import List, Set


def find_approved_files(directory: pathlib.Path) -> List[str]:
    approved_files = [str(file) for file in pathlib.Path(directory).rglob("*.approved.*")]
    return approved_files


def read_approved_files_log(log_path: pathlib.Path) -> Set[str]:
    with open(log_path, "r") as f:
        approved_files_log = set(line.strip() for line in f if line.strip())
    return approved_files_log


def compare_files(found_files: List[str], log_files: Set[str]) -> List[str]:
    not_in_log = [file for file in found_files if file not in log_files]
    return not_in_log


def main() -> None:
    args = create_argument_parser().parse_args()

    found_files = find_approved_files(args.directory)
    log_files = read_approved_files_log(args.log_file)

    missing_files = compare_files(found_files, log_files)

    if missing_files:
        print("The following files are not in the approved log:")
        for file in missing_files:
            print(file)
    else:
        print("All found approved files are present in the log.")


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__),
        description="Compare found approved files with log file."
    )
    parser.add_argument(
        "directory", type=pathlib.Path, help="Directory to search for approved files"
    )
    parser.add_argument("log_file", type=pathlib.Path, help="Path to the approved files log")
    return parser


if __name__ == "__main__":
    main()