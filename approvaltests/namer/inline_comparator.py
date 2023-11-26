import tempfile
from inspect import FrameInfo
from pathlib import Path
from typing import Optional, Callable, Any

from approval_utilities.utilities.multiline_string_utils import remove_indentation_from
from approvaltests import Namer, StackFrameNamer, Reporter, DiffReporter


class InlinePythonReporter(Reporter):

    def __init__(self):
        self.test_source_file = self.get_test_source_file()
        self.diffReporter = DiffReporter()

    def report(self, received_path: str, approved_path: str) -> bool:
        # create a temp file of the based on the source,
        received_path = self.create_received_file(received_path)
        self.diffReporter.report(received_path, self.test_source_file)

    def get_test_source_file(self):
        test_stack_frame: FrameInfo = StackFrameNamer.get_test_frame()
        return test_stack_frame.filename

    def create_received_file(self, received_path: str):
        file = tempfile.NamedTemporaryFile(suffix=".received.txt", delete=False).name
        code = Path(self.test_source_file).read_text()
        received_text = Path(received_path).read_text()
        method_name = StackFrameNamer.get_test_frame().function
        code = self.swap(received_text, code, method_name)

        Path(file).write_text(code)
        return file

    def swap(self, received_text, code, method_name):
        code = code.replace(method_name, f"def {method_name}(): \n\t'''\n\t{received_text}\n\t'''")

        return code


class InlineComparator(Namer):
    def get_approved_filename(self, base: Optional[str] = None) -> str:
        file = tempfile.NamedTemporaryFile(suffix=".approved.txt", delete=False).name
        docs = self.get_test_method_doc_string()
        Path(file).write_text(docs)
        return file

    def get_received_filename(self, base: Optional[str] = None) -> str:
        return tempfile.NamedTemporaryFile(suffix=".received.txt", delete=False).name

    def get_test_method_doc_string(self):
        test_stack_frame: FrameInfo = StackFrameNamer.get_test_frame()
        method: Callable[..., Any] = self.get_caller_method(test_stack_frame)
        return remove_indentation_from(method.__doc__)

    def get_caller_method(self, caller_frame) -> Callable:
        caller_function_name: str = caller_frame[3]
        caller_function_object = caller_frame.frame.f_globals.get(
            caller_function_name, None
        )
        return caller_function_object


    def register(self, options: "Options"):
        return options.with_namer(self).with_reporter(InlinePythonReporter())
