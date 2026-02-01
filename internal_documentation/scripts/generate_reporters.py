import csv
import textwrap
from pathlib import Path
from typing import Dict, List

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
        import platform

        from typing_extensions import override

        from approvaltests.reporters.first_working_reporter import FirstWorkingReporter
        from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter
        from approvaltests.reporters.generic_diff_reporter_config import (
            GenericDiffReporterConfig,
        )


    """)


def get_platform_name(os_name: str) -> str:
    return {"Mac": "Darwin", "Windows": "Windows", "Linux": "Linux"}[os_name]


def generate_per_os_reporter(os_name: str, class_names: List[str]) -> str:
    reporter_instances = ", ".join(f"{name}()" for name in class_names)
    platform_name = get_platform_name(os_name)
    return textwrap.dedent(f"""\
        class ReportWithDiffToolOn{os_name}(FirstWorkingReporter):
            def __init__(self) -> None:
                super().__init__({reporter_instances})

            @override
            def report(self, received_path: str, approved_path: str) -> bool:
                if platform.system() != "{platform_name}":
                    return False
                return super().report(received_path, approved_path)
        """)


def main() -> None:
    csv_path = _REPO_ROOT / "internal_documentation" / "issues" / "reporters.csv"
    output_dir = _REPO_ROOT / "approvaltests" / "reporters"

    reader = csv.DictReader(csv_path.read_text().splitlines())
    rows = list(reader)

    os_to_classes: Dict[str, List[str]] = {}

    output = generate_file_header()
    for row in rows:
        class_name = to_class_name(row["name"], row["os"])
        os_name = row["os"]
        if os_name not in os_to_classes:
            os_to_classes[os_name] = []
        os_to_classes[os_name].append(class_name)

        output += generate_class(
            name=row["name"],
            path=row["path"],
            arguments=row["arguments"],
            os_name=os_name,
        )
        output += "\n\n"

    for os_name, class_names in os_to_classes.items():
        output += generate_per_os_reporter(os_name, class_names)
        output += "\n\n"

    output_path = output_dir / "generated_reporters.py"
    output_path.write_text(output)

    print(f"Generated {len(rows)} reporter classes to {output_path}")


if __name__ == "__main__":
    main()
