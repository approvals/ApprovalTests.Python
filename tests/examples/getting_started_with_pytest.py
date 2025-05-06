from approvaltests.approvals import verify


def test_simple() -> None:
    result = "Hello ApprovalTests"
    verify(result)
