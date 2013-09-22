import unittest
import os
from StringWriter import StringWriter
from random import randint


class WriterTests(unittest.TestCase):
    def test_writes_file(self):
        contents = "foo" + str(randint(0, 100))
        sw = StringWriter(contents)
        fileName = './stuff.txt'
        sw.write_received_file(fileName)

        received = open(fileName, 'r')
        self.assertEqual(contents, received.read())
        received.close()
        os.remove(fileName)

    def test_received_name(self):
        sw = StringWriter(None)
        fileName = sw.GetReceivedFileName('./stuff')
        self.assertEqual(fileName, './stuff.received.txt')

    def test_approved_name(self):
        sw = StringWriter(None)
        fileName = sw.GetApprovedFileName('./stuff')
        self.assertEqual(fileName, './stuff.approved.txt')

    def test_alternative_extension(self):
        sw = StringWriter(None, '.html')
        fileName = sw.GetApprovedFileName('./stuff')
        self.assertEqual(fileName, './stuff.approved.html')


if __name__ == '__main__':
    unittest.main()
