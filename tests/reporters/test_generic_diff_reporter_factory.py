from approvaltests.reporters import GenericDiffReporterFactory


def test_fallback_reporter():
    factory = GenericDiffReporterFactory()
    fallback_reporter = factory.get("PythonNative")
    assert fallback_reporter.is_working()
