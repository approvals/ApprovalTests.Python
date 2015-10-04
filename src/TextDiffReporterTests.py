import os
import shutil
import unittest
from approvaltests.TextDiffReporter import TextDiffReporter


class TextDiffReportertests(unittest.TestCase):
    @property
    def tmp_dir(self):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(test_dir, 'tmp')

    def setUp(self):
        shutil.rmtree(self.tmp_dir)
        os.mkdir(self.tmp_dir)

    def test_constructs_valid_diff_command(self):
        diff_tool = 'meld'
        approved_path = 'a.txt'
        received_path = 'b.txt'
        os.environ[TextDiffReporter.DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME] = diff_tool
        reporter = TextDiffReporter()
        command = reporter.get_command(approved_path, received_path)
        self.assertEqual(command, [diff_tool, approved_path, received_path])

    def test_empty_approved_file_created_when_one_does_not_exist(self):
        diff_tool = 'echo'
        receieved_file_path = 'b.txt'
        approved_file_path = os.path.join(self.tmp_dir, 'approved_file.txt')
        os.environ[TextDiffReporter.DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME] = diff_tool
        self.assertFileDoesNotExist(approved_file_path)

        reporter = TextDiffReporter()
        reporter.report(approved_file_path, receieved_file_path)

        self.assertFileIsEmpty(approved_file_path)

    def assertFileDoesNotExist(self, file_path):
        file_exists = os.path.isfile(file_path)
        if file_exists:
            msg = "File {} exists when it shouldn't".format(file_path)
            self.fail(msg)

    def assertFileIsEmpty(self, file_path):
        file_size = os.stat(file_path).st_size
        if file_size != 0:
            msg = "File is not empty: {}" % file_path
            self.fail(msg)


if __name__ == '__main__':
    unittest.main()
