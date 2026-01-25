from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter
from approvaltests.reporters.generic_diff_reporter_config import (
    GenericDiffReporterConfig,
)


class ReportWithDiffMergeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/DiffMerge.app/Contents/MacOS/DiffMerge",
                extra_args=["--nosplash"],
            )
        )


class ReportWithBeyondCompareMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/Beyond Compare.app/Contents/MacOS/bcomp",
            )
        )


class ReportWithKaleidoscopeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/Kaleidoscope.app/Contents/MacOS/ksdiff",
            )
        )


class ReportWithKaleidoscope3Mac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/local/bin/ksdiff",
            )
        )


class ReportWithKdiff3Mac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/kdiff3.app/Contents/MacOS/kdiff3",
                extra_args=["-m"],
            )
        )


class ReportWithP4mergeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/p4merge.app/Contents/MacOS/p4merge",
            )
        )


class ReportWithTkDiffMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/TkDiff.app/Contents/MacOS/tkdiff",
            )
        )


class ReportWithVisualStudioCodeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code",
                extra_args=["-d"],
            )
        )


class ReportWithAraxisMergeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/Araxis Merge.app/Contents/Utilities/compare",
            )
        )


class ReportWithBeyondCompare3Windows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Beyond Compare 3/BCompare.exe",
            )
        )


class ReportWithBeyondCompare4Windows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Beyond Compare 4/BCompare.exe",
            )
        )


class ReportWithBeyondCompare5Windows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Beyond Compare 5/BCompare.exe",
            )
        )


class ReportWithTortoiseImageDiffWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}TortoiseSVN/bin/TortoiseIDiff.exe",
                extra_args=["/left:%s", "/right:%s"],
            )
        )


class ReportWithTortoiseTextDiffWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}TortoiseSVN/bin/TortoiseMerge.exe",
            )
        )


class ReportWithTortoiseGitImageDiffWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}TortoiseGIT/bin/TortoiseGitIDiff.exe",
                extra_args=["/left:%s", "/right:%s"],
            )
        )


class ReportWithTortoiseGitTextDiffWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}TortoiseGIT/bin/TortoiseGitMerge.exe",
            )
        )


class ReportWithWinMergeReporterWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}WinMerge/WinMergeU.exe",
            )
        )


class ReportWithAraxisMergeWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Araxis/Araxis Merge/Compare.exe",
            )
        )


class ReportWithCodeCompareWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Devart/Code Compare/CodeCompare.exe",
            )
        )


class ReportWithKdiff3Windows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}KDiff3/kdiff3.exe",
            )
        )


class ReportWithVisualStudioCodeWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Microsoft VS Code/Code.exe",
                extra_args=["-d"],
            )
        )


class ReportWithDiffMergeLinux(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/bin/diffmerge",
                extra_args=["--nosplash"],
            )
        )


class ReportWithMeldMergeLinux(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/bin/meld",
            )
        )


class ReportWithKdiff3Linux(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/bin/kdiff3",
                extra_args=["-m"],
            )
        )
