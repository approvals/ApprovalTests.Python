import pyperclip  # type: ignore

from approvaltests.core.reporter import Reporter


def get_command_text(received_path: str, approved_path: str) -> str:
    return "mv -f {0} {1}".format(received_path, approved_path)


class ClipboardReporter(Reporter):
    """
    A reporter that creates
    a command line suitable for approving
    the last failed test on systems that
    support terminal command 'mv', and puts
    the command on the clipboard, over-writes
    the previous clipboard contents.

    See also CommandLineReporter.
    """

    def report(self, received_path, approved_path):
        text = get_command_text(received_path, approved_path)
        print(text)
        pyperclip.copy(text)
        return True


class CommandLineReporter(Reporter):
    """
    A reporter that outputs a
    command line suitable for approving
    failing tests on systems that support
    terminal command 'mv'.

    The output is typically copied and pasted
    to a console window or script, to approve
    the new test results.

    See also ClipboardReporter.
    """

    def report(self, received_path, approved_path):
        text = get_command_text(received_path, approved_path)
        print("\n\n{}\n\n".format(text))
        return True
