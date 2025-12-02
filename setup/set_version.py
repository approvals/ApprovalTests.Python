from pathlib import Path
import argparse
from packaging.version import Version

_VERSION_FILES = map(Path, [
    "version.py",
    "approvaltests/version.py",
])

def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("version", type=Version)
    args = argument_parser.parse_args()
    version_number = args.version

    print(f"Setting version to {version_number}")
    for version_file in _VERSION_FILES:
        version_file.write_text(f'version_number = "{version_number}"\n')


if __name__ == "__main__": main()
