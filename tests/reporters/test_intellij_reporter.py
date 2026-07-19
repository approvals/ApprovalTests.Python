from approvaltests import Options, verify
from approvaltests.inline.parse_docstring import parse_docstring
from approvaltests.reporters.intellij_reporter import find_jetbrains_ides


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
