# use an approval test
# generate the command file contents and approve that contents
# two failing tests that use the new reporter
from approvaltests import Options, verify, Reporter
from approved_file_log import APPROVAL_TESTS_TEMP_DIRECTORY
from reporters import get_command_text


# approval_script.bat is the name of the script that will be created

# We want a class, not a function.  Reporters are classes.  Case matters in Python.
# Once we choose a reporter, we can use it in all our tests.


class ReporterThatCreatesAnApprovalScript (Reporter):
    def create_approval_script(self, script:str):
        dir = APPROVAL_TESTS_TEMP_DIRECTORY
        with open(f"{dir}/approval_script.bat", "a") as f:
            f.write(script)
            f.write("\n")

    def report(self, received_path: str, approved_path: str) -> bool:
        self.create_approval_script( get_command_text(received_path, approved_path))
        return True


def test_first():
    verify("hello first test", options=Options().with_reporter(ReporterThatCreatesAnApprovalScript()))

def test_two():
    verify("hello second test", options=Options().with_reporter(ReporterThatCreatesAnApprovalScript()))