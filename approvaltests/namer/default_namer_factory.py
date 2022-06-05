from contextlib import contextmanager
from typing import Optional, Any

from approvaltests.core.options import Options
from approvaltests.core.namer import Namer
from approvaltests.namer.stack_frame_namer import StackFrameNamer


def get_default_namer(extension: Optional[str] = None) -> Namer:
    return StackFrameNamer(extension)


class NamerFactory:
    @staticmethod
    def with_parameters(*args: Any) -> Options:
        from approvaltests.core.scenario_namer import ScenarioNamer
        namer = ScenarioNamer(get_default_namer(), *args)
        return Options().with_namer(namer)
