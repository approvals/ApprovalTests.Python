import pyperclip

from approvaltests import Reporter
from approvaltests.reporters import get_command_text


class ReporterByCopyMoveCommandForEverythingToClipboard(Reporter):
    text = ''

    def report(self, received_path, approved_path):
        ReporterByCopyMoveCommandForEverythingToClipboard.text = ReporterByCopyMoveCommandForEverythingToClipboard.text + get_command_text(received_path, approved_path) + '\n'
        pyperclip.copy(ReporterByCopyMoveCommandForEverythingToClipboard.text)
        return True