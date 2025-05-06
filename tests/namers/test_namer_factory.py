from typing import Optional

from approvaltests import verify
from approvaltests.namer import NamerFactory, is_ci


def test_CI_specific() -> None:
    result = "JACK-0-LANTERN!!!"
    verify(
        result,
        options=NamerFactory.as_ci_specific_test(),  # .with_reporter(FileCaptureReporter()),
    )


def assert_team_city(value: Optional[str], expected: bool) -> None:
    def loader(key):
        if key == "TEAMCITY_VERSION":
            return value
        return None

    assert expected == is_ci(loader)


def test_team_city() -> None:
    assert_team_city(None, False)
    assert_team_city("LOCAL", False)
    assert_team_city("1.1", True)
