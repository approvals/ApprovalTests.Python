from typing import Any

from typing_extensions import override

from approvaltests.core.namer import Namer
from approvaltests.namer.namer_base import NamerBase


class ScenarioNamer(Namer):
    """
    For use with parameterized tests.

    Use this namer when the same test case needs to verify more than one value, and produce more than one file.
    """

    def __init__(self, base_namer: NamerBase, *scenario_names: Any) -> None:
        self.base_namer = base_namer
        self.scenario_names = scenario_names

    def get_basename(self) -> str:
        basename = self.base_namer.get_basename()
        scenarios = ".".join(map(str, self.scenario_names))
        return f"{basename}.{scenarios}"

    @override
    def get_approved_filename(self) -> str:
        return self.get_basename() + Namer.APPROVED + self.base_namer.extension_with_dot

    @override
    def get_received_filename(self) -> str:
        return self.get_basename() + Namer.RECEIVED + self.base_namer.extension_with_dot

    def set_extension(self, extension: str) -> None:
        self.base_namer.set_extension(extension)
