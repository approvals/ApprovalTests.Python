import os
from random import randint
import unittest
from approvaltests.StringWriter import StringWriter


class WriterTests(unittest.TestCase):
    def test_writes_file(self):
        contents = "foo" + str(randint(0, 100))
        sw = StringWriter(contents)
        filename = './stuff.txt'
        sw.write_received_file(filename)

        received = open(filename, 'r')
        self.assertEqual(contents, received.read())
        received.close()
        os.remove(filename)

    def test_received_name(self):
        sw = StringWriter(None)
        filename = sw.GetReceivedFileName('./stuff')
        self.assertEqual(filename, './stuff.received.txt')

    def test_approved_name(self):
        sw = StringWriter(None)
        filename = sw.GetApprovedFileName('./stuff')
        self.assertEqual(filename, './stuff.approved.txt')

    def test_alternative_extension(self):
        sw = StringWriter(None, '.html')
        filename = sw.GetApprovedFileName('./stuff')
        self.assertEqual(filename, './stuff.approved.html')


if __name__ == '__main__':
    unittest.main()
