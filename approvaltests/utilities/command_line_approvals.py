import os
import subprocess
from typing import Any, Dict, Optional, Sequence

from approvaltests import Options, verify


def verify_command_line_with_inputs(
    command: str,
    *,
    inputs: Optional[Sequence[Any]] = None,
    options: Optional[Options] = None,
) -> None:
    input_string = "\n".join(map(lambda a: f"{a}", inputs))
    verify_command_line(command, input_string=input_string, options=options)


def verify_command_line(
    command_line: str,
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    input_string: Optional[str] = None,
    options: Optional[Options] = None,
    current_working_directory: str = ".",
    additional_environment_variables: Optional[Dict[str, str]] = None,
) -> None:
    # Set up environment with UTF-8 support for Windows
    my_env = {**os.environ}

    # Ensure UTF-8 encoding on Windows for emoji support
    if os.name == "nt":  # Windows
        my_env.update({"PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"})

    if additional_environment_variables:
        my_env.update(additional_environment_variables)
    try:
        result = subprocess.run(
            command_line,
            shell=True,
            text=True,
            encoding="utf-8",
            input=input_string,
            cwd=current_working_directory,
            env=my_env,
            capture_output=True,
        )
        output = result.stdout
        if result.stderr:
            output += "\n--- STDERR ---\n" + result.stderr
    except UnicodeDecodeError:
        # Fallback to system default encoding if UTF-8 fails
        result = subprocess.run(
            command_line,
            shell=True,
            text=True,
            input=input_string,
            cwd=current_working_directory,
            env=my_env,
            capture_output=True,
        )
        output = result.stdout
        if result.stderr:
            output += "\n--- STDERR ---\n" + result.stderr
    verify(
        output,
        options=options,
    )
