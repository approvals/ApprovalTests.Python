#!/usr/bin/env python

import os
import sys
from difflib import unified_diff

from approvaltests.reporters import get_command_text


def calculate_diff(file1, file2):
    with open(file1) as f1:
        with open(file2) as f2:
            diff = unified_diff(f2.readlines(),
                                f1.readlines(),
                                os.path.basename(file2),
                                os.path.basename(file1))
            diff_string = "\n".join(diff)
            if diff_string.strip():
                approve = get_command_text(file1, file2)
                approve_cmd = "\n\nto approve this result:\n\n" + approve + "\n"
            else:
                approve_cmd = ""
            return diff_string + approve_cmd


if __name__ == '__main__':
    fileA, fileB = sys.argv[1:3]
    print(calculate_diff(fileA, fileB))
