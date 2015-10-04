import os
import shutil
import unittest
from approvaltests.TextDiffReporter import TextDiffReporter


class TextDiffReportertests(unittest.TestCase):
    @staticmethod
    def set_environment_variable(name, value):
        os.environ[name] = value

    @staticmethod
    def instantiate_reporter_for_test():
        reporter = TextDiffReporter()
        reporter.run_command = lambda command_array: None
        return reporter

    @property
    def tmp_dir(self):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(test_dir, 'tmp')

    @property
    def received_file_path(self):
        return os.path.join(
            self.tmp_dir,
            'received_file.txt'
        )

    @property
    def approved_file_path(self):
        return os.path.join(
            self.tmp_dir,
            'approved_file.txt'
        )

    def setUp(self):
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)
        os.mkdir(self.tmp_dir)
        self.diff_tool = 'echo'
        self.set_environment_variable(
            TextDiffReporter.DIFF_TOOL_ENVIRONMENT_VARIABLE_NAME,
            self.diff_tool
        )
        open(self.received_file_path, 'w').close()


    def tearDown(self):
        shutil.rmtree(self.tmp_dir)

    def test_constructs_valid_diff_command(self):
        reporter = self.instantiate_reporter_for_test()
        command = reporter.get_command(
            self.approved_file_path,
            self.received_file_path
        )
        expected_command = [
            self.diff_tool,
            self.received_file_path,
            self.approved_file_path
        ]
        self.assertEqual(command, expected_command)

    def test_empty_approved_file_created_when_one_does_not_exist(self):
        self.assertFileDoesNotExist(self.approved_file_path)

        reporter = self.instantiate_reporter_for_test()
        reporter.report(self.approved_file_path, self.received_file_path)

        self.assertFileIsEmpty(self.approved_file_path)

    def test_approved_file_not_changed_when_one_exists_already(self):
        approved_contents = "Approved"
        with open(self.approved_file_path, 'w') as approved_file:
            approved_file.write(approved_contents)
        reporter = self.instantiate_reporter_for_test()
        reporter.report(self.approved_file_path, self.received_file_path)

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
