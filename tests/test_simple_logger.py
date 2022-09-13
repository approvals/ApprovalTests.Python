from approvaltests import verify, args_and_result_formatter
from approvaltests.utilities.logger.simple_logger import SimpleLogger


def log_from_inner_method():
    with SimpleLogger.use_markers() as m:
        name = "Example"
        SimpleLogger.variable("name", name)
        for _ in range(0,142):
            SimpleLogger.hour_glass()


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
