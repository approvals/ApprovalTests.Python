from typing import Any

from typing_extensions import override

from approvaltests.core.namer import Namer
from approvaltests.namer.stack_frame_namer import StackFrameNamer
from approvaltests.namer.templated_custom_namer import TemplatedCustomNamer


class ScenarioNamer(Namer):
    """
    For use with parameterized tests.

    Use this namer when the same test case needs to verify more than one value, and produce more than one file.
    """

    def __init__(
        self, base_namer: StackFrameNamer | TemplatedCustomNamer, *scenario_names: Any
    ) -> None:
        self.base_namer = base_namer
        self.scenario_names = scenario_names
        self.template = base_namer.get_template()
        self.template_field_values = (
            base_namer.get_template_field_values().with_additional_information(
                "." + ".".join(map(str, scenario_names))
            )
        )

    def _create_filename(self, approved_or_received: str) -> str:
        return TemplatedCustomNamer.create_filename(
            self.template,
            self.template_field_values.with_(
                approved_or_received, self.base_namer.extension_with_dot[1:]
            ),
        )

    def get_basename(self) -> str:
        basename = self.base_namer.get_basename()
        scenarios = ".".join(map(str, self.scenario_names))
        return f"{basename}.{scenarios}"

    @override
    def get_approved_filename(self) -> str:
        return self._create_filename(Namer.APPROVED_WITHOUT_DOT)

    @override
    def get_received_filename(self) -> str:
        return self._create_filename(Namer.RECEIVED_WITHOUT_DOT)

    def set_extension(self, extension: str) -> None:
        self.base_namer.set_extension(extension)
