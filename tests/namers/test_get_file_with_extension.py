import os

from approvaltests import verify_all
from approvaltests.asserts import FilePathNamer
from approvaltests.namer.cli_namer import CliNamer
from approvaltests.namer.inline_comparator import InlineComparator
from approvaltests.namer.stack_frame_namer import StackFrameNamer


def _names(namer: object) -> list[str]:
    return [
        os.path.basename(namer.get_approved_file(".json")),  # type: ignore[attr-defined]
        os.path.basename(namer.get_received_file(".json")),  # type: ignore[attr-defined]
    ]


def test_stack_frame_namer() -> None:
    verify_all("StackFrameNamer", _names(StackFrameNamer()))


def test_cli_namer() -> None:
    verify_all("CliNamer", _names(CliNamer("my_test")))


def test_file_path_namer() -> None:
    namer = FilePathNamer("fixed/path.approved.txt")
    verify_all(
        "FilePathNamer",
        [namer.get_approved_file(".json"), os.path.basename(namer.get_received_file(".json"))],
    )


def test_inline_comparator() -> None:
    namer = InlineComparator()
    received = namer.get_received_file(".json")
    verify_all("InlineComparator", [received.endswith(".received.json")])
