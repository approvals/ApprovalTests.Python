import os
import unittest

from approvaltests.core.namer import Namer, StackFrameNamer


class NamerTests(unittest.TestCase):
    def setUp(self):
        self.namer = StackFrameNamer()

    def test_class(self):
        self.assertEqual("NamerTests", self.namer.get_class_name())

    def test_method(self):
        n = StackFrameNamer()
        self.assertEqual("test_method", n.get_method_name())

    def test_file(self):
        self.assertTrue(os.path.exists(self.namer.get_directory() + "/test_namer.py"))

    def test_basename(self):
        n = StackFrameNamer()
        self.assertTrue(n.get_basename().endswith("NamerTests.test_basename"), n.get_basename())

    def test_received_name(self):
        filename = self.namer.get_received_filename('./stuff')
        self.assertEqual(filename, './stuff.received.txt')

    def test_approved_name(self):
        filename = self.namer.get_approved_filename('./stuff')
        self.assertEqual(filename, './stuff.approved.txt')

    def test_alternative_extension(self):
        n = Namer(extension='.html')
        filename = n.get_approved_filename('./stuff')
        self.assertEqual(filename, './stuff.approved.html')


if __name__ == '__main__':
    unittest.main()
