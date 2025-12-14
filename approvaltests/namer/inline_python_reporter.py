import tempfile
from inspect import FrameInfo
from pathlib import Path
from typing import Callable, Optional

from typing_extensions import override

from approvaltests import Reporter, StackFrameNamer
from approvaltests.inline.markers import PRESERVE_LEADING_WHITESPACE_MARKER
from approvaltests.inline.split_code import SplitCode


def handle_preceeding_whitespace(received_text: str) -> str:
    if not received_text:
        return received_text
    lines = received_text.split("\n")
    if all(
        (line.startswith(" ") or line.startswith("\t")) for line in lines if line != ""
    ):
        return f"{PRESERVE_LEADING_WHITESPACE_MARKER}" + received_text
    return received_text


def detect_trailing_whitespace(text: str) -> bool:
    if not text:
        return False
    return any(len(line) and line[-1] in " \t" for line in text.split("\n"))


def escape_backslashes(text: str) -> str:
    """
    Ensure literal backslashes in the approved docstring are preserved by escaping
    them in the source code injection so Python does not interpret sequences like
    "\n" or "\t".
    """
    if not text:
        return text
    return text.replace("\\", "\\\\")


escape_characters_dict = {
    v.encode().decode("unicode_escape"): v
    for v in [
        "\\x00",  # Null
        "\\b",  # Backspace
        "\\v",  # Vertical tab
        "\\f",  # Form feed
        "\\x1b",  # Escape
        "\\x7f",  # Delete
        "\\u00a0",  # Non-breaking space
        "\\u200b",  # Zero-width space
        "\\u200c",  # Zero-width non-joiner
        "\\u200d",  # Zero-width joiner
        "\\u200e",  # Left-to-right mark
        "\\u200f",  # Right-to-left mark
        "\\u202c",  # Pop directional formatting
        "\\u202d",  # Left-to-right override
        "\\u202e",  # Right-to-left override
        "\\u2028",  # Line separator
        "\\u2029",  # Paragraph separator
        "\\ufeff",  # Byte order mark
    ]
}


def escape_control_characters(text: str) -> str:
    if not text:
        return text

    translation_table = str.maketrans(escape_characters_dict)

    return text.translate(translation_table)


class InlinePythonReporter(Reporter):
    def __init__(
        self,
        reporter: Reporter,
        create_footer_function: Optional[Callable[[str, str], str]] = None,
    ):
        self.diffReporter = reporter
        self.footer_function = create_footer_function or (lambda __, ___: "")
        self.footer = ""

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        test_source_file = self.get_test_source_file()
        self.footer = self.footer_function(received_path, approved_path)
        received_path = self.create_received_file(received_path, test_source_file)
        return self.diffReporter.report(received_path, test_source_file)

    def get_test_source_file(self) -> str:
        test_stack_frame: FrameInfo = StackFrameNamer.get_test_frame()
        return test_stack_frame.filename

    def create_received_file(self, received_path: str, test_source_file: str) -> str:
        code = Path(test_source_file).read_text(encoding="utf-8")

        original_received_text = Path(received_path).read_text(encoding="utf-8")[:-1]
        received_text = original_received_text + self.footer
        received_text = handle_preceeding_whitespace(received_text)
        received_text = escape_backslashes(received_text)
        received_text = escape_control_characters(received_text)
        method_name = StackFrameNamer.get_test_frame().function
        if detect_trailing_whitespace(original_received_text):
            trailing_comment = "  # Warning: Editors may remove trailing spaces, causing this test to fail"
        else:
            trailing_comment = ""

        new_code = self.swap(
            received_text, code, method_name, after_docstring_comment=trailing_comment
        )
        file = tempfile.NamedTemporaryFile(suffix=".received.txt", delete=False).name
        Path(file).write_text(new_code, encoding="utf-8")
        return file

    def swap(
        self,
        received_text: str,
        code: str,
        method_name: str,
        after_docstring_comment: str = "",
    ) -> str:
        split_code = SplitCode.on_method(code, method_name)
        return "\n".join(
            [
                split_code.before_method,
                split_code.tab + '"""',
                split_code.indent(received_text),
                split_code.tab + '"""' + after_docstring_comment,
                split_code.after_method,
            ]
        )
