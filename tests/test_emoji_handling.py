from approvaltests import Options
from approvaltests.utilities.command_line_approvals import verify_command_line


def test_emoji_output() -> None:
    """
    Hello 🌟 World 🎉 Test 🚀
    """
    verify_command_line(
        "python -c \"print('Hello 🌟 World 🎉 Test 🚀')\"", options=Options().inline()
    )
