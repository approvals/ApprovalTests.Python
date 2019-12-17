
class PytestNamer:
    """
    For use with parameterized pytest tests.

    Use this namer when the same test case needs to verify more than one value, and produce more than one file.
    """
    def __init__(self, base_namer, pytest_request):
        self.base_namer = base_namer
        if pytest_request.node.originalname:
            self.parameters = pytest_request.node.name[len(pytest_request.node.originalname):]
        else:
            self.parameters = ''

    def get_basename(self):
        basename = self.base_namer.get_basename()
        return basename + self.parameters

    def get_approved_filename(self, basename=None):
        if basename is None:
            basename = self.get_basename()
        return self.base_namer.get_approved_filename(basename)

    def get_received_filename(self, basename=None):
        if basename is None:
            basename = self.get_basename()
        return self.base_namer.get_received_filename(basename)
