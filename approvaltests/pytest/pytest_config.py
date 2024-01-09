class PytestConfig:
    test_naming_pattern = "test_*"

    @staticmethod
    def set_config(config):
        PytestConfig.test_naming_pattern = config.getini("python_functions")


def pytest_config(config):
    PytestConfig.set_config(config)
