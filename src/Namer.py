import inspect

class Namer(object):
    """description of class"""
    
    ClassName = ''
    MethodName = ''
    def __init__(self):
        caller = inspect.stack(1)
        self.MethodName = caller[1][3]
        self.ClassName = caller[1][0].f_globals["__name__"]
        pass

    def getClassName(self):
         return self.ClassName
     
    def getMethodName(self):
         return self.MethodName
