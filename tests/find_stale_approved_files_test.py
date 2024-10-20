import os
import tempfile
import subprocess

# Create a temporary sandbox directory and log file
def create_sandbox():
    sandbox_dir = tempfile.TemporaryDirectory()
    log_file_path = os.path.join(sandbox_dir.name, 'approvedfiles.log')

    # Create a few approved files in the sandbox
    approved_files = [
        'file1.approved.txt',
        'file2.approved.doc',
        'file3.approved.csv'
    ]
    for file_name in approved_files:
        open(os.path.join(sandbox_dir.name, file_name), 'w').close()

    # Write the approved files to the log file
    with open(log_file_path, 'w') as log_file:
        for file_name in approved_files:
            log_file.write(os.path.join(sandbox_dir.name, file_name) + '\n')

    return sandbox_dir, log_file_path

# Execute the comparison script
def execute_script(directory, log_file):
    subprocess.run(['python', 'find_stale_approved_files.py', directory, log_file])

if __name__ == "__main__":
    # Create the sandbox environment
    sandbox_dir, log_file_path = create_sandbox()

    # Execute the script
    execute_script(sandbox_dir.name, log_file_path)

    # Cleanup
    sandbox_dir.cleanup()
