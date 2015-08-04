import inspect
import os


class Namer(object):
    ClassName = ''
    MethodName = ''
    Directory = ''

    def setForStack(self, caller):
        stackFrame = caller[self.frame]
        self.MethodName = stackFrame[3]
        self.ClassName = stackFrame[0].f_globals["__name__"]
        self.Directory = os.path.dirname(stackFrame[1])

    def __init__(self, frame=1):
        self.frame = frame
        self.setForStack(inspect.stack(1))

    def getClassName(self):
        return self.ClassName

    def getMethodName(self):
        return self.MethodName

    def getDirectory(self):
        return self.Directory

    def get_basename(self):
        return os.path.join(self.Directory, self.ClassName + "." + self.MethodName)
