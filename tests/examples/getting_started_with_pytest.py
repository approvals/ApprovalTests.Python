from approvaltests.approvals import verify


def test_simple():
    result = "Hello ApprovalTests"
    verify(result)
