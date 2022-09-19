import os
from typing import Any

from approvaltests.core.options import Options
from approvaltests.namer.default_name import get_default_namer


def is_ci():
    possible = [
        "CI",
        "CONTINUOUS_INTEGRATION",
        "GITHUB_ACTIONS",
        "GO_SERVER_URL",
        "JENKINS_URL",
        "TEAMCITY_VERSION",
        "TF_BUILD",
    ]
    return any(os.environ.get(possibile_ci) for possibile_ci in possible)


class NamerFactory:
    @staticmethod
    def with_parameters(*args: Any) -> Options:
        from approvaltests.core.scenario_namer import ScenarioNamer

        namer = ScenarioNamer(get_default_namer(), *args)
        return Options().with_namer(namer)

    @staticmethod
    def as_ci_specific_test() -> Options:
        if is_ci():
            return NamerFactory.with_parameters("ci")
        else:
            return Options()
