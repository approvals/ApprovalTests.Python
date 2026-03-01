import glob
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time
import typing


def main() -> None:
    for package_name, setup_file in [
        ("approval_utilities", "setup/setup.approval_utilities.py"),
        ("approvaltests", "setup/setup.py"),
    ]:
        print(f"Testing build {package_name} ...")
        dist_dir = pathlib.Path("dist")
        if dist_dir.exists():
            shutil.rmtree(dist_dir)

        shutil.copy2(setup_file, "setup.py")
        try:
            _run_python_checked(["-m", "build", "--wheel", "."], quiet=True)
        finally:
            _unlink_with_retry(pathlib.Path("setup.py"))

        wheel_files = glob.glob("dist/*.whl")
        assert len(wheel_files) == 1, f"Expected 1 wheel, found {wheel_files}"
        _run_python_checked(
            [
                "-m",
                "pip",
                "install",
                "--force-reinstall",
                wheel_files[0],
                "--quiet",
                "--no-warn-script-location",
            ]
        )

        with tempfile.TemporaryDirectory() as _temporary_directory:
            temporary_directory = pathlib.Path(_temporary_directory)
            test_file_path = temporary_directory / "test.py"
            test_file_path.write_text(f"import {package_name}")

            _run_python_checked(
                ["-m", "mypy", str(test_file_path)],
                cwd=temporary_directory,
            )


def _run_python_checked(
    args: typing.List[str],
    cwd: typing.Optional[pathlib.Path] = None,
    quiet: bool = False,
) -> None:
    subprocess.run(
        [sys.executable, *args],
        check=True,
        cwd=cwd,
        stdout=subprocess.DEVNULL if quiet else None,
        stderr=subprocess.DEVNULL if quiet else None,
    )


def _unlink_with_retry(
    path: pathlib.Path, retries: int = 5, delay: float = 1.0
) -> None:
    for attempt in range(retries):
        try:
            path.unlink(missing_ok=True)
            return
        except PermissionError:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise


if __name__ == "__main__":
    main()
