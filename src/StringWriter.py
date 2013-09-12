import inspect
import os

class StringWriter(object):
    """description of class"""
 
    extention_with_dot = None
    contents=None
    RECEIVED = '.received'
    APPROVED = '.approved'
    
  
    def __init__(self,contents,extension='.txt'):
        self.contents = contents
        self.extention_with_dot=extension

    def WriteReceivedFile(self, receivedFile):
        f = open(receivedFile,'w')
        f.write(self.contents);
        f.close()
        return receivedFile
    
    def GetReceivedFileName(self, basename):
        return basename + self.RECEIVED + self.extention_with_dot;
    
    def GetApprovedFileName(self, basename):
        return basename + self.APPROVED + self.extention_with_dot;
        
        
        