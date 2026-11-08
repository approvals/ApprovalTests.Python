from approvaltests.reporters.ai_coding_agent_reporter import AiCodingAgentReporter


def test_detects_an_agent_when_claudecode_is_set() -> None:
    environment = {"CLAUDECODE": "1"}

    assert AiCodingAgentReporter.is_agent_detected(environment)
