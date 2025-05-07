__author__ = "Chris Lucian; Llewellyn Falco; Jim Counts"

from tests.approvals_config import configure_approvaltests

# mypy: disable-error-code=no-untyped-call

# begin-snippet: configure_approvaltests_under_init
# From __init__.py
configure_approvaltests()
# end-snippet
