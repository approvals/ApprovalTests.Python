from typing import List


def compare_log_and_file_system(
    log_file_names: List[str], fs_file_names: List[str]
) -> List[str]:
    return [file for file in fs_file_names if file not in log_file_names]


def test_returns_empty_list_for_two_empty_lists() -> None:
    log_file_names: List[str] = []
    fs_file_names: List[str] = []
    assert compare_log_and_file_system(log_file_names, fs_file_names) == []


def test_returns_empty_list_for_identical_lists() -> None:
    log_file_names = ["a", "b", "c"]
    fs_file_names = ["a", "b", "c"]
    assert compare_log_and_file_system(log_file_names, fs_file_names) == []


def test_returns_items_only_in_fs() -> None:
    log_file_names = ["a", "b", "c"]
    fs_file_names = ["a", "b", "c", "d", "e"]
    assert compare_log_and_file_system(log_file_names, fs_file_names) == ["d", "e"]


# Future tests
# 1 - fs:[a,b,c], log:[a,b,c] => []
# 2 - fs:[a,b,c,d], log:[a,b,c] => [d]
