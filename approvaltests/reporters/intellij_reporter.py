from typing_extensions import override

from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter
from approvaltests.reporters.generic_diff_reporter_config import (
    GenericDiffReporterConfig,
)

JETBRAINS_KEYWORDS = [
    "idea",
    "pycharm",
    "webstorm",
    "phpstorm",
    "goland",
    "rider",
    "clion",
    "rubymine",
    "appcode",
    "datagrip",
]


def _is_main_executable(path: str, keyword: str) -> bool:
    normalized = path.lower().replace("\\", "/")
    return normalized.endswith(f"macos/{keyword}") or f"bin/{keyword}" in normalized


def find_jetbrains_ides(paths: list[str]) -> str:
    return next(
        (
            path
            for path in paths
            for keyword in JETBRAINS_KEYWORDS
            if keyword in path.lower() and _is_main_executable(path, keyword)
        ),
        "",
    )


def get_running_process_paths() -> list[str]:
    """
    Defers importing psutil until actual usage, since it is an optional dependency.
    """
    import psutil

    paths = []
    for process in psutil.process_iter():
        try:
            exe = process.exe()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            exe = None
        if exe:
            paths.append(exe)

        try:
            cmdline = process.cmdline()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            cmdline = []
        paths.extend(cmdline)
    return paths


class ReportWithIntellijTools(GenericDiffReporter):

    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="",
                extra_args=["diff", "%s", "%s"],
            )
        )
        self.path = ""

    @override
    def is_working(self) -> bool:
        self.path = find_jetbrains_ides(get_running_process_paths())
        return super().is_working()


