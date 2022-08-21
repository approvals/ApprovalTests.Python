from typing import Any

from approvaltests.core.options import Options
from approvaltests.namer.default_name import get_default_namer


class NamerFactory:
    @staticmethod
    def with_parameters(*args: Any) -> Options:
        from approvaltests.core.scenario_namer import ScenarioNamer

        namer = ScenarioNamer(get_default_namer(), *args)
        return Options().with_namer(namer)
