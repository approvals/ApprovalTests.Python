import os
import sys
import tempfile
import subprocess

from approvaltests import Options
from approvaltests.utilities.logger.simple_logger_approvals import verify_simple_logger
from approval_utilities.utilities.logger.simple_logger import SimpleLogger
from scrubbers import create_regex_scrubber


# Create a temporary sandbox directory and log file
def create_sandbox(approved_files, log_entries, nested=False):
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
def execute_script(directory, log_file):
    result = subprocess.run(
        [sys.executable, "find_stale_approved_files.py", directory, log_file],
        capture_output=True,
        text=True,
    )
    output = result.stdout
    SimpleLogger.message(output)


def test_find_stale_approved_files():
    scrubber = create_regex_scrubber(r".+(?=file\d\.)", "<FULL PATH>")
    with verify_simple_logger(options=Options().with_scrubber(scrubber)):
        # Test Scenario 1: All approved files are in the log
        SimpleLogger.message("Test Scenario 1: All approved files are in the log")
        approved_files_1 = [
            "file1.approved.txt",
            "file2.approved.doc",
            "file3.approved.csv",
        ]
        log_entries_1 = approved_files_1
        sandbox_dir_1, log_file_path_1 = create_sandbox(approved_files_1, log_entries_1)
        execute_script(sandbox_dir_1.name, log_file_path_1)
        sandbox_dir_1.cleanup()

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
        sandbox_dir_2, log_file_path_2 = create_sandbox(approved_files_2, log_entries_2)
        execute_script(sandbox_dir_2.name, log_file_path_2)
        sandbox_dir_2.cleanup()

        # Test Scenario 3: Log contains files that are not in the directory
        SimpleLogger.message(
            "Test Scenario 3: Log contains files that are not in the directory"
        )
        approved_files_3 = ["file1.approved.txt", "file2.approved.doc"]
        log_entries_3 = approved_files_3 + [
            "file3.approved.csv"
        ]  # 'file3.approved.csv' is in the log but not in the directory
        sandbox_dir_3, log_file_path_3 = create_sandbox(approved_files_3, log_entries_3)
        execute_script(sandbox_dir_3.name, log_file_path_3)
        sandbox_dir_3.cleanup()

        # Test Scenario 4: No approved files in the directory
        SimpleLogger.message("Test Scenario 4: No approved files in the directory")
        approved_files_4 = []  # No files in the directory
        log_entries_4 = ["file1.approved.txt", "file2.approved.doc"]
        sandbox_dir_4, log_file_path_4 = create_sandbox(approved_files_4, log_entries_4)
        execute_script(sandbox_dir_4.name, log_file_path_4)
        sandbox_dir_4.cleanup()

        # Test Scenario 5: Directory has files but none are in the log
        SimpleLogger.message(
            "Test Scenario 5: Directory has files but none are in the log"
        )
        approved_files_5 = ["file1.approved.txt", "file2.approved.doc"]
        log_entries_5 = []  # No entries in the log
        sandbox_dir_5, log_file_path_5 = create_sandbox(approved_files_5, log_entries_5)
        execute_script(sandbox_dir_5.name, log_file_path_5)
        sandbox_dir_5.cleanup()

        # Test Scenario 6: Nested folders with approved files
        SimpleLogger.message("Test Scenario 6: Nested folders with approved files")
        approved_files_6 = ["file1.approved.txt", "file2.approved.doc"]
        log_entries_6 = approved_files_6
        sandbox_dir_6, log_file_path_6 = create_sandbox(
            approved_files_6, log_entries_6, nested=True
        )
        execute_script(sandbox_dir_6.name, log_file_path_6)
        sandbox_dir_6.cleanup()

        # Test Scenario 7: Files that do not match the naming convention
        SimpleLogger.message(
            "Test Scenario 7: Files that do not match the naming convention"
        )
        approved_files_7 = ["file1.txt", "file2.doc", "file3.csv"]
        log_entries_7 = approved_files_7
        sandbox_dir_7, log_file_path_7 = create_sandbox(approved_files_7, log_entries_7)
        execute_script(sandbox_dir_7.name, log_file_path_7)
        sandbox_dir_7.cleanup()
