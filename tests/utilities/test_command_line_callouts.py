from pathlib import Path

from approvaltests import Options
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
    import tempfile
    # create a temporary directory
    temp_dir: Path = Path(tempfile.TemporaryDirectory().name)
    temp_dir.mkdir()
    working_directory: Path = Path(__file__).parents[2]
    python_script_path = working_directory / "approvaltests/commandline_interface.py"
    test_script_path = working_directory / "tests/utilities/passing_command_line_verify"
    working_directory_str = str(working_directory.resolve())
    verify_command_line(
        f"python {python_script_path} -t {test_script_path}",
        input_string="hello from command line interface",
        current_working_directory=str(temp_dir.resolve()),
        additional_environment_variables={"PYTHONPATH": working_directory_str},
        options=Options().with_scrubber(lambda s: s.replace(working_directory_str, ".").replace("\\", "/")),
    )


def test_verify_command_line_with_inputs():
    verify_command_line_with_inputs(
        'python -c "import sys; print(sys.stdin.read())"', inputs=range(3, 7)
    )
