import tempfile
from inspect import FrameInfo
from pathlib import Path

from approvaltests import Reporter, StackFrameNamer
from approvaltests.inline.split_code import SplitCode

DELETE_ME_TO_APPROVE_ = "\n***** DELETE ME TO APPROVE *****"


class InlinePythonReporter(Reporter):
    def __init__(self, reporter, add_approval_line=False, previous_result=None):
        self.diffReporter = reporter
        self.semi_automatic_extra_line = (
            DELETE_ME_TO_APPROVE_ if add_approval_line else ""
        )
        self.previous_result = previous_result

    def report(self, received_path: str, approved_path: str) -> bool:
        test_source_file = self.get_test_source_file()
        if self.previous_result:
            previous_result_stuff = lambda: "\n" + "vvvvv PREVIOUS RESULT vvvvv" + "\n" + "41"
            self.semi_automatic_extra_line = DELETE_ME_TO_APPROVE_ + previous_result_stuff()
        received_path = self.create_received_file(received_path, test_source_file)
        return self.diffReporter.report(received_path, test_source_file)

    def get_test_source_file(self):
        test_stack_frame: FrameInfo = StackFrameNamer.get_test_frame()
        return test_stack_frame.filename

    def create_received_file(self, received_path: str, test_source_file: str):
        code = Path(test_source_file).read_text()

        received_text = (
            Path(received_path).read_text()[:-1] + self.semi_automatic_extra_line
        )
        method_name = StackFrameNamer.get_test_frame().function
        new_code = self.swap(received_text, code, method_name)
        file = tempfile.NamedTemporaryFile(suffix=".received.txt", delete=False).name
        Path(file).write_text(new_code)
        return file

    def swap(self, received_text, code, method_name):
        split_code = SplitCode.on_method(code, method_name)
        return f'{split_code.before_method}\n{split_code.tab}"""\n{split_code.indent(received_text)}\n{split_code.tab}"""\n{split_code.after_method}'
