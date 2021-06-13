from tests.approvals_config import configure_approvaltests

import pytest

# begin-snippet: conftest_pytest_session_scoped
@pytest.fixture(scope="session", autouse=True)
def set_default_reporter():
    configure_approvaltests()
# end-snippet