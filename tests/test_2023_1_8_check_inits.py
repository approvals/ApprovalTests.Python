from pathlib import Path


def is_dunder(directory_name):
    return "__" in directory_name


def assert_directories_have_inits(param):
    if not is_dunder(f"{param}"):
        if not Path(f"{param}/__init__.py").exists():
            assert False, f"__init__.py is missing from {param}"
        for dir in Path(f"{param}").iterdir():
            if dir.is_dir() :
                assert_directories_have_inits(dir)


def test_init_present():
    # were gonna check the approval tests
    assert_directories_have_inits("../approvaltests")
    assert_directories_have_inits("../approval_utilities")
    # also check the approval utilities
