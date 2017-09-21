import os
from unittest import TestCase

from approvaltests import approvals
from approvaltests.reporters.clipboard_reporter import CommandLineReporter 
from approvaltests.reporters.multi_reporter import MultiReporter 
from approvaltests.reporters.diff_reporter import DiffReporter 
from approvaltests.generic_diff_reporter import GenericDiffReporter


class TestList(TestCase):
    def setUp(self):
        reporter = MultiReporter(GenericDiffReporter.create('diff'), CommandLineReporter())
        approvals.set_default_reporter(reporter)
        
    def test(self):
        alist = ['a', 'b', 'c', 'd', 'e']
        approvals.verify_all('letters', alist, reporter=DiffReporter())

    def test_uppercase(self):
        alist = ['a', 'b', 'c', 'd']
        approvals.verify_all('uppercase', alist, lambda x: '{0} => {1}'.format(x, x.upper()))
