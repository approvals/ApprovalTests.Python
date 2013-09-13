import unittest
import os
import shutil
import filecmp
from Namer import Namer
from StringWriter import StringWriter
from random import randint
from Reporter import Reporter

class FileApprover(object):
    def verify(self, namer, writer, reporter):
        #get base
        base = namer.get_basename()
        approved = writer.GetApprovedFileName(base)
        received = writer.WriteReceivedFile(writer.GetReceivedFileName(base))
        self.verify_files(approved, received, reporter)
        #get approved 
        
        #get received file
        #write recieved file
        #verify files
        
    
    def verify_files(self,approved_file, received_file,reporter):
        #if the two files are the same do nothing
        if(self.are_files_the_same(approved_file, received_file)):
            os.remove(received_file)
        else:
            reporter.report(approved_file,received_file)
            
        # or call reporter

    def are_files_the_same(self,approved_file,received_file):
        if(not self.FileExists(approved_file) or not self.FileExists(received_file)):
            return False 
        
        if(os.stat(approved_file).st_size != os.stat(received_file).st_size):
            return False
        else:
            return filecmp.cmp(approved_file,received_file)
            
    def FileExists(self,path):
        try:
           with open(path): pass
           return True
        except IOError:
           print ('File does not exist ' + path)
           return False
       
class TestingReporter(Reporter):
    
    def __init__(self):
        self.called = False
    
    def report(self,approved_path,received_path):
        self.called = True

class FileApproverTests(unittest.TestCase):
    def test_compare_same_files(self):
        approver = FileApprover()
        shutil.copy("a.txt","a_same.txt")
        approver.verify_files("a.txt","a_same.txt", None)

    def test_compare_different_files(self):
        approver = FileApprover()
        reporter = TestingReporter()
        approver.verify_files("a.txt","b.txt", reporter)
        self.assertTrue(reporter.called)
    
    def test_full(self):
        namer =  Namer()
        writer = StringWriter("b")
        reporter = TestingReporter()
        approver = FileApprover()
        approver.verify(namer, writer, reporter)
        self.assertTrue(reporter.called)
        
        
        
if __name__ == '__main__':
    unittest.main()
