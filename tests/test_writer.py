import os
from pathlib import Path
from random import randint

from approvaltests.string_writer import StringWriter


def test_writes_file(tmp_path: Path) -> None:
    contents = "foo" + str(randint(0, 100)) + "\n"
    sw = StringWriter(contents)
    filename = os.path.join(str(tmp_path), "stuff.txt")
    sw.write_received_file(filename)

    with open(filename, "r") as received:
        assert contents == received.read()


def test_writes_file_to_missing_directory(tmp_path: Path) -> None:
    contents = "foo\n"
    sw = StringWriter(contents)
    filename = os.path.join(str(tmp_path), "non_existent_folder", "./stuff.txt")
    sw.write_received_file(filename)

    with open(filename, "r") as received:
        assert contents == received.read()


def test_new_lines_with_empty_string() -> None:
    sw = StringWriter("")
    sw2 = StringWriter(None)
    assert sw.contents == sw2.contents
