from approvaltests.reporters import GenericDiffReporterFactory, DiffReporter, PythonNativeReporter


class FakeFactory:
    def get_all_reporters(self):
        return []


def test_fallback_reporter():
    empty_reporter_factory = FakeFactory()
    reporter = DiffReporter(empty_reporter_factory)
    # Testing implementation detail, not great but good enough for now
    assert isinstance(reporter.reporters[-1], PythonNativeReporter)
