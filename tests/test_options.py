from approvaltests import get_default_reporter, approvals, verify, ReporterForTesting
from approvaltests.core.options import Options


def test_empty_options_has_default_reporter():
    approvals.set_default_reporter(None)
    options = Options()
    assert options.reporter == get_default_reporter()


def test_with_reporter():
    testr = ReporterForTesting()
    options = Options().with_reporter(testr)
    try:
        verify("Data2", options=options)
    except:
        pass

    assert testr.called


def test_setting_reporter():
    testr = ReporterForTesting()
    options = Options().with_reporter(testr)
    assert options.reporter == testr
