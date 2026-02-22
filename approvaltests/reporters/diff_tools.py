import platform

from typing_extensions import override

from approvaltests.reporters.first_working_reporter import FirstWorkingReporter
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
                extra_args=["--nosplash", "%s", "%s"],
            )
        )


class ReportWithFileMergeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/Xcode.app/Contents/Applications/FileMerge.app/Contents/MacOS/FileMerge",
                extra_args=["--nosplash", "-left", "%s", "-right", "%s"],
            )
        )


class ReportWithBeyondCompareMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/Beyond Compare.app/Contents/MacOS/bcomp",
                extra_args=[],
            )
        )


class ReportWithKaleidoscopeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/Kaleidoscope.app/Contents/MacOS/ksdiff",
                extra_args=[],
            )
        )


class ReportWithKaleidoscope3Mac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/local/bin/ksdiff",
                extra_args=[],
            )
        )


class ReportWithKdiff3Mac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/kdiff3.app/Contents/MacOS/kdiff3",
                extra_args=["%s", "%s", "-m"],
            )
        )


class ReportWithP4mergeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/p4merge.app/Contents/MacOS/p4merge",
                extra_args=[],
            )
        )


class ReportWithTkDiffMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/TkDiff.app/Contents/MacOS/tkdiff",
                extra_args=[],
            )
        )


class ReportWithVisualStudioCodeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code",
                extra_args=["-d", "%s", "%s"],
            )
        )


class ReportWithAraxisMergeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/Araxis Merge.app/Contents/Utilities/compare",
                extra_args=[],
            )
        )


class ReportWithBeyondCompare3Windows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Beyond Compare 3/BCompare.exe",
                extra_args=[],
            )
        )


class ReportWithBeyondCompare4Windows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Beyond Compare 4/BCompare.exe",
                extra_args=[],
            )
        )


class ReportWithBeyondCompare5Windows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Beyond Compare 5/BCompare.exe",
                extra_args=[],
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
                extra_args=[],
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
                extra_args=[],
            )
        )


class ReportWithWinMergeReporterWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}WinMerge/WinMergeU.exe",
                extra_args=[],
            )
        )


class ReportWithAraxisMergeWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Araxis/Araxis Merge/Compare.exe",
                extra_args=[],
            )
        )


class ReportWithCodeCompareWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Devart/Code Compare/CodeCompare.exe",
                extra_args=[],
            )
        )


class ReportWithKdiff3Windows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}KDiff3/kdiff3.exe",
                extra_args=[],
            )
        )


class ReportWithVisualStudioCodeWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Microsoft VS Code/Code.exe",
                extra_args=["-d", "%s", "%s"],
            )
        )


class ReportWithDiffMergeLinux(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/bin/diffmerge",
                extra_args=["--nosplash", "%s", "%s"],
            )
        )


class ReportWithMeldMergeLinux(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/bin/meld",
                extra_args=["%s", "%s"],
            )
        )


class ReportWithKdiff3Linux(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/bin/kdiff3",
                extra_args=["%s", "%s", "-m"],
            )
        )


class ReportWithDiffCommandLineLinux(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/bin/diff",
                extra_args=["-u", "%s", "%s"],
            )
        )


class ReportWithDiffCommandLineMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/bin/diff",
                extra_args=["-u", "%s", "%s"],
            )
        )


class ReportWithSublimeMergeMac(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/Applications/Sublime Merge.app/Contents/SharedSupport/bin/smerge",
                extra_args=["mergetool", "%s", "%s"],
            )
        )


class ReportWithSublimeMergeWindows(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="{ProgramFiles}Sublime Merge/smerge.exe",
                extra_args=["mergetool", "%s", "%s"],
            )
        )


class ReportWithSublimeMergeLinux(GenericDiffReporter):
    def __init__(self) -> None:
        super().__init__(
            config=GenericDiffReporterConfig(
                name=self.__class__.__name__,
                path="/usr/bin/smerge",
                extra_args=["mergetool", "%s", "%s"],
            )
        )


class ReportWithDiffToolOnMac(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithDiffMergeMac(),
            ReportWithFileMergeMac(),
            ReportWithBeyondCompareMac(),
            ReportWithKaleidoscopeMac(),
            ReportWithKaleidoscope3Mac(),
            ReportWithKdiff3Mac(),
            ReportWithP4mergeMac(),
            ReportWithTkDiffMac(),
            ReportWithVisualStudioCodeMac(),
            ReportWithAraxisMergeMac(),
            ReportWithDiffCommandLineMac(),
            ReportWithSublimeMergeMac(),
        )

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        if platform.system() != "Darwin":
            return False
        return super().report(received_path, approved_path)


class ReportWithDiffToolOnWindows(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithBeyondCompare3Windows(),
            ReportWithBeyondCompare4Windows(),
            ReportWithBeyondCompare5Windows(),
            ReportWithTortoiseImageDiffWindows(),
            ReportWithTortoiseTextDiffWindows(),
            ReportWithTortoiseGitImageDiffWindows(),
            ReportWithTortoiseGitTextDiffWindows(),
            ReportWithWinMergeReporterWindows(),
            ReportWithAraxisMergeWindows(),
            ReportWithCodeCompareWindows(),
            ReportWithKdiff3Windows(),
            ReportWithVisualStudioCodeWindows(),
            ReportWithSublimeMergeWindows(),
        )

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        if platform.system() != "Windows":
            return False
        return super().report(received_path, approved_path)


class ReportWithDiffToolOnLinux(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithDiffMergeLinux(),
            ReportWithMeldMergeLinux(),
            ReportWithKdiff3Linux(),
            ReportWithDiffCommandLineLinux(),
            ReportWithSublimeMergeLinux(),
        )

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        if platform.system() != "Linux":
            return False
        return super().report(received_path, approved_path)


class ReportWithDiffMerge(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithDiffMergeMac(),
            ReportWithDiffMergeLinux(),
        )


class ReportWithBeyondCompare(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithBeyondCompareMac(),
            ReportWithBeyondCompare3Windows(),
            ReportWithBeyondCompare4Windows(),
            ReportWithBeyondCompare5Windows(),
        )


class ReportWithKaleidoscope(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithKaleidoscopeMac(),
            ReportWithKaleidoscope3Mac(),
        )


class ReportWithKdiff3(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithKdiff3Mac(),
            ReportWithKdiff3Windows(),
            ReportWithKdiff3Linux(),
        )


class ReportWithVisualStudioCode(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithVisualStudioCodeMac(),
            ReportWithVisualStudioCodeWindows(),
        )


class ReportWithAraxisMerge(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithAraxisMergeMac(),
            ReportWithAraxisMergeWindows(),
        )


class ReportWithTortoise(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithTortoiseImageDiffWindows(),
            ReportWithTortoiseTextDiffWindows(),
        )


class ReportWithTortoiseGit(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithTortoiseGitImageDiffWindows(),
            ReportWithTortoiseGitTextDiffWindows(),
        )


class ReportWithDiffCommandLine(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithDiffCommandLineLinux(),
            ReportWithDiffCommandLineMac(),
        )


class ReportWithSublimeMerge(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(
            ReportWithSublimeMergeMac(),
            ReportWithSublimeMergeWindows(),
            ReportWithSublimeMergeLinux(),
        )
