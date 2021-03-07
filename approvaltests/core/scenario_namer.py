from typing import Optional

from approvaltests.core.namer import StackFrameNamer


class ScenarioNamer:
    """
    For use with parameterized tests.

    Use this namer when the same test case needs to verify more than one value, and produce more than one file.
    """

    def __init__(self, base_namer: StackFrameNamer, scenario_name: int) -> None:
        self.base_namer = base_namer
        self.scenario_name = scenario_name

    def get_basename(self) -> str:
        basename = self.base_namer.get_basename()
        return basename + "." + str(self.scenario_name)

    def get_approved_filename(self, base: Optional[str] = None) -> str:
        return self.base_namer.get_approved_filename(base)

    def get_received_filename(self, base: Optional[str] = None) -> str:
        return self.base_namer.get_received_filename(base)
