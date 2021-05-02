from approvaltests import get_default_reporter, approvals, verify, ReporterForTesting
from approvaltests.core.options import Options

def test_every_function_in_approvals_with_verify_has_an_options():
    # get all methods in Approvals
    for function_name, obj in approvals.__dict__.items():
        if 'verify' not in function_name:
            continue
        if not callable(obj):
            continue
        import inspect
        argspec = inspect.getfullargspec(obj)
        print(argspec)
        assert "options" in argspec.kwonlyargs
        #print(function_name, obj)
    assert 0
# filter for verify
#check has an options paramater


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
