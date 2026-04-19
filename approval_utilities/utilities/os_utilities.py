import subprocess


def run_command(command_array: list[str]) -> None:
    with subprocess.Popen(command_array):
        pass
