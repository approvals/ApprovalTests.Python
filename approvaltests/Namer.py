import inspect
import os


class Namer(object):
    ClassName = ''
    MethodName = ''
    Directory = ''

    APPROVED = '.approved'
    RECEIVED = '.received'

    def __init__(self, extension='.txt'):
        self.extension_with_dot = extension
        self.set_for_stack(inspect.stack(1))

    def get_class_name(self):
        return self.ClassName

    def get_method_name(self):
        return self.MethodName

    def get_directory(self):
        return self.Directory

    def get_basename(self):
        return os.path.join(self.Directory, self.ClassName + "." + self.MethodName)

    def get_received_filename(self, basename=None):
        basename = basename or self.get_basename()
        return basename + self.RECEIVED + self.extension_with_dot

    def get_approved_filename(self, basename=None):
        basename = basename or self.get_basename()
        return basename + self.APPROVED + self.extension_with_dot

    def set_for_stack(self, caller):
        frame = self.get_test_frame(caller)
        stacktrace = caller[frame]
        self.MethodName = stacktrace[3]
        self.ClassName = stacktrace[0].f_locals["self"].__class__.__name__
        self.Directory = os.path.dirname(stacktrace[1])

    def get_test_frame(self, caller):
        frameNumber = 1
        for index, frame in enumerate(caller):
            if "self" in frame[0].f_locals \
                    and "_testMethodName" in frame[0].f_locals["self"].__dict__ \
                    and frame[3] is not "__call__" \
                    and frame[3] is not "run":
                frameNumber = index

        return frameNumber