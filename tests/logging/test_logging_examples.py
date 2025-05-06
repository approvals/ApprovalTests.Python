import logging

from approval_utilities.utilities.multiline_string_utils import remove_indentation_from
from approvaltests import verify
from approvaltests.namer import NamerFactory
from approvaltests.utilities.logging.logging_approvals import verify_logging


def load_person() -> str:
    logging.info("connecting to the database")
    logging.info("querying a table")
    logging.info("closing the database")

    return remove_indentation_from(
        """
    {
        "first_name":"Britney",
        "last_name": "Spears",
        "profession":"Singer"    
    }
    """
    )


# begin-snippet: test_logging_separately
def test_load_person_logs():
    with verify_logging():
        load_person()


# end-snippet


# begin-snippet: test_logging_separately_results
def test_load_person_results():
    verify(load_person())


# end-snippet


# begin-snippet: testing_logging_combined_with_results
def test_load_person_logs_and_results():
    with verify_logging():
        logging.info(f"result = {load_person()}")


# end-snippet


# begin-snippet: testing_logging_with_namer_factory
def test_load_person_logs_and_results_separately():
    with verify_logging(options=NamerFactory.with_parameters("logging")):
        verify(load_person())


# end-snippet
