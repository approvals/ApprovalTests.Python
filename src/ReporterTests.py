import unittest
from ReceivedFileLauncherReporter import ReceivedFileLauncherReporter

class ReporterTests(unittest.TestCase):
    def test_file_launcher(self):
        reporter = ReceivedFileLauncherReporter()
        command = reporter.get_command("a.txt","b.txt")
        self.assertEqual(command, ['cmd', '/C', 'start', 'b.txt', '/B'])
        
if __name__ == '__main__':
    unittest.main()
