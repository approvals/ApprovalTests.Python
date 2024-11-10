import argparse
import os

from approvaltests import verify_argument_parser
from tests.find_stale_approved_files import create_argument_parser
from approvaltests.core.options import Options


def test_argument_parser():
    parser = argparse.ArgumentParser(
        prog="my_program.py",
        description="My Description",
    )
    parser.add_argument("1st_argument", help="1st argument help text")
    parser.add_argument("--optional_argument", help="An Optional Argument help text")
    parser.add_argument("long_argument", help=f"{'Very' * 100} Long message")

    scrubber = lambda t: t.replace("options:", "<optional header>:").replace(
        "optional arguments:", "<optional header>:"
    )
    verify_argument_parser(parser, options=Options().with_scrubber(scrubber))
