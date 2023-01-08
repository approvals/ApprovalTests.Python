from pathlib import Path


def is_dunder(directory_name):
    return "__" in directory_name


def assert_directories_have_inits(param):
    # check the directory to see if it has an init file
    if is_dunder(f"{param}"):
        return
    if not Path(f"{param}/__init__.py").exists():
        assert False, f"__init__.py is missing from {param}"
    # check the subdirectory if they have an init
    for dir in Path(f"{param}").iterdir():
        if dir.is_dir():
            assert_directories_have_inits(dir)

    #if not Path(f"{param}/__init__.py").exists():
    #    assert False, f"__init__.py is missing from {param}"
    # if they dont we fail


def test_init_present():
    # were gonna check the approval tests
    assert_directories_have_inits("../approvaltests")
    assert_directories_have_inits("../approval_utilities")
    # also check the approval utilities
