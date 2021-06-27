# -*- coding: utf-8 -*-

import unittest

from approvaltests import Options, verify_sequence
from approvaltests.approval_exception import ApprovalException
from approvaltests.approvals import verify, verify_as_json, verify_file, verify_xml
from approvaltests.reporters.report_all_to_clipboard import ReporterByCopyMoveCommandForEverythingToClipboard
from approvaltests.reporters.report_with_beyond_compare import ReportWithPycharm
from approvaltests.reporters.testing_reporter import ReporterForTesting
from approvaltests.utils import get_adjacent_file


def print_grid(width, height, cell_print_func):
    result = ""
    for y  in range(0,height):
        for x in range(0,width):
            result += cell_print_func(x,y)
        result += "\n"
    return result

class GameOfLife:
    def __init__(self, board):
        self.board = board

    def advance(self) -> "GameOfLife":
        old = self.board
        def my_next(x, y):
            count = (
                old(x + 1, y) +
                old(x + 1, y - 1) +
                old(x + 1, y + 1) +
                old(x - 1, y) +
                old(x - 1, y - 1) +
                old(x - 1, y + 1) +
                old(x,     y + 1) +
                old(x,     y - 1)
            )
            return count == 3 or (count == 2 and old(x, y))
        self.board = my_next
        return self

    def __str__(self):
        return print_grid(5, 5, lambda x, y : "X " if  self.board(x, y) else ". ")

class VerifyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.reporter = ReporterByCopyMoveCommandForEverythingToClipboard()

    def test_verify(self) -> None:
        verify("Hello World.", self.reporter)

    def test_verify_with_encoding(self) -> None:
        verify(
            u"Høvdingens kjære squaw får litt pizza i Mexico by",
            self.reporter,
            encoding="utf-8",
        )

    def test_verify_with_encoding_error_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            verify(
                u"Høvdingens kjære squaw får litt pizza i Mexico by",
                self.reporter,
                encoding="ascii",
            )

    def test_verify_with_errors_replacement_character(self) -> None:
        verify(
            u"Falsches Üben von Xylophonmusik quält jeden größeren Zwerg",
            self.reporter,
            encoding="ascii",
            errors="replace",
        )

    def test_verify_with_newlines(self) -> None:
        verify(
            u"I cannot live without approval.\n"
            u"Your satisfaction is my demand.\n"
            u"I must control what you think of me.\n"
            u"I have to understand.\n",
            reporter=self.reporter,
            encoding="utf-8",
            newline="\r\n",
        )

    def test_verify_fail(self) -> None:
        reporter = ReporterForTesting()
        try:
            verify("Hello World.", reporter)
            self.assertFalse(True, "expected exception")
        except ApprovalException as e:
            self.assertTrue("Approval Mismatch", e.value)

    def test_verify_as_json(self) -> None:
        class Bag(object):
            def __init__(self):
                self.stuff = 1
                self.json = None

        o = Bag()
        o.json = {"a": 0, "z": 26}
        verify_as_json(o, self.reporter)

    def test_verify_file(self) -> None:
        name = "exampleFile.txt"
        filename = get_adjacent_file(name)
        verify_file(filename, self.reporter)

    def hidden_test_verify_file_with_windows_1252_encoding(self):
        name = "exampleFileWindows1252.txt"
        filename = get_adjacent_file(name)
        verify_file(filename, self.reporter)

    def test_verify_file_with_actual_windows_1252_encoding(self) -> None:
        name = "exampleFile_Actual_Windows1252.txt"
        filename = get_adjacent_file(name)
        verify_file(filename, self.reporter)

    def test_verify_xml(self) -> None:
        xml = """<?xml version="1.0" encoding="UTF-8"?><orderHistory createdAt='2019-08-02T16:40:18.109470'><order date='2018-09-01T00:00:00+00:00' totalDollars='149.99'><product id='EVENT02'>Makeover</product></order><order date='2017-09-01T00:00:00+00:00' totalDollars='14.99'><product id='LIPSTICK01'>Cherry Bloom</product></order></orderHistory>"""
        verify_xml(xml)

    def test_newlines_at_end_of_files(self) -> None:
        verify("There should be a blank line underneath this", options=Options().with_reporter(ReportWithPycharm()))

    def test_sequence(self) -> None:
        gameOfLife = GameOfLife(lambda x, y: 2 <= x <= 4 and y == 2)
        verify_sequence(gameOfLife, 2, lambda _ :  gameOfLife.advance()  )

        # def as_iterable():
        #     yield gameOfLife
        #     while True:
        #         yield gameOfLife.advance()
        # verify_sequence2(as_iterable(), 3)