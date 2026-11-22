import inspect
import json
import os
from inspect import FrameInfo

from approvaltests.approval_exception import FrameNotFound
from approvaltests.integrations.pytest._pytest_pattern_matching import (
    matches_prefix_or_glob,
)
from approvaltests.integrations.pytest.pytest_config import PytestConfig

UNITTEST_EXCLUDED_METHOD_NAMES = {
    "__call__",
    "_callTestMethod",
    "_callMaybeAsync",
    "_asyncioLoopRunner",
    "run",
}


def get_test_frame_index(caller: list[FrameInfo]) -> int:
    tmp_array = []
    for index, frame in enumerate(caller):
        if is_test_method(frame):
            tmp_array.append(index)
    if tmp_array:
        return tmp_array[-1]
    message = """Could not find test method/function. Possible reasons could be:
1) approvaltests is not being used inside a test function
2) your test framework is not supported by ApprovalTests (unittest and pytest are currently supported)."""
    raise FrameNotFound(message)


def is_pytest_test(frame: FrameInfo) -> bool:
    method_name = frame[3]
    patterns = PytestConfig.test_naming_patterns
    return matches_prefix_or_glob(method_name, patterns)


def is_unittest_test(frame: FrameInfo) -> bool:
    method_name = frame[3]
    local_attributes = frame[0].f_locals
    return (
        "self" in local_attributes
        and hasattr(local_attributes["self"], "__dict__")
        and "_testMethodName" in vars(local_attributes["self"])
        and method_name not in UNITTEST_EXCLUDED_METHOD_NAMES
    )


def is_test_method(frame: FrameInfo) -> bool:
    return is_unittest_test(frame) or is_pytest_test(frame)


def get_test_frame() -> FrameInfo:
    calling_stack = inspect.stack(1)
    return calling_stack[get_test_frame_index(calling_stack)]


def load_config(directory: str) -> dict[str, str]:
    config_file = os.path.join(directory, "approvaltests_config.json")
    if os.path.exists(config_file):
        with open(config_file, encoding="utf8") as file:
            config: dict[str, str] = json.load(file)
            return config
    return {}
