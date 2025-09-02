from pathlib import Path

import yaml

from approvaltests import verify

SCRIPT_DIR = Path(__file__).parent.resolve()


def test_workflow_matrix_python_versions() -> None:
    test_workflow = yaml.safe_load(
        (SCRIPT_DIR.parent / ".github/workflows/test.yml").read_text()
    )
    python_versions = test_workflow["jobs"]["build"]["strategy"]["matrix"][
        "python-version"
    ]

    test_min_workflow = yaml.safe_load(
        (SCRIPT_DIR.parent / ".github/workflows/test_min.yml").read_text()
    )
    python_versions_min = test_min_workflow["jobs"]["build"]["strategy"]["matrix"][
        "python-version"
    ]
    assert python_versions == python_versions_min, (
        "Python version matrix in test.yml and test_min.yml do not match"
    )

    test_current_release_workflow = yaml.safe_load(
        (SCRIPT_DIR.parent / ".github/workflows/test_current_release.yml").read_text()
    )
    python_versions_current_release = test_current_release_workflow["jobs"]["build"][
        "strategy"
    ]["matrix"]["python-version"]
    assert python_versions == python_versions_current_release, (
        "Python version matrix in test.yml and test_current_release.yml do not match"
    )

    verify(
        f"ApprovalTests is tested on the following Python versions: {', '.join(python_versions)}."
    )
