from pathlib import Path
from typing import List
import yaml

from approvaltests import verify

SCRIPT_DIR = Path(__file__).parent.resolve()


def test_workflow_matrix_python_versions() -> None:
    python_versions = _get_workflow_matrix_python_versions("test.yml")
    python_versions_min = _get_workflow_matrix_python_versions("test_min.yml")
    assert python_versions == python_versions_min, (
        "Python version matrix in test.yml and test_min.yml do not match"
    )

    python_versions_current_release = _get_workflow_matrix_python_versions("test_current_release.yml")
    assert python_versions == python_versions_current_release, (
        "Python version matrix in test.yml and test_current_release.yml do not match"
    )

    verify(
        f"ApprovalTests is tested on the following Python versions: {', '.join(python_versions)}."
    )

def _get_workflow_matrix_python_versions(filename: str) -> List[str]:
    test_workflow = yaml.safe_load(
        (SCRIPT_DIR.parent / ".github/workflows" / filename).read_text()
    )
    python_versions = test_workflow["jobs"]["build"]["strategy"]["matrix"][
        "python-version"
    ]
    
    return python_versions
