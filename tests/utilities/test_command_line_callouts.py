from typing import Sequence

from approvaltests import verify
import subprocess

# Future:  have a default joiner  character  like "\n"
# takes an iterable and turns it into a list
# verify_command_line_for_inputs(command, inputs)
# verify_command_line(command, input: str)
# verify_command_line(command)

def test_fizzbuzz_verify_range_1_to_5():
    # verify(command.run(
    #     ["bash", "-c", "jaq -n 'range(100) | .+1' | jaq -f fizzbuzz.jq"]).output.decode("utf8"))
    verify_command_line('jq -n -f test_fizzbuzz.jq')
    verify_command_line('jq -n "range(5) | .+1" | jq -f fizzbuzz.jq')


def verify_command_line_with_inputs(command, input: Sequence[any]):
    input_string="\n".join(map(lambda a: f"{a}", input))
    verify_command_line(command, input=input_string)


def test_command_line_with_input():
    verify_command_line("jq -f fizzbuzz.jq", input="3")

def test_command_line_with_inputs():
    verify_command_line_with_inputs(command="jq -f fizzbuzz.jq", input=range(1, 6))

def verify_command_line(command_line,
                        *  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
                        ,input:str = None):
    verify(subprocess.check_output(command_line, shell=True, universal_newlines=True, input=input))