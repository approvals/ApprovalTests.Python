import argparse
import textwrap
from pathlib import Path

from packaging.version import Version

_VERSION_FILES = map(
    Path,
    [
        "version.py",
        "approvaltests/version.py",
    ],
)


def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("version", type=Version)
    args = argument_parser.parse_args()
    version_number = args.version

    print(f"Setting version to {version_number}")
    for version_file in _VERSION_FILES:
        version_file.write_text(
            textwrap.dedent(f"""\
                # Do not edit manually — use setup/set_version.py to change the version
                version_number = "{version_number}"
            """)
        )


if __name__ == "__main__":
    main()
