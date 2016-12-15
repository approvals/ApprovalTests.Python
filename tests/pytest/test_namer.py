from approvaltests.Approvals import get_default_namer, verify


def test_basic_approval():
    verify("foo")


def test_received_filename():
    namer = get_default_namer()
    assert namer.get_received_filename().endswith("ApprovalTests.Python/tests/pytest/test_namer.test_received_filename.received.txt")