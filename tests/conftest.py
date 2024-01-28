from tests.approvals_config import configure_approvaltests

import pytest
# The next line registers the plugin
from approvaltests.pytest.pytest_plugin import pytest_configure

# begin-snippet: conftest_pytest_session_scoped
@pytest.fixture(scope="session", autouse=True)
def set_default_reporter_for_all_tests():
    configure_approvaltests()


# end-snippet


