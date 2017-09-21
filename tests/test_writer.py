import os
import unittest
from random import randint

from approvaltests.string_writer import StringWriter


class WriterTests(unittest.TestCase):
    def test_writes_file(self):
        contents = "foo" + str(randint(0, 100))
        sw = StringWriter(contents)
        filename = './stuff.txt'
        sw.write_received_file(filename)

        with open(filename, 'r') as received:
            self.assertEqual(contents, received.read())

        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
