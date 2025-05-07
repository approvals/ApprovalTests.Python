import os
import unittest

from approvaltests.namer.default_namer_factory import NamerFactory, get_default_namer
from approvaltests.namer.stack_frame_namer import StackFrameNamer


class NamerTests(unittest.TestCase):
    def test_class(self) -> None:
        self.assertEqual("NamerTests", StackFrameNamer().get_class_name())

    def test_method(self) -> None:
        n = StackFrameNamer()
        self.assertEqual("test_method", n.get_method_name())

    def test_name_works_from_inside_an_other_method(self) -> None:
        self.an_other_method()

    def an_other_method(self) -> None:
        n = StackFrameNamer()
        self.assertEqual(
            "test_name_works_from_inside_an_other_method", n.get_method_name()
        )

    def test_file(self) -> None:
        directory = StackFrameNamer().get_directory()
        assert os.path.exists(directory + "/test_namer.py")

    def test_basename(self) -> None:
        n = StackFrameNamer()
        self.assertTrue(
            n.get_basename().endswith("NamerTests.test_basename"), n.get_basename()
        )

    def test_received_name(self) -> None:
        filename = StackFrameNamer().get_received_filename("./stuff")
        self.assertEqual(filename, "./stuff.received.txt")

    def test_approved_name(self) -> None:
        filename = StackFrameNamer().get_approved_filename("./stuff")
        self.assertEqual(filename, "./stuff.approved.txt")

    def test_alternative_extension(self) -> None:
        n = StackFrameNamer(extension=".html")
        filename = n.get_approved_filename("./stuff")
        self.assertEqual(filename, "./stuff.approved.html")

    def test_additional_information(self) -> None:
        assert_ends_with(
            NamerFactory.with_parameters("case1").namer.get_approved_filename(),
            "test_additional_information.case1.approved.txt",
        )
        assert_ends_with(
            NamerFactory.with_parameters(
                "case1", "case2"
            ).namer.get_approved_filename(),
            "test_additional_information.case1.case2.approved.txt",
        )
        assert_ends_with(
            get_default_namer().get_approved_filename(),
            "test_additional_information.approved.txt",
        )


def assert_ends_with(received_string: str, expected_ending: str) -> None:
    assert received_string.endswith(expected_ending)


if __name__ == "__main__":
    unittest.main()
