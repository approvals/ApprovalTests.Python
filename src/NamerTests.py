import unittest
import os
from Namer import Namer

class NamerTests(unittest.TestCase):
    def test_class(self):
        n = Namer() 
        self.assertEqual("NamerTests", n.getClassName())
                
    def test_method(self):
        n = Namer() 
        self.assertEqual("test_method", n.getMethodName())
    
    def test_file(self):
        n = Namer() 
        self.assertTrue(os.path.exists(n.getDirectory() + "/NamerTests.py"))
    
if __name__ == '__main__':
    unittest.main()
