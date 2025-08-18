import tempfile
from inspect import FrameInfo
from pathlib import Path
from typing import Any, Callable, Optional

from typing_extensions import override

from approval_utilities.utilities.multiline_string_utils import remove_indentation_from
from approval_utilities.utilities.stack_frame_utilities import get_class_name_for_frame
from approvaltests import Namer, StackFrameNamer
from approvaltests.core.options import Options
from approvaltests.inline.inline_options import InlineOptions
from approvaltests.inline.markers import (
    PRESERVE_LEADING_WHITESPACE_MARKER,
)
from approvaltests.namer.inline_python_reporter import InlinePythonReporter
from approvaltests.reporters import ReporterThatAutomaticallyApproves


class InlineComparator(Namer):
    @override
    def get_approved_filename(self, base: Optional[str] = None) -> str:
        file = tempfile.NamedTemporaryFile(suffix=".approved.txt", delete=False).name
        docs = self.get_test_method_doc_string()
        Path(file).write_text(docs)
        return file

    @override
    def get_received_filename(self, base: Optional[str] = None) -> str:
        return tempfile.NamedTemporaryFile(suffix=".received.txt", delete=False).name

    @staticmethod
    def get_test_method_doc_string() -> str:
        test_stack_frame: FrameInfo = StackFrameNamer.get_test_frame()
        method: Callable[..., Any] = InlineComparator.get_caller_method(
            test_stack_frame
        )
        doc = remove_indentation_from(method.__doc__)
        if doc.startswith(PRESERVE_LEADING_WHITESPACE_MARKER):
            return doc[len(PRESERVE_LEADING_WHITESPACE_MARKER) :]
        return doc

    @staticmethod
    def get_caller_method(caller_frame: FrameInfo) -> Callable:
        caller_function_name: str = caller_frame[3]
        caller_function_object = caller_frame.frame.f_globals.get(caller_function_name)
        if caller_function_object:
            # pytest function
            return caller_function_object
        else:
            # unittest class function
            className = get_class_name_for_frame(caller_frame)
            clazz = caller_frame.frame.f_globals.get(className)
            caller_function_object = clazz.__dict__.get(caller_function_name)
            return caller_function_object

    def register(
        self, options: Options, inline_options: Optional[InlineOptions] = None
    ) -> Options:
        inline_options = (
            InlineOptions.show_code() if inline_options is None else inline_options
        )
        options2 = options.with_namer(self)
        options2 = inline_options.apply(options2)

        return options2
