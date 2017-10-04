from approvaltests import get_default_namer, verify_with_namer, write_to_temporary_file, get_reporter


def assert_against_file(actual, file_path, reporter=None):
    namer = get_default_namer()
    namer.get_approved_filename = lambda self,_=None: file_path
    verify_with_namer(actual, namer, reporter)


def assert_equal_with_reporter(expected, actual, reporter=None):
    if actual == expected:
        return

    name = get_default_namer().get_file_name()
    expected_file = write_to_temporary_file(expected, name + '.expected.')
    actual_file = write_to_temporary_file(actual, name + '.actual.')
    get_reporter(reporter).report(actual_file, expected_file)
    raise AssertionError('expected != actual\n  actual: "{}"\nexpected: "{}"'.format(actual, expected))