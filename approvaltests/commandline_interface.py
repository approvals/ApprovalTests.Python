from pathlib import Path

from approvaltests import verify
from build.lib.approvaltests.commandline_interface import parse_arguments
from namer.cli_namer import CliNamer


# simplify the following lines of code from commandline_interface.py

# 1.  Modify so our future-selves would recognize it
# >>> 2.  Make a test
# 3.  Refactor parse_arguments to be part of a class (suggested by Jay)

# NEw code...
# received = args.received or stdin.read()
# Old code...
# received = args.received
# if args.received is None:
#    received = stdin.read()
# return (args.id, received)



def verify_using_commandline_arguments():
    test_id, received = parse_arguments()
    verify_with_id(received, test_id)


def verify_with_id(received, test_id):
    verify(received, namer=CliNamer(test_id=test_id))
    print(f"Test Passed: {test_id}")


if __name__ == "__main__":
    verify_using_commandline_arguments()


def list_approved_files_in_test_directory(test_dir: Path):
    return [file.name for file in test_dir.iterdir() if file.name.endswith(".approved.txt")]
