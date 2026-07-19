import unittest
from unittest.mock import MagicMock, patch

import psutil

from approvaltests import Options, verify
from approvaltests.inline.parse_docstring import parse_docstring
from approvaltests.reporters.intellij_reporter import (
    ReportWithIntellijTools,
    find_jetbrains_ides,
    get_running_process_paths,
)


# begin-snippet: use_intellij_reporter
class TestUseIntellijReporter(unittest.TestCase):
    def test_simple(self) -> None:
        verify("Hello", options=Options().with_reporter(ReportWithIntellijTools()))


# end-snippet


def test_find_jetbrains_ides() -> None:
    """
    /Applications/PyCharm.app/Contents/MacOS/pycharm -> /Applications/PyCharm.app/Contents/MacOS/pycharm
    /usr/bin/idea -> /usr/bin/idea
    C:\\Program Files\\JetBrains\\IntelliJ\\bin\\idea64.exe -> C:\\Program Files\\JetBrains\\IntelliJ\\bin\\idea64.exe
    /Applications/PyCharm.app/Contents/MacOS/pycharm_helper -> (no match)
    /usr/bin/chrome -> (no match)
    """
    verify(
        "\n".join(
            f"{path} -> {find_jetbrains_ides([path]) or '(no match)'}"
            for path in parse_docstring()
        ),
        options=Options().inline(),
    )


def test_find_jetbrains_ides_returns_first_match() -> None:
    """
    /usr/bin/pycharm
    """
    paths = ["/usr/bin/chrome", "/usr/bin/pycharm", "/usr/bin/idea"]
    verify(find_jetbrains_ides(paths), options=Options().inline())


def test_find_jetbrains_ides_no_processes() -> None:
    """
    (no match)
    """
    verify(find_jetbrains_ides([]) or "(no match)", options=Options().inline())


def test_get_running_process_paths_falls_back_to_cmdline_on_access_denied() -> None:
    """
    /usr/bin/pycharm
    /usr/bin/pycharm
    /opt/idea/bin/idea.sh
    """
    readable_process = MagicMock()
    readable_process.exe.return_value = "/usr/bin/pycharm"
    readable_process.cmdline.return_value = ["/usr/bin/pycharm"]

    exe_denied_process = MagicMock()
    exe_denied_process.exe.side_effect = psutil.AccessDenied()
    exe_denied_process.cmdline.return_value = ["/opt/idea/bin/idea.sh"]

    fully_denied_process = MagicMock()
    fully_denied_process.exe.side_effect = psutil.NoSuchProcess(0)
    fully_denied_process.cmdline.side_effect = psutil.AccessDenied()

    with patch(
        "psutil.process_iter",
        return_value=[readable_process, exe_denied_process, fully_denied_process],
    ):
        paths = get_running_process_paths()

    verify("\n".join(paths), options=Options().inline())
