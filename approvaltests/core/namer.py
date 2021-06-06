import inspect
import json
import os
from inspect import FrameInfo
from typing import Dict, List, Optional

from approvaltests.approval_exception import FrameNotFound


class Namer(object):
    APPROVED = ".approved"
    RECEIVED = ".received"

    def __init__(self, extension: Optional[str] = None) -> None:
        self.extension_with_dot = extension or ".txt"

    def get_file_name(self):
        raise Exception("This class is abstract, override this method in a subclass")

    def get_directory(self):
        raise Exception("This class is abstract, override this method in a subclass")

    def get_config(self):
        raise Exception("This class is abstract, override this method in a subclass")

    def get_basename(self) -> str:
        file_name = self.get_file_name()
        subdirectory = self.get_config().get("subdirectory", "")
        return os.path.join(self.get_directory(), subdirectory, file_name)

    def get_received_filename(self, basename: Optional[str] = None) -> str:
        basename = basename or self.get_basename()
        return basename + Namer.RECEIVED + self.extension_with_dot

    def get_approved_filename(self, basename: Optional[str] = None) -> str:
        basename = basename or self.get_basename()
        return basename + Namer.APPROVED + self.extension_with_dot

    def set_extension(self, extension):
        self.extension_with_dot = extension


class StackFrameNamer(Namer):
    Directory = ""
    MethodName = ""
    ClassName = ""

    def __init__(self, extension: Optional[str] = None) -> None:
        Namer.__init__(self, extension)
        self.set_for_stack(inspect.stack(1))
        self.config: Dict[str, str] = {}
        self.config_loaded = False

    def set_for_stack(self, caller: List[FrameInfo]) -> None:
        frame = self.get_test_frame(caller)
        stacktrace = caller[frame]
        self.MethodName = stacktrace[3]
        self.ClassName = self.get_class_name_for_frame(stacktrace)
        self.Directory = os.path.dirname(stacktrace[1])

    def get_class_name_for_frame(self, stacktrace: FrameInfo) -> str:
        if "self" not in stacktrace[0].f_locals:
            return os.path.splitext(os.path.basename(stacktrace[1]))[0]
        else:
            return stacktrace[0].f_locals["self"].__class__.__name__

    def get_test_frame(self, caller: List[FrameInfo]) -> int:
        tmp_array = []
        for index, frame in enumerate(caller):
            if self.is_test_method(frame):
                tmp_array.append(index)
        if tmp_array:
            return tmp_array[-1]
        message = """Could not find test method/function. Possible reasons could be: 
1) approvaltests is not being used inside a test function 
2) your test framework is not supported by ApprovalTests (unittest and pytest are currently supported)."""
        raise FrameNotFound(message)

    def is_test_method(self, frame: FrameInfo) -> bool:
        is_unittest_test = (
            "self" in frame[0].f_locals
            and "_testMethodName" in frame[0].f_locals["self"].__dict__
            and frame[3] != "__call__"
            and frame[3] != "run"
        )

        is_pytest_test = frame[3].startswith("test_")

        return is_unittest_test or is_pytest_test

    def get_class_name(self) -> str:
        return self.ClassName

    def get_method_name(self) -> str:
        return self.MethodName

    def get_directory(self) -> str:
        return self.Directory

    def config_directory(self) -> str:
        return self.Directory

    def get_config(self) -> Dict[str, str]:
        """lazy load config when we need it, then store it in the instance variable self.config"""
        if not self.config_loaded:
            config_file = os.path.join(
                self.config_directory(), "approvaltests_config.json"
            )
            if os.path.exists(config_file):
                with open(config_file, "r") as f:
                    self.config = json.load(f)
            else:
                self.config = {}
            self.config_loaded = True
        return self.config

    def get_file_name(self) -> str:
        class_name = "" if (self.ClassName is None) else (self.ClassName + ".")
        return class_name + self.MethodName
