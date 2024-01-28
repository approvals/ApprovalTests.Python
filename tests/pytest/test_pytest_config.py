from approvaltests import get_default_namer



def test_different_name():
    assert get_default_namer().get_approved_filename().endswith("test_pytest_config.test_different_name.approved.txt")

def different_name_check():
    assert get_default_namer().get_approved_filename().endswith("test_pytest_config.different_name_check.approved.txt")

