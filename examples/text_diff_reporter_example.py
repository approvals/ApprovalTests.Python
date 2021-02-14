from approvaltests import approvals
from approvaltests.TextDiffReporter import TextDiffReporter
import os
import unittest


class Test(unittest.TestCase):
    def __init__(self):
        # This environment variable should be set somewhere outside of the test
        # but is here to make the example clearer.
        os.environ["APPROVALS_TEXT_DIFF_TOOL"] = "meld"

    def test(self):
        reporter = TextDiffReporter()
        approvals.verify("x", reporter)


if __name__ == "__main__":
    unittest.main()
