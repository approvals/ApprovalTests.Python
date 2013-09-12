import unittest
import os
from Namer import Namer
from ReceivedFileLauncherReporter import ReceivedFileLauncherReporter
from random import randint

class ReporterTests(unittest.TestCase):
    def test_file_launcher(self):
        reporter = ReceivedFileLauncherReporter()
        reporter.Report("a.txt",r"C:\Users\Chris\Documents\GitHub\ApprovalTests.Python\src\b.txt")
        
if __name__ == '__main__':
    unittest.main()
