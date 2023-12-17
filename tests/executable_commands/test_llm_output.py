from approvaltests import verify, verify_executable_command
import pytest

from approval_utilities.approvaltests.core.executable_command import ExecutableCommand

from openai import OpenAI

client = OpenAI()


def call_llm(prompt: str) -> str:
    pass


class CallLlm(ExecutableCommand):
    def get_command(self) -> str:
        return """
        please rename the name foo to smthg better

        ---

        ```
        function foo(a,b) {
        return a +b
        }
        ```

        output format:
        suggested name - <name here>
        """

    def execute_command(self, command: str) -> str:
        completion = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": command},
            ],
        )
        return completion.choices[0].message.content


def test_total_output():
    verify_executable_command(CallLlm())


def get_new_name(llm_output):
    pass


@pytest.mark.skip()
def test_useful_output():
    verify(get_new_name(llm_output=reuse_recorded_llm_output()))
