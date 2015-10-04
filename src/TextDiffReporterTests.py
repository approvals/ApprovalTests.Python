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
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)
        os.mkdir(self.tmp_dir)
        self.receieved_file_path = 'b.txt'
        self.approved_file_path = os.path.join(
            self.tmp_dir,
            'approved_file.txt'
        )
        self.diff_tool = 'echo'
        os.environ[TextDiffReporter.DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME] = self.diff_tool

    def tearDown(self):
        shutil.rmtree(self.tmp_dir)

    def test_constructs_valid_diff_command(self):
        reporter = TextDiffReporter()
        command = reporter.get_command(self.approved_file_path, self.receieved_file_path)
        self.assertEqual(command, [self.diff_tool, self.approved_file_path, self.receieved_file_path])

    def test_empty_approved_file_created_when_one_does_not_exist(self):
        self.assertFileDoesNotExist(self.approved_file_path)

        reporter = TextDiffReporter()
        reporter.report(self.approved_file_path, self.receieved_file_path)

        self.assertFileIsEmpty(self.approved_file_path)

    def test_approved_file_not_changed_when_one_exists_already(self):
        approved_contents = "Approved"
        with open(self.approved_file_path, 'w') as approved_file:
            approved_file.write(approved_contents)
        reporter = TextDiffReporter()
        reporter.report(self.approved_file_path, self.receieved_file_path)

        with open(self.approved_file_path, 'r') as approved_file:
            actual_contents = approved_file.read()
        self.assertEqual(actual_contents, approved_contents)

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
