import os
from typing import ClassVar, Mapping

from typing_extensions import override

from approvaltests.core.reporter import Reporter
from approvaltests.reporters.python_native_reporter import PythonNativeReporter


class AiCodingAgentReporter(Reporter):
    """
    A reporter for tests run by an AI coding agent.

    When an agent is detected, it prints the failure as text the
    agent can read, so that no visual diff tool is opened.
    """

    ENVIRONMENT_VARIABLES: ClassVar[list[str]] = [
        "AI_AGENT",
        "APPROVAL_TESTS_AGENT",
        "CLAUDECODE",
        "CLAUDE_CODE_ENTRYPOINT",
        "CODEX_SANDBOX",
        "CURSOR_AGENT",
        "CURSOR_TRACE_ID",
        "GEMINI_CLI",
        "OPENCODE",
    ]
    FALSE_VALUES: ClassVar[list[str]] = ["", "0", "f", "F", "false", "FALSE", "False"]

    @staticmethod
    def is_agent_detected(environment: Mapping[str, str] | None = None) -> bool:
        values = os.environ if environment is None else environment
        return any(
            values.get(variable, "") not in AiCodingAgentReporter.FALSE_VALUES
            for variable in AiCodingAgentReporter.ENVIRONMENT_VARIABLES
        )

    @override
    def report(self, received_path: str, approved_path: str) -> bool:
        if not self.is_agent_detected():
            return False
        return PythonNativeReporter().report(received_path, approved_path)
