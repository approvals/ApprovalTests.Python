import unittest
import os
from Namer import Namer

class WriterTests(unittest.TestCase):
    def test_recieved_name(self):
        sw = StringWriter()
        self.assertEquals("")
        
    
if __name__ == '__main__':
    unittest.main()
