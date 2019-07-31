#!/usr/bin/env python

import filecmp
import os
import sys
from difflib import unified_diff

from approvaltests.reporters import get_command_text


def calculate_diff(file1, file2):
    if filecmp.cmp(file1, file2):
        return "Files are identical"
    else:
        with open(file1) as f1:
            with open(file2) as f2:
                diff = unified_diff(f1.readlines(),
                                    f2.readlines(),
                                    os.path.basename(file1),
                                    os.path.basename(file2))
                diff_string = "\n".join(diff)
                approve = get_command_text(file1, file2)
                approve_cmd = "\n\nto approve this result:\n\n" + approve + "\n"
                return diff_string + approve_cmd


if __name__ == '__main__':
    fileA, fileB = sys.argv[1:3]
    print(calculate_diff(fileA, fileB))
