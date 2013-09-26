from approvaltests.Reporter import Reporter


class TestingReporter(Reporter):

    def __init__(self):
        self.called = False

    def report(self, approved_path, received_path):
        self.called = True
