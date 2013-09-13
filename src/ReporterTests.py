import unittest
import os
from Namer import Namer
from ReceivedFileLauncherReporter import ReceivedFileLauncherReporter
from random import randint
from numpy.ma.testutils import assert_equal

class ReporterTests(unittest.TestCase):
    def test_file_launcher(self):
        reporter = ReceivedFileLauncherReporter()
        command = reporter.get_command("a.txt","b.txt")
        
        assert_equal(command, ['cmd', '/C', 'start', 'b.txt', '/B'])
        
if __name__ == '__main__':
    unittest.main()
