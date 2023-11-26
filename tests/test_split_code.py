from approvaltests import verify


class SplitCode:
    def __init__(self, before_method, after_method):
        self.before_method = before_method
        self.after_method = after_method
    def __str__(self):
        return f"before:\n{self.before_method}\nafter:\n{self.after_method}"
    @staticmethod
    def on_method(code, method_name):
        # cycles through the lines of the codE
        # add to before until it finds the method name
        # skip the doc string
        # then add to after until it finds the next method name
        before_method = ""

        for line in code.splitlines():

            if method_name in line:
                break
            before_method += line
        before_method = code.split(f"def {method_name}")[0]
        after_method = code.split(f"def {method_name}")[1]
        return SplitCode(before_method, after_method)


def test_splitting_code():
    code = \
    '''
def other_code():
   pass
def testy_mctest():
    """
    Approved: test_inline_approvals.py
    Received:test_inline_approvals.recieved.txt
    """
    verify(greeting(), options = Options().inline())

    '''
    verify(SplitCode.on_method(code, "testy_mctest"))