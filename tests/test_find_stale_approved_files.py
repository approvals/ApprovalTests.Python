import os
import subprocess
import sys
import tempfile
from typing import List, Tuple

from approval_utilities.utilities.logger.simple_logger import SimpleLogger
from approvaltests import Options, verify_argument_parser
from approvaltests.scrubbers import create_regex_scrubber
from approvaltests.utilities.logger.simple_logger_approvals import verify_simple_logger
from tests.find_stale_approved_files import create_argument_parser


# Create a temporary sandbox directory and log file
def create_sandbox(
    approved_files: List[str], log_entries: List[str], nested: bool = False
) -> Tuple[tempfile.TemporaryDirectory, str]:
    sandbox_dir = tempfile.TemporaryDirectory()
    log_file_path = os.path.join(sandbox_dir.name, "approvedfiles.log")

    # Create approved files in the sandbox
    for file_name in approved_files:
        if nested:
            nested_dir = os.path.join(sandbox_dir.name, "nested")
            os.makedirs(nested_dir, exist_ok=True)
            open(os.path.join(nested_dir, file_name), "w").close()
        else:
            open(os.path.join(sandbox_dir.name, file_name), "w").close()

    # Write the log entries to the log file
    with open(log_file_path, "w") as log_file:
        for entry in log_entries:
            if nested:
                log_file.write(os.path.join(sandbox_dir.name, "nested", entry) + "\n")
            else:
                log_file.write(os.path.join(sandbox_dir.name, entry) + "\n")

    return sandbox_dir, log_file_path


# Execute the comparison script
def execute_script(directory: str, log_file: str) -> None:

    script = "find_stale_approved_files.py"
    dirname = os.path.dirname(__file__)
    full_script = os.path.join(dirname, script)
    print(f"Executing script: {full_script=}")
    result = subprocess.run(
        [sys.executable, full_script, directory, log_file],
        capture_output=True,
        text=True,
    )
    output = result.stdout
    SimpleLogger.message(output)


def test_create_argument_parser() -> None:
    verify_argument_parser(create_argument_parser())


def test_find_stale_approved_files() -> None:
    scrubber = create_regex_scrubber(r".+(?=file\d\.)", "")
    with verify_simple_logger(options=Options().with_scrubber(scrubber)):
        # Test Scenario 1: All approved files are in the log
        SimpleLogger.message("Test Scenario 1: All approved files are in the log")
        approved_files_1 = [
            "file1.approved.txt",
            "file2.approved.doc",
            "file3.approved.csv",
        ]
        log_entries_1 = approved_files_1
        verify_files(approved_files_1, log_entries_1)

        # Test Scenario 2: Approved files that are not in the log
        SimpleLogger.message("Test Scenario 2: Approved files that are not in the log")
        approved_files_2 = [
            "file1.approved.txt",
            "file2.approved.doc",
            "file3.approved.csv",
            "file4.approved.md",
        ]
        log_entries_2 = approved_files_2[
            :-1
        ]  # Exclude 'file4.approved.md' from the log
        verify_files(approved_files_2, log_entries_2)

        # Test Scenario 3: Log contains files that are not in the directory
        SimpleLogger.message(
            "Test Scenario 3: Log contains files that are not in the directory"
        )
        approved_files_3 = ["file1.approved.txt", "file2.approved.doc"]
        log_entries_3 = approved_files_3 + [
            "file3.approved.csv"
        ]  # 'file3.approved.csv' is in the log but not in the directory
        verify_files(approved_files_3, log_entries_3)

        # Test Scenario 4: No approved files in the directory
        SimpleLogger.message("Test Scenario 4: No approved files in the directory")
        verify_files([], ["file1.approved.txt", "file2.approved.doc"])

        # Test Scenario 5: Directory has files but none are in the log
        SimpleLogger.message(
            "Test Scenario 5: Directory has files but none are in the log"
        )
        verify_files(["file1.approved.txt", "file2.approved.doc"], [])

        # Test Scenario 6: Nested folders with approved files
        SimpleLogger.message("Test Scenario 6: Nested folders with approved files")
        approved_files_6 = ["file1.approved.txt", "file2.approved.doc"]
        verify_files(approved_files_6, approved_files_6, nested=True)

        # Test Scenario 7: Files that do not match the naming convention
        SimpleLogger.message(
            "Test Scenario 7: Files that do not match the naming convention"
        )
        approved_files_7 = ["file1.txt", "file2.doc", "file3.csv"]
        verify_files(approved_files_7, approved_files_7)

        SimpleLogger.message(
            "Test Scenario 8: Log contains files that are not in the directory"
        )
        approved_files = ["custom_name_1.txt"]
        log_entries = approved_files + ["custom_name_2.txt"]
        verify_files(approved_files, log_entries)


def verify_files(
    approved_files: List[str], log_entries: List[str], nested: bool = False
) -> None:
    SimpleLogger.variable("Approved Files", approved_files)
    SimpleLogger.variable("Log Entries", log_entries)

    sandbox_dir, log_file_path = create_sandbox(
        approved_files, log_entries, nested=nested
    )
    execute_script(sandbox_dir.name, log_file_path)
    sandbox_dir.cleanup()
