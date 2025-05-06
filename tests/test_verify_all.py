from approvaltests import Options, verify_all


def test_verify_all_with_no_header() -> None:
    """
    0) 1
    1) 2
    2) 3
    """
    verify_all("", ["1", "2", "3"], options=Options().inline())
