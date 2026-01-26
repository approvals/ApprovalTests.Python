import csv
from pathlib import Path
from typing import List
import textwrap

_SCRIPT_DIR = Path(__file__).parent
_REPO_ROOT = _SCRIPT_DIR.parent.parent
assert _REPO_ROOT.joinpath(".gitattributes").exists()

def to_class_name(name: str, os_name: str) -> str:
    parts = name.split("_")
    camel = "".join(word.capitalize() for word in parts)
    return f"ReportWith{camel}{os_name}"


def parse_extra_args(arguments: str) -> List[str]:
    if not arguments:
        return []
    args = []
    for part in arguments.split():
        if part != "%s":
            args.append(part)
    return args


def normalize_path(path: str) -> str:
    return path.replace("\\", "/")


def generate_class(name: str, path: str, arguments: str, os_name: str) -> str:
    class_name = to_class_name(name, os_name)
    normalized_path = normalize_path(path)
    extra_args = parse_extra_args(arguments)

    extra_args_str = ", ".join(f'"{arg}"' for arg in extra_args)
        
    return textwrap.dedent(f"""\
        class {class_name}(GenericDiffReporter):
            def __init__(self) -> None:
                super().__init__(
                    config=GenericDiffReporterConfig(
                        name=self.__class__.__name__,
                        path="{normalized_path}",
                        extra_args=[{extra_args_str}],
                    )
                )
        """)


def generate_file_header() -> str:
    return textwrap.dedent("""\
        from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter
        from approvaltests.reporters.generic_diff_reporter_config import (
            GenericDiffReporterConfig,
        )

 
    """)


def main() -> None:
    csv_path = _REPO_ROOT / "internal_documentation" / "issues" / "reporters.csv"
    output_dir = _REPO_ROOT / "approvaltests" / "reporters"

    reader = csv.DictReader(csv_path.read_text().splitlines())
    rows = list(reader)

    output = generate_file_header()
    for row in rows:
        output += generate_class(
            name=row["name"],
            path=row["path"],
            arguments=row["arguments"],
            os_name=row["os"],
        )
        output += "\n\n"

    output_path = output_dir / "generated_reporters.py"
    output_path.write_text(output)

    print(f"Generated {len(rows)} reporter classes to {output_path}")


if __name__ == "__main__":
    main()
