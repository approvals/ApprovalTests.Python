import os
from unittest import TestCase

from approvaltests import Approvals
from approvaltests.TextDiffReporter import TextDiffReporter


class TestList(TestCase):
    def setUp(self):
        os.environ["APPROVALS_TEXT_DIFF_TOOL"] = 'diff' 
        Approvals.set_default_reporter(TextDiffReporter())
        

    def test(self):
        alist = ['a', 'b', 'c', 'd']
        Approvals.verify_all('letters', alist)
