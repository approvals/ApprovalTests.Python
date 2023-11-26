from approval_utilities.utilities.multiline_string_utils import remove_indentation_from
from approvaltests import verify


class SplitCode:
    def __init__(self, before_method, after_method):
        self.before_method = before_method
        self.after_method = after_method
    def __str__(self):
        return f"before:\n{self.before_method}\nafter:\n{self.after_method}"
    @staticmethod
    def on_method(code, method_name):
        lines = code.split('\n')
        before = []
        after = []
        inside_method = False
        inside_doc_string = False

        for line in lines:
            stripped_line = line.strip()

            # Detect the start of a method
            if stripped_line.startswith('def ') and stripped_line.endswith('):'):
                current_method = stripped_line.split(' ')[1].split('(')[0]

                if current_method == method_name:
                    inside_method = True
                    before.append(line)  # Include method signature in 'before'
                    continue
                elif inside_method:
                    # Exit the method and start 'after'
                    inside_method = False
                    after.append(line)
                    continue

            if inside_method:
                # Detect and skip the docstring
                if stripped_line.startswith('"""'):
                    if not inside_doc_string:  # Start of docstring
                        inside_doc_string = True
                    else:  # End of docstring
                        inside_doc_string = False
                    continue

                if not inside_doc_string:
                    after.append(line)  # Include other contents of the method in 'after'
                continue

            if not inside_method:
                before.append(line)
        return SplitCode('\n'.join(before), '\n'.join(after))




def test_splitting_code():
    code = \
    remove_indentation_from('''
        def other_code():
           pass
        def testy_mctest():
            """
            Approved: test_inline_approvals.py
            Received:test_inline_approvals.recieved.txt
            """
            verify(greeting(), options = Options().inline())
        ''');
    verify(SplitCode.on_method(code, "testy_mctest"))