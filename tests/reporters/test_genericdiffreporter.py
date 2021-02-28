import json
import os
import re
import shutil
import unittest

from approvaltests.approvals import verify, get_default_namer
from approvaltests.command import Command
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter, create_config
from approvaltests.reporters.generic_diff_reporter_factory import (
    GenericDiffReporterFactory,
)
import approvaltests
from approvaltests.core.namer import Namer
from approvaltests.utils import to_json, is_windows_os


class GenericDiffReporterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = GenericDiffReporterFactory()
        self.reporter = self.factory.get_first_working()
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)
        os.mkdir(self.tmp_dir)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp_dir)

    def test_list_configured_reporters(self) -> None:
        verify(to_json(self.factory.list()), self.reporter)

    def test_get_reporter(self) -> None:
        verify(str(self.factory.get("BeyondCompare4")), self.reporter)

    def test_get_winmerge(self) -> None:
        verify(str(self.factory.get("WinMerge")), self.factory.get("WinMerge"))

    def test_get_araxis(self) -> None:
        verify(
            str(self.factory.get("AraxisMergeWin")), self.factory.get("AraxisMergeWin")
        )

    def test_get_araxis_mac(self) -> None:
        verify(
            str(self.factory.get("AraxisMergeMac")), self.factory.get("AraxisMergeMac")
        )

    def test_get_beyondcompare4_mac(self) -> None:
        verify(
            str(self.factory.get("BeyondCompare4Mac")),
            self.factory.get("BeyondCompare4Mac"),
        )

    def test_constructs_valid_diff_command(self) -> None:
        reporter = self.factory.get("BeyondCompare4")
        namer = get_default_namer()
        received = namer.get_received_filename()
        approved = namer.get_approved_filename()
        command = reporter.get_command(received, approved)
        expected_command = [reporter.path, received, approved]
        self.assertEqual(command, expected_command)

    def test_empty_approved_file_created_when_one_does_not_exist(self) -> None:
        namer = get_default_namer()
        received = namer.get_received_filename()
        approved = namer.get_approved_filename()
        if os.path.isfile(approved):
            os.remove(approved)
        self.assertFalse(os.path.isfile(approved))

        reporter = self.factory.get("BeyondCompare4")
        reporter.run_command = lambda command_array: None
        reporter.is_working = lambda: True
        reporter.report(received, approved)
        self.assertEqual(0, os.stat(approved).st_size)

    def test_approved_file_not_changed_when_one_exists_already(self) -> None:
        namer = get_default_namer()
        approved_contents = "Approved"
        approved = namer.get_approved_filename()
        os.remove(approved)
        with open(approved, "w") as approved_file:
            approved_file.write(approved_contents)
        reporter = self.factory.get("BeyondCompare4")
        reporter.run_command = lambda command_array: None

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
                verify(file_contents, self.reporter)
        finally:
            os.remove(saved_reporters_file)

    def test_deserialization(self) -> None:
        namer = get_default_namer()
        full_name = os.path.join(namer.get_directory(), "custom-reporters.json")
        reporters = self.factory.load(full_name)
        verify(to_json(reporters), self.reporter)

    def test_notworking_in_environment(self) -> None:
        reporter = GenericDiffReporter(create_config(["Custom", "NotReal"]))
        self.assertFalse(reporter.is_working())

    def test_find_working_reporter(self) -> None:
        r = self.factory.get_first_working()
        if r:
            self.assertTrue(r.is_working())

    def test_remove_reporter(self) -> None:
        self.factory.remove("meld")
        verify(to_json(self.factory.list()), self.reporter)

    @staticmethod
    def instantiate_reporter_for_test() -> GenericDiffReporter:
        program = r"C:\Windows\System32\help.exe" if is_windows_os() else "echo"
        reporter = GenericDiffReporter.create(program)
        reporter.run_command = lambda command_array: None
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

    def test_approved_file_not_changed_when_one_exists_already(self) -> None:
        approved_contents = "Approved"
        with open(self.approved_file_path, "w") as approved_file:
            approved_file.write(approved_contents)
        reporter = self.instantiate_reporter_for_test()
        reporter.report(self.received_file_path, self.approved_file_path)

        with open(self.approved_file_path, "r") as approved_file:
            actual_contents = approved_file.read()
        self.assertEqual(actual_contents, approved_contents)

    def assertFileDoesNotExist(self, file_path: str) -> None:
        file_exists = os.path.isfile(file_path)
        if file_exists:
            msg = "File {} exists when it shouldn't".format(file_path)
            self.fail(msg)

    def assertFileIsEmpty(self, file_path: str) -> None:
        file_size = os.stat(file_path).st_size
        if file_size != 0:
            msg = "File is not empty: {}" % file_path
            self.fail(msg)

    def test_get_pycharm_reporter(self) -> None:
        verify(str(self.factory.get("PyCharm")), reporter=self.reporter)

    def test_non_working_reporter_does_not_report(self) -> None:
        self.assertFileDoesNotExist(self.approved_file_path)

        reporter = GenericDiffReporter(create_config(["Custom", "NotReal"]))
        success = reporter.report(self.received_file_path, self.approved_file_path)

        self.assertFalse(success)
