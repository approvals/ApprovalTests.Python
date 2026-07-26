import argparse
from sys import stdin

from approvaltests import verify

# pylint: disable = no-name-in-module
from approvaltests.namer.cli_namer import CliNamer


def _get_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="verify")
    parser.add_argument(
        "--test-id", "-t", dest="id", required=True, type=str, help="test id"
    )
    parser.add_argument("--received", "-r", type=str, required=False, help="received")
    return parser


def parse_arguments() -> tuple[str, str]:
    parser = _get_argument_parser()
    args = parser.parse_args()
    received = args.received
    if args.received is None:
        received = stdin.read()
    return (args.id, received)


def verify_using_commandline_arguments() -> None:
    test_id, received = parse_arguments()
    verify_with_id(received, test_id)


def verify_with_id(received: str, test_id: str) -> None:
    verify(received, namer=CliNamer(test_id=test_id))
    print(f"Test Passed: {test_id}")


if __name__ == "__main__":
    verify_using_commandline_arguments()
