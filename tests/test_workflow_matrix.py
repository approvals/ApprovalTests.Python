import yaml
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()

def test_workflow_matrix_python_versions() -> None:
    test_workflow = yaml.safe_load((SCRIPT_DIR.parent / '.github/workflows/test.yml').read_text())
    test_matrix = test_workflow['jobs']['build']['strategy']['matrix']
    
    test_min_workflow = yaml.safe_load((SCRIPT_DIR.parent / '.github/workflows/test_min.yml').read_text())
    test_min_matrix = test_min_workflow['jobs']['build']['strategy']['matrix']    
    assert test_matrix == test_min_matrix, "Matrix configurations in test.yml and test_min.yml do not match"

    test_current_release_workflow = yaml.safe_load((SCRIPT_DIR.parent / '.github/workflows/test_current_release.yml').read_text())
    test_current_release_matrix = test_current_release_workflow['jobs']['build']['strategy']['matrix']
    assert test_matrix == test_current_release_matrix, "Matrix configurations in test.yml and test_current_release.yml do not match"

