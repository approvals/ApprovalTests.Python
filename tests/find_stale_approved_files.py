#! /usr/bin/env python3
import argparse
import os
import pathlib
from pathlib import Path
from typing import List, Set


def find_approved_files(directory: pathlib.Path) -> List[Path]:
    return list(directory.rglob("*.approved.*"))


def read_approved_files_log(log_path: pathlib.Path) -> Set[pathlib.Path]:
    lines = log_path.read_text().split("\n")
    return set(map(pathlib.Path, lines))


def compare_files(found_files: List[Path], log_files: Set[Path]) -> List[Path]:
    not_in_log = [file for file in found_files if file not in log_files]
    return not_in_log


def main() -> None:
    args = create_argument_parser().parse_args()

    found_files = find_approved_files(args.directory)
    log_files = read_approved_files_log(args.log_file)

    missing_files = compare_files(found_files, log_files)

    if missing_files:
        print("The following files are not in the approved log:")
        for file in sorted(missing_files):
            print(file)
    else:
        print("All found approved files are present in the log.")


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__),
        description="Compare found approved files with log file.",
    )
    parser.add_argument(
        "directory", type=pathlib.Path, help="Directory to search for approved files"
    )
    parser.add_argument(
        "log_file", type=pathlib.Path, help="Path to the approved files log"
    )
    return parser


if __name__ == "__main__":
    main()
