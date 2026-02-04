import csv
import textwrap
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

_SCRIPT_DIR = Path(__file__).parent
_REPO_ROOT = _SCRIPT_DIR.parent.parent
assert _REPO_ROOT.joinpath(".gitattributes").exists()


@dataclass(frozen=True)
class ReporterDefinition:
    name: str
    path: str
    arguments: str
    file_types: str
    os: str
    group_name: str

    @property
    def class_name(self) -> str:
        parts = self.name.split("_")
        camel = "".join(word.capitalize() for word in parts)
        return f"ReportWith{camel}{self.os}"


def parse_extra_args(arguments: str) -> List[str]:
    return [part for part in arguments.split() if part != "%s"]


def normalize_path(path: str) -> str:
    return path.replace("\\", "/")


def generate_class(reporter_definition: ReporterDefinition) -> str:
    class_name = reporter_definition.class_name
    normalized_path = normalize_path(reporter_definition.path)
    extra_args = parse_extra_args(reporter_definition.arguments)

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
    reporter_instances = ",\n                    ".join(
        f"{name}()" for name in class_names
    )
    platform_name = get_platform_name(os_name)
    return textwrap.dedent(f"""\
        class ReportWithDiffToolOn{os_name}(FirstWorkingReporter):
            def __init__(self) -> None:
                super().__init__(
                    {reporter_instances},
                )

            @override
            def report(self, received_path: str, approved_path: str) -> bool:
                if platform.system() != "{platform_name}":
                    return False
                return super().report(received_path, approved_path)
        """)


def main() -> None:
    csv_path = _REPO_ROOT / "internal_documentation" / "issues" / "reporters.csv"

    reader = csv.DictReader(csv_path.read_text().splitlines())
    rows = [ReporterDefinition(**row) for row in reader]

    os_to_classes: Dict[str, List[str]] = defaultdict(list)
    for row in rows:
        os_to_classes[row.os].append(row.class_name)

    output = generate_file_header()
    output += "\n\n".join(map(generate_class, rows)) + "\n\n"

    output += "\n\n".join(
        map(
            lambda item: generate_per_os_reporter(*item),
            os_to_classes.items(),
        )
    )

    output_path = _REPO_ROOT / "approvaltests" / "reporters" / "generated_reporters.py"
    output_path.write_text(output)

    print(f"Generated {len(rows)} reporter classes to {output_path}")


if __name__ == "__main__":
    main()
