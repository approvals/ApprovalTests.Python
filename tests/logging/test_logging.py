import logging
from datetime import datetime

from approvaltests.utilities.logging.logging_approvals import verify_logging


def test_basic_logging() -> None:
    with verify_logging():
        logging.info("1")
        logging.info(datetime.now())
