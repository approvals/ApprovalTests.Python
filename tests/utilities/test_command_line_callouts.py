from pathlib import Path

from approvaltests.utilities.command_line_approvals import (
    verify_command_line_with_inputs,
    verify_command_line,
)


def test_verify_command_line():
    verify_command_line("echo hello world!")


def test_verify_command_line_with_input():
    verify_command_line(
        'python -c "import sys; print(sys.stdin.read())"', input="input"
    )

def test_command_line_verify():
    verify_command_line(
        f'python approvaltests/verify.py -t tests/utilities/hello', input="hello world",
        cwd = Path(__file__).parents[2],
        additional_env= {'PYTHONPATH': '.'}
    )



def test_verify_command_line_with_inputs():
    verify_command_line_with_inputs(
        'python -c "import sys; print(sys.stdin.read())"', inputs=range(3, 7)
    )
