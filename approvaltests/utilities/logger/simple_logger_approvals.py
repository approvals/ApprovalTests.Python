from types import TracebackType
from typing import ContextManager

from approval_utilities.utilities.logger.simple_logger import SimpleLogger
from approvaltests.approvals import verify
from approvaltests.core.options import Options


def verify_simple_logger(
    *,  # enforce keyword arguments - https://www.python.org/dev/peps/pep-3102/
    options: Options | None = None,
) -> ContextManager[None]:
    class VerifySimpleLogger:
        def __init__(self) -> None:
            self.output = SimpleLogger.log_to_string()

        def __enter__(self) -> None:
            pass

        def __exit__(
            self,
            exc_type: type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None,
        ) -> bool:
            verify(self.output, options=options)

    return VerifySimpleLogger()
