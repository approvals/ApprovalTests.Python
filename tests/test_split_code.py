from approval_utilities.utilities.multiline_string_utils import remove_indentation_from
from approvaltests import verify
from approvaltests.inline.split_code import SplitCode


def test_splitting_code():
    code = remove_indentation_from(
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
            return "hello world"
        '''
    )
    verify(SplitCode.on_method(code, "testy_mctest"))
