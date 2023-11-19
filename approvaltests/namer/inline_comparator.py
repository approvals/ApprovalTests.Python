import tempfile
from inspect import FrameInfo
from pathlib import Path
from typing import Optional, Callable, Any

from approval_utilities.utilities.multiline_string_utils import remove_indentation_from
from approvaltests import Namer, StackFrameNamer


class InlineComparator(Namer):
    def get_approved_filename(self, base: Optional[str] = None) -> str:
        file = tempfile.NamedTemporaryFile(suffix=".approved.txt", delete=False)
        # talk away....
        # get test method doc string
        docs = self.get_test_method_doc_string()

        # write to file
        #file.write(docs.encode("utf-8"))
        Path(file.name).write_text(docs)
        return file.name

    def get_received_filename(self, base: Optional[str] = None) -> str:
        file = tempfile.NamedTemporaryFile(suffix=".received.txt", delete=False)
        return file.name
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
        return options.with_namer(self)
