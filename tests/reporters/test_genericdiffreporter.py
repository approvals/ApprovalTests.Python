import os
import re
import shutil
import unittest
from typing import cast

from approvaltests import Options
from approvaltests.approvals import verify, get_default_namer, delete_approved_file
from approvaltests.reporters import MultiReporter
from approvaltests.reporters.generic_diff_reporter import (
    GenericDiffReporter,
)
from approvaltests.reporters.generic_diff_reporter_config import create_config
from approvaltests.reporters.generic_diff_reporter_factory import (
    GenericDiffReporterFactory,
)
from approvaltests.reporters.report_with_beyond_compare import ReportWithBeyondCompare
from approval_utilities.utils import to_json, is_windows_os


class GenericDiffReporterTests(unittest.TestCase):
    def setUp(self) -> None:
        GenericDiffReporter.reset_opened_diff_tool_count()
        self.factory = GenericDiffReporterFactory()
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)
        os.mkdir(self.tmp_dir)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp_dir)

    def test_list_configured_reporters(self) -> None:
        verify(to_json(self.factory.list()))

    def test_document_existing_reporters(self) -> None:
        reporters = self.factory.list()
        reporters.sort()
        markdown = ""
        for reporter in reporters:
            markdown += f"* {reporter}\n"

        verify(markdown, options=Options().for_file.with_extension(".md"))

    def test_get_reporter(self) -> None:
        verify(str(self.factory.get("BeyondCompare4")))

    def test_get_winmerge(self) -> None:
        self.assert_for_reporter("WinMerge")

    def test_get_araxis(self) -> None:
        self.assert_for_reporter("AraxisMergeWin")

    def assert_for_reporter(self, reporter):
        the_reporter = self.factory.get(reporter)
        verify(
            str(the_reporter), MultiReporter(ReportWithBeyondCompare(), the_reporter)
        )

    def test_get_araxis_mac(self) -> None:
        self.assert_for_reporter("AraxisMergeMac")

    def test_get_beyondcompare4_mac(self) -> None:
        self.assert_for_reporter("BeyondCompare4Mac")

    def test_constructs_valid_diff_command(self) -> None:
        reporter = cast(GenericDiffReporter, self.factory.get("BeyondCompare4"))
        namer = get_default_namer()
        received = namer.get_received_filename()
        approved = namer.get_approved_filename()
        command = reporter.get_command(received, approved)
        expected_command = [reporter.path, received, approved]
        self.assertEqual(command, expected_command)

    def test_empty_approved_file_created_when_one_does_not_exist(self) -> None:
        delete_approved_file()
        
        namer = get_default_namer()
        received = namer.get_received_filename()
        approved = namer.get_approved_filename()
        self.assertFalse(os.path.isfile(approved))

        reporter = self.factory.get("BeyondCompare4")

        setattr(reporter, "run_command", lambda command_array: None)
        setattr(reporter, "is_working", lambda: True)
        reporter.report(received, approved)
        self.assertEqual(0, os.stat(approved).st_size)
        delete_approved_file()

    def test_approved_file_not_changed_when_one_exists_already(self) -> None:
        namer = get_default_namer()
        approved = namer.get_approved_filename()
        os.remove(approved)
        approved_contents = "Approved"
        with open(approved, "w") as approved_file:
            approved_file.write(approved_contents)
        reporter = self.factory.get("BeyondCompare4")
        setattr(reporter, "run_command", lambda command_array: None)

        reporter.report(namer.get_received_filename(), approved)

        with open(approved, "r") as approved_file:
            actual_contents = approved_file.read()
        self.assertEqual(actual_contents, approved_contents)

    def test_serialization(self) -> None:
        n = get_default_namer()
        saved_reporters_file = os.path.join(n.get_directory(), "saved-reporters.json")
        self.factory.save(saved_reporters_file)
        try:
            with open(saved_reporters_file, "r") as f:
                file_contents = f.read()
                # remove the absolute path to the python_native_reporter.py file since it is different on every machine
                regex = re.compile(r'.*"([^"]*)python_native_reporter.py')
                match = regex.findall(file_contents)
                if match:
                    file_contents = file_contents.replace(match[0], "")
                file_contents = file_contents.replace("python.exe", "python")
                verify(file_contents)
        finally:
            os.remove(saved_reporters_file)

    def test_deserialization(self) -> None:
        namer = get_default_namer()
        full_name = os.path.join(namer.get_directory(), "custom-reporters.json")
        reporters = self.factory.load(full_name)
        verify(to_json(reporters))

    def test_notworking_in_environment(self) -> None:
        reporter = GenericDiffReporter(create_config(["Custom", "NotReal"]))
        self.assertFalse(reporter.is_working())

    def test_find_working_reporter(self) -> None:
        r = self.factory.get_first_working()
        if r:
            self.assertTrue(r.is_working())

    def test_remove_reporter(self) -> None:
        self.factory.remove("meld")
        verify(to_json(self.factory.list()))

    @staticmethod
    def instantiate_reporter_for_test() -> GenericDiffReporter:
        program = r"C:\Windows\System32\help.exe" if is_windows_os() else "echo"
        reporter = GenericDiffReporter.create(program)
        setattr(reporter, "run_command", lambda command_array: None)
        return reporter

    @property
    def tmp_dir(self) -> str:
        test_dir = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(test_dir, "tmp")

    @property
    def received_file_path(self) -> str:
        return os.path.join(self.tmp_dir, "received_file.txt")

    @property
    def approved_file_path(self) -> str:
        return os.path.join(self.tmp_dir, "approved_file.txt")

    def test_empty_approved_file_created_when_one_does_not_exist_2(self) -> None:
        self.assertFileDoesNotExist(self.approved_file_path)

        reporter = self.instantiate_reporter_for_test()
        reporter.report(self.received_file_path, self.approved_file_path)

        self.assertFileIsEmpty(self.approved_file_path)

    def assertFileDoesNotExist(self, file_path: str) -> None:
        file_exists = os.path.isfile(file_path)
        if file_exists:
            msg = "File {} exists when it shouldn't".format(file_path)
            self.fail(msg)

    def assertFileIsEmpty(self, file_path: str) -> None:
        file_size = os.stat(file_path).st_size
        if file_size != 0:
            msg = f"File is not empty: {file_path}"
            self.fail(msg)

    def test_get_pycharm_reporter(self) -> None:
        verify(str(self.factory.get("PyCharm")))

    def test_diff_tool_limiting(self) -> None:
        reporter = self.instantiate_reporter_for_test()
        for i in range(0, 7):
            reporter.report("a.txt", "b.txt")
        assert 7 == GenericDiffReporter.opened_diff_tool_count
        assert 2 == reporter.get_limit_count()
        os.remove("b.txt")

    def test_non_working_reporter_does_not_report(self) -> None:
        self.assertFileDoesNotExist(self.approved_file_path)

        reporter = GenericDiffReporter(create_config(["Custom", "NotReal"]))
        success = reporter.report(self.received_file_path, self.approved_file_path)

        self.assertFalse(success)

    def _test_string_representation(self) -> None:
        reporter = GenericDiffReporter(create_config(["Custom", "NotReal"]))
        expected = "GenericDiffReporter(...)"
        self.assertEqual(expected, str(reporter))
