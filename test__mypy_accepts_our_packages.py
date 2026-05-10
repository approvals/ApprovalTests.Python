import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

PACKAGES = [
    ("approval_utilities", "setup.approval_utilities.py"),
    ("approvaltests", "setup.approvaltests.py"),
    ("approvaltests", "setup.approvaltests-minimal.py"),
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

    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

    for package_name, wheel_file in built:
        with tempfile.TemporaryDirectory() as _temporary_directory:
            temporary_directory = pathlib.Path(_temporary_directory)

            test_file_path = temporary_directory / "test.py"
            test_file_path.write_text(f"import {package_name}")

            subprocess.check_call(
                [
                    "uv",
                    "run",
                    "--isolated",
                    "--python",
                    python_version,
                    "--find-links",
                    str(dist_dir.resolve()),
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
