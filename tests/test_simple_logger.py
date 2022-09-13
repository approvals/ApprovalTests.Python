from approvaltests import verify
from approvaltests.utilities.logger.simple_logger import SimpleLogger


def test_standard_logger():
    '''
      let output = SimpleLogger.logToString()
        do {
            let m = SimpleLogger.useMarkers()
            SimpleLogger.printLineNumber()
            do {
                let m2 = SimpleLogger.useMarkers()
                let name = "llewellyn"
                SimpleLogger.variable("name", name)
                for _ in 0 ..< 142 {
                    SimpleLogger.hourGlass()
                }
            }
        }
        try Approvals.verify(output)
    '''
    output = SimpleLogger.log_to_string()
    with SimpleLogger.use_markers() as m :
        pass
    verify(output)
    """
    
-> in: test_standard_logger()test_simple_logger.py
<- out: test_standard_logger()test_simple_logger.py
    """
    
    
        
