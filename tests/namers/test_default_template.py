import os

from approvaltests import verify_all
from approvaltests.namer.default_name import get_default_namer
from approvaltests.namer.stack_frame_namer import StackFrameNamer
from approvaltests.namer.templated_custom_namer import TemplatedCustomNamer

SUBDIRECTORIES = ["", "my_subdir"]


def template_names(subdirectory: str) -> list[str]:
    namer = TemplatedCustomNamer(TemplatedCustomNamer.DEFAULT_TEMPLATE)
    namer.approvals_subdirectory = subdirectory
    return [namer.get_approved_filename(), namer.get_received_filename()]


def default_names(subdirectory: str) -> list[str]:
    namer = get_default_namer()
    assert isinstance(namer, StackFrameNamer)
    namer.config = {"subdirectory": subdirectory}
    namer.config_loaded = True
    return [namer.get_approved_filename(), namer.get_received_filename()]


def compare_names(subdirectory: str) -> str:
    template = template_names(subdirectory)
    same = list(map(os.path.normpath, template)) == list(
        map(os.path.normpath, default_names(subdirectory))
    )
    relative = [os.path.relpath(name).replace(os.sep, "/") for name in template]
    return f"same as default namer: {same}, names: {relative}"


class TestDefaultTemplate:
    def test_class_method(self) -> None:
        verify_all("subdirectory", SUBDIRECTORIES, compare_names)


def test_function() -> None:
    verify_all("subdirectory", SUBDIRECTORIES, compare_names)
