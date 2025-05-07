# -*- coding: utf-8 -*-

import json
import random
import unittest
from typing import Callable, Dict, Optional

import pytest
from typing_extensions import override

from approval_utilities.approvaltests.core.verifiable import Verifiable
from approval_utilities.approvaltests.core.verify_parameters import VerifyParameters
from approval_utilities.utilities.multiline_string_utils import remove_indentation_from
from approval_utilities.utils import get_adjacent_file, is_windows_os, print_grid
from approvaltests import List, Options, approvals, delete_approved_file
from approvaltests.approval_exception import ApprovalException
from approvaltests.approvals import (
    verify,
    verify_as_json,
    verify_binary,
    verify_exception,
    verify_file,
    verify_html,
    verify_xml,
)
from approvaltests.core.comparator import Comparator
from approvaltests.reporters.report_all_to_clipboard import (
    ReporterByCopyMoveCommandForEverythingToClipboard,
)
from approvaltests.reporters.report_with_beyond_compare import ReportWithPycharm
from approvaltests.reporters.reporter_that_automatically_approves import (
    ReporterThatAutomaticallyApproves,
)
from approvaltests.reporters.testing_reporter import ReporterForTesting
from approvaltests.storyboard import Storyboard, verify_storyboard


class GameOfLife:
    def __init__(self, board: Callable[[int, int], int]):
        self.board = board
        self.alive = "X"
        self.dead = "."

    def advance(self) -> "GameOfLife":
        old = self.board

        def my_next(x, y):
            count = (
                old(x + 1, y)
                + old(x + 1, y - 1)
                + old(x + 1, y + 1)
                + old(x - 1, y)
                + old(x - 1, y - 1)
                + old(x - 1, y + 1)
                + old(x, y + 1)
                + old(x, y - 1)
            )
            return count == 3 or (count == 2 and old(x, y))

        self.board = my_next
        return self

    @override
    def __str__(self):
        return print_grid(
            5, 5, lambda x, y: f"{self.alive} " if self.board(x, y) else f"{self.dead} "
        )

    def set_alive_cell(self, alive: str) -> str:
        self.alive = alive
        return self.alive

    def set_dead_cell(self, dead: str) -> str:
        self.dead = dead
        return self.dead


class VerifyTests(unittest.TestCase):
    @override
    def setUp(self) -> None:
        self.reporter = ReporterByCopyMoveCommandForEverythingToClipboard()

    def test_verify(self) -> None:
        verify("Hello World.", self.reporter)

    def test_verify_with_encoding(self) -> None:
        verify(
            "Høvdingens kjære squaw får litt pizza i Mexico by",
            self.reporter,
            encoding="utf-8",
        )

    def test_verify_with_encoding_error_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            verify(
                "Høvdingens kjære squaw får litt pizza i Mexico by",
                self.reporter,
                encoding="ascii",
            )

    def test_verify_with_errors_replacement_character(self) -> None:
        verify(
            "Falsches Üben von Xylophonmusik quält jeden größeren Zwerg",
            self.reporter,
            encoding="ascii",
            errors="replace",
        )

    def test_verify_with_newlines(self) -> None:
        verify(
            "I cannot live without approval.\n"
            "Your satisfaction is my demand.\n"
            "I must control what you think of me.\n"
            "I have to understand.\n",
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
            def __init__(self) -> None:
                self.stuff = 1
                self.json: Optional[Dict[str, int]] = None

        o = Bag()
        o.json = {"a": 0, "z": 26}
        verify_as_json(o)

    def test_verify_as_json_raises_type_error_for_non_renderable_types(self):
        with self.assertRaises(AttributeError):
            verify_as_json(Ellipsis, self.reporter)

    def test_verify_as_json_raises_value_error_for_non_renderable_values(self):
        circular_data: List[List] = []
        circular_data.append(circular_data)
        with self.assertRaises(ValueError):
            verify_as_json(circular_data, self.reporter)

    def test_json_in_json(self):
        dict = {"a": 1, "b": 2, "c": 3}
        verify_as_json(
            {"type": "dictionary", "value": json.dumps(dict)},
            deserialize_json_fields=True,
        )

    def test_json_in_dict_in_json(self):
        dict = {"a": 1, "b": 2, "c": 3}
        verify_as_json(
            {"type": "dictionary", "value": {"key": json.dumps(dict)}},
            deserialize_json_fields=True,
        )

    def test_verify_file(self) -> None:
        name = "exampleFile.txt"
        filename = get_adjacent_file(name)
        verify_file(filename, self.reporter)

    @pytest.mark.skipif(not is_windows_os(), reason="Doesn't work on unix")
    def test_verify_file_with_windows_1252_encoding(self):
        name = "exampleFileWindows1252.txt"
        filename = get_adjacent_file(name)
        verify_file(filename, self.reporter)

    def test_verify_file_with_actual_windows_1252_encoding(self) -> None:
        name = "exampleFile_Actual_Windows1252.txt"
        filename = get_adjacent_file(name)
        verify_file(filename, self.reporter)

    def test_verify_file_binary_file(self) -> None:
        name = "icon.png"
        filename = get_adjacent_file(name)
        verify_file(filename)

    def test_verify_bytes(self) -> None:
        # begin-snippet: verify_binary_image
        name = "icon.png"
        filename = get_adjacent_file(name)
        with open(filename, mode="rb") as f:
            verify_binary(f.read(), ".png")
        # end-snippet

    def test_verify_xml(self) -> None:
        xml = """<?xml version="1.0" encoding="UTF-8"?><orderHistory createdAt='2019-08-02T16:40:18.109470'><order date='2018-09-01T00:00:00+00:00' totalDollars='149.99'><product id='EVENT02'>Makeover</product></order><order date='2017-09-01T00:00:00+00:00' totalDollars='14.99'><product id='LIPSTICK01'>Cherry Bloom</product></order></orderHistory>"""
        verify_xml(xml)

    def test_verify_html(self) -> None:
        html = """<!DOCTYPE html><html><head> <title>Example</title> </head> <body> <p>This is an example of a simple HTML page with one paragraph.</p></body></html>"""
        verify_html(html)

    def test_newlines_at_end_of_files(self) -> None:
        verify(
            "There should be a blank line underneath this",
            options=Options().with_reporter(ReportWithPycharm()),
        )

    def test_verify_storyboard(self) -> None:
        with verify_storyboard() as b:
            game_of_life = GameOfLife(lambda x, y: 2 <= x <= 4 and y == 2)
            b.add_frame(game_of_life)
            b.add_frames(2, lambda _: game_of_life.advance())

    def test_storyboard(self) -> None:
        game_of_life = GameOfLife(lambda x, y: 2 <= x <= 4 and y == 2)
        verify(
            Storyboard()
            .add_frame(game_of_life)
            .add_frames(2, lambda _: game_of_life.advance())
        )

    def test_simple_storyboard(self) -> None:
        class AsciiWheel:
            def __init__(self) -> None:
                self.steps = ["-", "\\", "|", "/"]
                self.step = 0

            @override
            def __str__(self) -> str:
                return self.steps[self.step]

            def advance(self) -> None:
                self.step += 1
                self.step %= 4

        ascii_wheel = AsciiWheel()
        # begin-snippet: use_storyboard
        story = Storyboard()
        story.add_description("Spinning wheel")
        story.add_frame(ascii_wheel)
        ascii_wheel.advance()
        story.add_frame(ascii_wheel)
        verify(story)
        # end-snippet

    def test_storyboard_of_iterable(self) -> None:
        approvals.settings().allow_multiple_verify_calls_for_this_method()
        spinning_wheel = ["-", "\\", "|", "/"] * 3
        verify(Storyboard().iterate_frames(spinning_wheel, 5))

        spinning_wheel = ["-", "\\", "|", "/", "-"]
        verify(Storyboard().iterate_frames(spinning_wheel))

    def test_other_storyboard_machanisms(self) -> None:
        game_of_life = GameOfLife(lambda x, y: 1 <= x <= 3 and y == 2)

        story = Storyboard()
        story.add_description("Game of Life")
        story.add_frame(game_of_life)

        game_of_life = game_of_life.advance()
        story.add_frame(game_of_life, "Start game_of_life")

        game_of_life = game_of_life.advance()
        story.add_frame(game_of_life)

        story.add_description_with_data(
            "setting alive", game_of_life.set_alive_cell("*")
        )
        story.add_description_with_data("setting dead", game_of_life.set_dead_cell("_"))
        game_of_life = game_of_life.advance()
        story.add_frame(game_of_life)

        game_of_life = game_of_life.advance()
        story.add_frame(game_of_life)

        game_of_life = game_of_life.advance()
        story.add_frame(game_of_life)

        verify(story)

    def test_exist_file_extension(self):
        verify_file(get_adjacent_file("sample.xml"))

    def test_exist_file_with_modified_extension(self):
        verify_file(
            get_adjacent_file("sample.xml"),
            options=Options().for_file.with_extension(".json"),
        )

    def test_verify_converts_to_string(self):
        verify(1)

    def test_verify_automatic_approval(self):
        approvals.settings().allow_multiple_verify_calls_for_this_method()
        delete_approved_file()
        with pytest.raises(ApprovalException):
            verify(
                2,
                options=Options().with_reporter(
                    reporter=ReporterThatAutomaticallyApproves()
                ),
            )
        verify(2)

    def test_verify_custom_comparator_allows_all_inputs(self):
        class EverythingIsTrue(Comparator):
            @override
            def compare(self, received_path: str, approved_path: str) -> bool:
                return True

        verify(random.random(), options=Options().with_comparator(EverythingIsTrue()))

    # begin-snippet: verifiable_object_example
    def test_verifiable(self):
        class MarkdownParagraph(Verifiable):
            def __init__(self, title: str, text: str) -> None:
                self.title = title
                self.text = text

            @override
            def __str__(self) -> str:
                return remove_indentation_from(
                    f""" 
                # {self.title}
                {self.text}
                """
                )

            @override
            def get_verify_parameters(self, options: Options) -> VerifyParameters:
                return VerifyParameters(options.for_file.with_extension(".md"))

        verify(
            MarkdownParagraph("Paragraph Title", "This is where the paragraph text is.")
        )

    # end-snippet

    def test_verify_exception(self):
        def throw_exception():
            raise RuntimeError("some error")

        verify_exception(throw_exception)
