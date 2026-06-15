import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

PACKAGES = [
    ("approval_utilities", "setup.approval_utilities.py"),
    ("approvaltests", "setup.approvaltests.py"),
    ("approvaltests", "setup.approvaltests_minimal.py"),
]


def main() -> None:
    dist_dir = pathlib.Path("dist")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)

    built: list[tuple[str, pathlib.Path]] = []
    for package_name, setup_file in PACKAGES:
        before = set(dist_dir.glob("*.whl")) if dist_dir.exists() else set()

        shutil.copy2("setup/" + setup_file, "setup.py")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "build", "--quiet", "--quiet", "--wheel", "."],
            )
        finally:
            _unlink_with_retry(pathlib.Path("setup.py"))

        after = set(dist_dir.glob("*.whl"))
        new_wheels = after - before
        assert len(new_wheels) == 1, f"Expected 1 new wheel, found {new_wheels}"
        built.append((package_name, new_wheels.pop().resolve()))


    for package_name, wheel_file in built:
        with tempfile.TemporaryDirectory() as _temporary_directory:
            temporary_directory = pathlib.Path(_temporary_directory)

            test_file_path = temporary_directory / "test.py"
            test_file_path.write_text(f"import {package_name}")

            _uv_run_isolated(
                dist_dir,
                temporary_directory,
                with_packages=[wheel_file, "mypy"],
                command=["mypy", test_file_path],
            )

            _uv_run_isolated(
                dist_dir,
                temporary_directory,
                with_packages=[wheel_file],
                command=["python", test_file_path],
            )


def _uv_run_isolated(
    dist_dir: pathlib.Path,
    temporary_directory: pathlib.Path,
    with_packages: list[str | pathlib.Path],
    command: list[str | pathlib.Path],
) -> None:
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

    with_args = [with_package for package in with_packages for with_package in ("--with", package)]

    subprocess.check_call(
        [
            "uv",
            "run",
            "--isolated",
            "--python",
            python_version,
            "--find-links",
            dist_dir.resolve(),
            *with_args,
            "--no-project",
            *command,
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
