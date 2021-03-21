from approvaltests import get_default_reporter, approvals


class Options:
    def get_reporter(self):
        return get_default_reporter()


def test_empty_options_has_default_reporter():
    approvals.set_default_reporter(None)
    options = Options()
    assert options.get_reporter() == get_default_reporter()

