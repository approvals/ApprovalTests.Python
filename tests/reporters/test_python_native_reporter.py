import os
from pathlib import Path

from approvaltests import verify

from approvaltests.reporters.python_native_reporter import *


def test_files_identical(tmpdir):
    file1 = os.path.join(str(tmpdir), "a.received.txt")
    file2 = os.path.join(str(tmpdir), "b.approved.txt")
    identical_contents = "abc"
    with open(file1, "w") as f1:
        f1.write(identical_contents)
    with open(file2, "w") as f2:
        f2.write(identical_contents)
    verify(calculate_diff(file1, file2))


def test_files_differ(tmpdir):
    file1 = os.path.join(str(tmpdir), "a.received.txt")
    file2 = os.path.join(str(tmpdir), "b.approved.txt")
    with open(file1, "w") as f1:
        f1.write("abc")
    with open(file2, "w") as f2:
        f2.write("def")
    diff = calculate_diff(file1, file2)
    diff = diff.replace(str(tmpdir), "tmpdir")  # use scrubber in future
    diff = diff.replace('\\', '/')

    verify(diff)

def test_approved_file_is_created_when_missing(tmpdir):
    file1 = os.path.join(str(tmpdir), "a.received.txt")
    file2 = os.path.join(str(tmpdir), "b.approved.txt")
    with open(file1, "w") as f1:
        f1.write("abc")
    reporter = PythonNativeReporter()
    reporter.report(file1, file2)
    assert Path(file2).exists()
