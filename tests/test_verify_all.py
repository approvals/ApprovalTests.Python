from approvaltests import Options, verify_all


def test_verify_all_with_no_header() -> None:
    """
    0) 1
    1) 2
    2) 3
    """
    verify_all("", ["1", "2", "3"], options=Options().inline())


def test_dict() -> None:
    """
    0) k1
    """
    verify_all("", {"k1": "v1"}, options=Options().inline())


def test_dict_items() -> None:
    """
    0) ('k1', 'v1')
    """
    verify_all("", {"k1": "v1"}.items(), options=Options().inline())
