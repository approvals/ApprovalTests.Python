from approvaltests import verify
from approvaltests.namer import NamerFactory
from approvaltests.reporters.file_capture_reporter import FileCaptureReporter


def test_CI_specific() -> None:
    result = "JACK-0-LANTERN!!!"
    verify(result, options=NamerFactory.as_ci_specific_test().with_reporter(FileCaptureReporter()))