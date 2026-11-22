from approvaltests.reporters.ai_coding_agent_reporter import AiCodingAgentReporter
from approvaltests.reporters.environment_variable_reporter import (
    EnvironmentVariableReporter,
)
from approvaltests.reporters.first_working_reporter import FirstWorkingReporter


class DefaultFrontLoadedReporter(FirstWorkingReporter):
    def __init__(self) -> None:
        super().__init__(EnvironmentVariableReporter(), AiCodingAgentReporter())
