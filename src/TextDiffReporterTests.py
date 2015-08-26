import os
import unittest
from approvaltests.TextDiffReporter import TextDiffReporter

class TextDiffReportertests(unittest.TestCase):
    def test_constructs_valid_diff_command(self):
        diff_tool = 'meld'
        approved_path = 'a.txt'
        received_path = 'b.txt'
        os.environ[TextDiffReporter.DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME] = diff_tool
        reporter = TextDiffReporter()
        command = reporter.get_command(approved_path, received_path)
        self.assertEqual(command, [diff_tool, approved_path, received_path])

if __name__ == '__main__':
    unittest.main()
