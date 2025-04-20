import pathlib
import tempfile
import subprocess
import sys
import time
import typing
import os

from version import version_number


def main() -> None:
    for package_name, setup_file in [
        ("approval_utilities", "setup.approval_utilities.py"),
        ("approvaltests", "setup.py"),
    ]:
        build_number = str(int(time.time()))
        _run_python_checked(
            [
                setup_file,
                "bdist_wheel",
                "--build-number",
                build_number,
            ]
        )
        _run_python_checked(
            [
                "-m",
                "pip",
                "install",
                "--force-reinstall",
                # version_number starts with `v`; remove that character
                f"dist/{package_name}-{version_number[1:]}-{build_number}-py3-none-any.whl",
            ]
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = pathlib.Path(temp_dir)
            test_file_path = temp_path / "test.py"
            test_file_path.write_text(f"import {package_name}")

            _run_python_checked(
                ["-m", "mypy", str(test_file_path)],
                cwd=temp_path,
            )


def _run_python_checked(
    args: typing.List[str], cwd: typing.Optional[pathlib.Path] = None
) -> None:
    subprocess.run(
        [sys.executable, *args],
        check=True,
        cwd=cwd,
    )


if __name__ == "__main__":
    main()
