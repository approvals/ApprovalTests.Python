from approval_utilities.utilities.multiline_string_utils import remove_indentation_from
from approvaltests import verify_all
from approvaltests.inline.split_code import SplitCode


def test_splitting_code() -> None:
    code_list = [
        '''
        def other_code():
        \tpass
        def testy_mctest():
        \t"""
        \tApproved: test_inline_approvals.py
        \tReceived:test_inline_approvals.recieved.txt
        \t"""
        \tverify(greeting(), options = Options().inline())
            
        def greeting():
        \t# start of greeting() method
        \treturn "using tabs"
        ''',
        """
        def other_code():
        \tpass
        def testy_mctest():
        \t'''
        \tApproved: test_inline_approvals.py
        \tReceived:test_inline_approvals.recieved.txt
        \t'''
        \tverify(greeting(), options = Options().inline())

        def greeting():
        \t# start of greeting() method
        \treturn "using tabs"
        """,
        '''
        def other_code():
            pass
        def testy_mctest():
            """
            Approved: test_inline_approvals.py
            Received:test_inline_approvals.recieved.txt
            """
            verify(greeting(), options = Options().inline())
            
        def greeting():
            # start of greeting() method
            return "using spaces instead of tabs"
        ''',
        """
        def other_code():
            pass
        def testy_mctest():
            verify(greeting(), options = Options().inline())

        def greeting():
            # start of greeting() method
            return "not using docstring"
        """,
    ]
    verify_all(
        "splitting code",
        code_list,
        lambda code: str(
            SplitCode.on_method(remove_indentation_from(code), "testy_mctest")
        ),
    )
