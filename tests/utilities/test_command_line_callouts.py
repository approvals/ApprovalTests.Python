from pathlib import Path

from approvaltests.utilities.command_line_approvals import (
    verify_command_line_with_inputs,
    verify_command_line,
)


def test_verify_command_line():
    verify_command_line("echo hello world!")


def test_verify_command_line_with_input():
    verify_command_line(
        'python -c "import sys; print(sys.stdin.read())"', input_string="input"
    )


def test_command_line_verify():
    verify_command_line(
        f"python approvaltests/commandline_interface.py -t tests/utilities/passing_command_line_verify",
        input_string="hello from command line interface",
        current_working_directory=Path(__file__).parents[2],
        additional_environment_variables={"PYTHONPATH": "."},
    )


def test_verify_command_line_with_inputs():
    verify_command_line_with_inputs(
        'python -c "import sys; print(sys.stdin.read())"', inputs=range(3, 7)
    )
