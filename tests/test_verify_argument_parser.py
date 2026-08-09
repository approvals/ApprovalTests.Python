import argparse
import sys

from approvaltests import verify_argument_parser
from approvaltests.namer.default_namer_factory import NamerFactory
from approvaltests.core.options import Options

def test_argument_parser() -> None:
    parser = argparse.ArgumentParser(
        prog="my_program.py",
        description="My Description",
    )
    parser.add_argument("1st_argument", help="1st argument help text")
    parser.add_argument("--optional_argument", help="An Optional Argument help text")
    parser.add_argument("-c", "--count", type=int, help="Number of items to process")
    parser.add_argument("long_argument", help=f"{'Very' * 100} Long message")
    help_includes_duplicate_metavars = sys.version_info < (3, 13)
    options = NamerFactory.with_parameters("help_includes_duplicate_metavars")
    if help_includes_duplicate_metavars:
        pass
    else:
        options = None
    verify_argument_parser(
        parser,
        options=options,
    )


def test_argument_parser_scrubs() -> None:
    """
    <SCRUBBED>
    """
    parser = argparse.ArgumentParser()
    verify_argument_parser(
        parser,
        options=Options().with_scrubber(lambda s: "<SCRUBBED>").inline(),
    )
