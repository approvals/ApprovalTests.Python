import pathlib
import shutil
import subprocess
import sys
import tempfile
import time


def main() -> None:
    for package_name, setup_file in [
        ("approval_utilities", "setup.approval_utilities.py"),
        ("approvaltests", "setup.approvaltests.py"),
        ("approvaltests", "setup.approvaltests-minimal.py"),
    ]:
        dist_dir = pathlib.Path("dist")
        if dist_dir.exists():
            shutil.rmtree(dist_dir)

        shutil.copy2("setup/" + setup_file, "setup.py")
        try:
            subprocess.check_output([sys.executable, "-m", "build", "--quiet", "--quiet", "--wheel", "."], stderr=subprocess.STDOUT)
        finally:
            _unlink_with_retry(pathlib.Path("setup.py"))

        with tempfile.TemporaryDirectory() as _temporary_directory:
            temporary_directory = pathlib.Path(_temporary_directory)

            wheel_files = list(dist_dir.glob("*.whl"))
            assert len(wheel_files) == 1, f"Expected 1 wheel, found {wheel_files}"
            wheel_file = wheel_files[0].resolve()

            test_file_path = temporary_directory / "test.py"
            test_file_path.write_text(f"import {package_name}")

            python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
            subprocess.check_call(
                [
                    "uv",
                    "run",
                    "--isolated",
                    "--python",
                    python_version,
                    "--with",
                    wheel_file,
                    "--with",
                    "mypy",
                    "--no-project",
                    "mypy",
                    test_file_path,
                ],
                cwd=temporary_directory,
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
