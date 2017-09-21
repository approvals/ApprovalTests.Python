import pyperclip

from approvaltests.core.reporter import Reporter


def get_command_text(received_path, approved_path):
    return 'mv -f {0} {1}'.format(received_path, approved_path)


class ClipboardReporter(Reporter):
    def report(self, received_path, approved_path):
        text = get_command_text(received_path, approved_path)
        print(text)
        pyperclip.copy(text)
        return True


class CommandLineReporter(Reporter):
    def report(self, received_path, approved_path):
        text = get_command_text(received_path, approved_path)
        print('\n\n{}\n\n'.format(text))
        return True
