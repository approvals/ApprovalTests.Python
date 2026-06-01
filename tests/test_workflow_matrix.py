from pathlib import Path

import yaml

from approvaltests import verify
from setup.setup_utils import PYTHON_VERSIONS

SCRIPT_DIR = Path(__file__).parent.resolve()


def test_workflow_matrixes_match() -> None:
    _assert_workflow_matrix_python_versions_match(
        "test.yml", "test_minimum_dependency_versions.yml"
    )
    _assert_workflow_matrix_python_versions_match(
        "test.yml", "test_current_release.yml"
    )


def test_tested_versions_message() -> None:
    python_versions = _get_workflow_matrix_python_versions("test.yml")
    verify(
        f"ApprovalTests is tested on the following Python versions: {', '.join(python_versions)}."
    )


def test_package_classifiers() -> None:
    assert PYTHON_VERSIONS == _get_workflow_matrix_python_versions("test.yml")


def _assert_workflow_matrix_python_versions_match(left: str, right: str) -> None:
    python_versions = _get_workflow_matrix_python_versions(left)
    python_versions_min = _get_workflow_matrix_python_versions(right)
    assert python_versions == python_versions_min, (
        f"Python version matrix in {left} and {right} do not match"
    )


def _get_workflow_matrix_python_versions(filename: str) -> list[str]:
    test_workflow = yaml.safe_load(
        (SCRIPT_DIR.parent / ".github/workflows" / filename).read_text()
    )
    python_versions = test_workflow["jobs"]["build"]["strategy"]["matrix"][
        "python-version"
    ]

    assert isinstance(python_versions, list), (
        f"Expected python-version to be a list in {filename}"
    )
    return python_versions
