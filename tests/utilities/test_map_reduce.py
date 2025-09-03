from approval_utilities.utilities.map_reduce import first, product_dict
from approvaltests import Options, verify_as_json


def test_first() -> None:
    assert first([1, 2, 3], lambda x: x == 2) == 2
    assert first([1, 2, 3], lambda x: x == 4) is None
    assert first([], lambda x: x == 4) is None


def test_product_dict() -> None:
    """
    [
        {
            "a": 1,
            "b": 3
        },
        {
            "a": 1,
            "b": 4
        },
        {
            "a": 2,
            "b": 3
        },
        {
            "a": 2,
            "b": 4
        }
    ]
    """
    result = list(product_dict(a=[1, 2], b=[3, 4]))
    verify_as_json(result, options=Options().inline())
