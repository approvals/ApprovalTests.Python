import subprocess
from typing import Sequence

from approvaltests import verify, Options


def verify_command_line_with_inputs(
    command, *, inputs: Sequence[any] = None, options: Options = None
):
    input_string = "\n".join(map(lambda a: f"{a}", inputs))
    verify_command_line(command, input=input_string, options=options)


def verify_command_line(
    command_line,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    input: str = None,
    options: Options = None,
):
    verify(
        subprocess.check_output(
            command_line, shell=True, universal_newlines=True, input=input
        ),
        options=options,
    )
