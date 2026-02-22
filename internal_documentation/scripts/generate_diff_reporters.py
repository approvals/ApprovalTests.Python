import csv
import subprocess
import textwrap
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

_SCRIPT_DIR = Path(__file__).parent
_REPO_ROOT = _SCRIPT_DIR.parent.parent
assert _REPO_ROOT.joinpath(".gitattributes").exists()

_DIFF_TOOLS_DIR = _REPO_ROOT / ".ignore" / "DiffTools"
_DIFF_TOOLS_REPO_URL = "https://github.com/approvals/DiffTools"


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
    return arguments.split() if arguments else []


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


def screaming_snake_to_pascal(name: str) -> str:
    return "".join(word.capitalize() for word in name.split("_"))


def generate_group_reporter(group_name: str, class_names: List[str]) -> str:
    reporter_instances = ",\n                    ".join(
        f"{name}()" for name in class_names
    )
    pascal_name = screaming_snake_to_pascal(group_name)
    return textwrap.dedent(f"""\
        class ReportWith{pascal_name}(FirstWorkingReporter):
            def __init__(self) -> None:
                super().__init__(
                    {reporter_instances},
                )
        """)


def clone_and_update_diff_tools() -> None:
    if not _DIFF_TOOLS_DIR.exists():
        subprocess.run(
            ["git", "clone", _DIFF_TOOLS_REPO_URL, _DIFF_TOOLS_DIR.as_posix()],
            check=True,
        )
        return

    if not _DIFF_TOOLS_DIR.joinpath(".git").exists():
        raise RuntimeError(f"{_DIFF_TOOLS_DIR} exists but is not a git repository")

    subprocess.run(
        ["git", "-C", _DIFF_TOOLS_DIR.as_posix(), "pull", "--ff-only"],
        check=True,
    )


def main() -> None:
    clone_and_update_diff_tools()
    csv_path = _DIFF_TOOLS_DIR / "diff_reporters.csv"

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

    group_to_classes: Dict[str, List[str]] = defaultdict(list)
    for row in rows:
        if row.group_name:
            group_to_classes[row.group_name].append(row.class_name)

    output += "\n\n"
    output += "\n\n".join(
        generate_group_reporter(name, classes)
        for name, classes in group_to_classes.items()
    )

    output_path = _REPO_ROOT / "approvaltests/reporters/diff_tools.py"
    output_path.write_text(output)

    print(f"Generated {len(rows)} reporter classes to {output_path}")


if __name__ == "__main__":
    main()
