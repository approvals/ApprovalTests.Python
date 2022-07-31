from approvaltests import to_json


class VerifiableArgparseNamespace:
    def __init__(self, result ):
        self.result = result


    def __str__(self):
        return to_json(vars(self.result))