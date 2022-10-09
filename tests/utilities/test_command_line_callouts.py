from typing import Sequence

from approvaltests import verify
import subprocess


def test_verify_command_line():
    verify_command_line('echo "hello world!"')

def test_verify_command_line_with_input():
    verify_command_line('python -c "import sys; print(sys.stdin.read())"', input="input")

def test_verify_command_line_with_inputs():
    verify_command_line_with_inputs('python -c "import sys; print(sys.stdin.read())"', inputs=range(3,7))

def verify_command_line_with_inputs(command, inputs: Sequence[any]):
    input_string="\n".join(map(lambda a: f"{a}", inputs))
    verify_command_line(command, input=input_string)

def verify_command_line(command_line,
                        *  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
                        ,input:str = None):
    verify(subprocess.check_output(command_line, shell=True, universal_newlines=True, input=input))