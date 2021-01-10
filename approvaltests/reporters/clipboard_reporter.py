import pyperclip

from approvaltests.core.reporter import Reporter


def get_command_text(received_path, approved_path):
    return 'mv -f {0} {1}'.format(received_path, approved_path)


class ClipboardReporter(Reporter):
    """
    A blocking reporter that creates
    a command line suitable for approving
    the last failed test on systems that
    support terminal command 'mv'.
    """

    def report(self, received_path, approved_path):
        text = get_command_text(received_path, approved_path)
        print(text)
        pyperclip.copy(text)
        return True


class CommandLineReporter(Reporter):
    """
    A blocking reporter that outputs
    command lines suitable for approving
    failing tests on systems that support
    terminal command 'mv'.
    """

    def report(self, received_path, approved_path):
        text = get_command_text(received_path, approved_path)
        print('\n\n{}\n\n'.format(text))
        return True
