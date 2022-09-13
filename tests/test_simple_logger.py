from approvaltests import verify
from approvaltests.utilities.logger.simple_logger import SimpleLogger


def log_from_inner_method():
    with SimpleLogger.use_markers() as m:
        pass


def test_standard_logger():
    """
    SimpleLogger.printLineNumber()
    do {
        let m2 = SimpleLogger.useMarkers()
        let name = "llewellyn"
        SimpleLogger.variable("name", name)
        for _ in 0 ..< 142 {
            SimpleLogger.hourGlass()
        }
    }

    """
    output = SimpleLogger.log_to_string()
    with SimpleLogger.use_markers() as m:
        log_from_inner_method()
    verify(output)
