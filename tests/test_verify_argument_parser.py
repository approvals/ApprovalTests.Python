import argparse
import os

from approvaltests import verify_argument_parser
from tests.find_stale_approved_files import create_argument_parser


def test_argument_parser() -> None:
    parser = argparse.ArgumentParser(
        prog="my_program.py",
        description="My Description",
    )
    parser.add_argument("1st_argument", help="1st argument help text")
    parser.add_argument("--optional_argument", help="An Optional Argument help text")
    parser.add_argument("long_argument", help=f"{'Very' * 100} Long message")
    verify_argument_parser(parser)
