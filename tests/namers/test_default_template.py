import os

from approvaltests import verify_all
from approvaltests.core.scenario_namer import ScenarioNamer
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


PARAMETERS = [(), ("a",), ("a", 2), ("ci", None, 3.5)]


def template_names_with_parameters(parameters: tuple) -> list[str]:
    namer = TemplatedCustomNamer(TemplatedCustomNamer.DEFAULT_TEMPLATE)
    namer.approvals_subdirectory = ""
    namer.additional_information = ".".join(map(str, parameters))
    return [namer.get_approved_filename(), namer.get_received_filename()]


def scenario_names(parameters: tuple) -> list[str]:
    namer = ScenarioNamer(get_default_namer(), *parameters)
    return [namer.get_approved_filename(), namer.get_received_filename()]


def compare_names_with_parameters(parameters: tuple) -> str:
    template = template_names_with_parameters(parameters)
    expected = scenario_names(parameters) if parameters else default_names("")
    same = list(map(os.path.normpath, template)) == list(
        map(os.path.normpath, expected)
    )
    relative = [os.path.relpath(name).replace(os.sep, "/") for name in template]
    return f"same as scenario namer: {same}, names: {relative}"


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

    def test_parameters(self) -> None:
        verify_all("parameters", PARAMETERS, compare_names_with_parameters)


def test_function() -> None:
    verify_all("subdirectory", SUBDIRECTORIES, compare_names)
