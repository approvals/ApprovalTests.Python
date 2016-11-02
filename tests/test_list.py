import os
from unittest import TestCase

from approvaltests import Approvals
from approvaltests.TextDiffReporter import TextDiffReporter
from approvaltests.reporters.clipboard_reporter import CommandLineReporter 
from approvaltests.reporters.multi_reporter import MultiReporter 


class TestList(TestCase):
    def setUp(self):
        os.environ["APPROVALS_TEXT_DIFF_TOOL"] = 'diff' 
        reporter = MultiReporter(TextDiffReporter(), CommandLineReporter())
        Approvals.set_default_reporter(reporter)
        
    def test(self):
        alist = ['a', 'b', 'c', 'd', 'e']
        Approvals.verify_all('letters', alist)

    def test_uppercase(self):
        alist = ['a', 'b', 'c', 'd']
        Approvals.verify_all('uppercase', alist, lambda x: '{0} => {1}'.format(x, x.upper()))
