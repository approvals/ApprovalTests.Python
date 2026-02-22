import os
import shutil
import unittest

from typing_extensions import override

from approval_utilities.utils import is_windows_os, to_json
from approvaltests.approvals import delete_approved_file, get_default_namer, verify
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter
from approvaltests.reporters.generic_diff_reporter_config import (
    GenericDiffReporterConfig,
    create_config,
)
from approvaltests.reporters.generic_diff_reporter_factory import (
    GenericDiffReporterFactory,
)


class GenericDiffReporterTests(unittest.TestCase):
    @override
    def setUp(self) -> None:
        GenericDiffReporter.reset_opened_diff_tool_count()
        self.factory = GenericDiffReporterFactory()
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)
        os.mkdir(self.tmp_dir)

    @override
    def tearDown(self) -> None:
        shutil.rmtree(self.tmp_dir)

    def test_constructs_valid_diff_command(self) -> None:
        reporter = GenericDiffReporter.create("test")
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

        reporter = GenericDiffReporter.create("test")

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
        reporter = GenericDiffReporter.create("test")
        setattr(reporter, "run_command", lambda command_array: None)

        reporter.report(namer.get_received_filename(), approved)

        with open(approved) as approved_file:
            actual_contents = approved_file.read()
        self.assertEqual(actual_contents, approved_contents)

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
            msg = f"File {file_path} exists when it shouldn't"
            self.fail(msg)

    def assertFileIsEmpty(self, file_path: str) -> None:
        file_size = os.stat(file_path).st_size
        if file_size != 0:
            msg = f"File is not empty: {file_path}"
            self.fail(msg)

    def test_get_from_reporters_json(self) -> None:
        verify(str(self.factory.get("CustomName")))

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

    def test_get_command_appends_files_when_no_placeholder(self) -> None:
        config = GenericDiffReporterConfig("test", "/usr/bin/diff", ["-u"])
        reporter = GenericDiffReporter(config)
        result = reporter.get_command("received.txt", "approved.txt")
        self.assertEqual(result, ["/usr/bin/diff", "-u", "received.txt", "approved.txt"])

    def test_get_command_substitutes_standalone_placeholders(self) -> None:
        config = GenericDiffReporterConfig("kdiff3", "/usr/bin/kdiff3", ["%s", "%s", "-m"])
        reporter = GenericDiffReporter(config)
        result = reporter.get_command("received.txt", "approved.txt")
        self.assertEqual(result, ["/usr/bin/kdiff3", "received.txt", "approved.txt", "-m"])

    def test_get_command_substitutes_embedded_placeholders(self) -> None:
        config = GenericDiffReporterConfig("tortoise", "/path/to/tortoise", ["/left:%s", "/right:%s"])
        reporter = GenericDiffReporter(config)
        result = reporter.get_command("received.txt", "approved.txt")
        self.assertEqual(result, ["/path/to/tortoise", "/left:received.txt", "/right:approved.txt"])

    def test_get_command_with_no_extra_args(self) -> None:
        config = GenericDiffReporterConfig("simple", "/usr/bin/simple")
        reporter = GenericDiffReporter(config)
        result = reporter.get_command("received.txt", "approved.txt")
        self.assertEqual(result, ["/usr/bin/simple", "received.txt", "approved.txt"])
