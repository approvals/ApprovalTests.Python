from approval_utilities.utilities import markdown_table
from approvaltests import Options, verify, verify_exception
from approvaltests.scrubbers.date_scrubber import DateScrubber


def test_supported_formats() -> None:
    supported_formats = DateScrubber.get_supported_formats()
    for date_regex, examples in supported_formats:
        for example in examples:
            assert DateScrubber(date_regex).scrub(example) == "<date0>"


def test_supported_formats_arbitrary_string() -> None:
    assert (
        DateScrubber("[a-zA-Z]{3} [a-zA-Z]{3} \\d{2} \\d{2}:\\d{2}:\\d{2}").scrub(
            "arbitrary string"
        )
        == "arbitrary string"
    )


def test_supported_format_example() -> None:
    # begin-snippet: scrub-date-example
    verify(
        "created at 03:14:15",
        options=Options().with_scrubber(DateScrubber.get_scrubber_for("00:00:00")),
    )
    # end-snippet


def test_adds_valid_date_scrubber():
    """
    Hello on <date0>
    """
    text = "2025-07-20"
    DateScrubber.add_scrubber(text, "\\d{4}-\\d{2}-\\d{2}")
    print("DEBUG: About to call verify, DateScrubber.get_scrubber_for(text)=", DateScrubber.get_scrubber_for(text))
    verify(f"Hello on {text}", options=Options().with_scrubber(DateScrubber.get_scrubber_for(text)).inline())


def test_raises_error_if_regex_does_not_match_example():
    """
    Exception: Regex '\\d{2}/\\d{2}/\\d{4}' does not match example '2025-07-20'
    """
    def call():
        DateScrubber.add_scrubber("2025-07-20", "\\d{2}/\\d{2}/\\d{4}")
    verify_exception(call, options=Options().inline())

def test_handles_invalid_regex_patterns_gracefully():
    """
    Exception: Invalid regex pattern '[invalid-regex': unterminated character set at position 0
    """
    def call():
        DateScrubber.add_scrubber("2025-07-20", "[invalid-regex")
    verify_exception(call, options=Options().inline())


def test_gives_instructions_on_how_to_add_new_date_scrubber():
    """
    Exception: No match found for '07-20-2025'.
    Feel free to add your date at https://github.com/approvals/ApprovalTests.Python/issues/124
    Current supported formats are: 
        Tue May 13 16:30:00 | [a-zA-Z]{3} [a-zA-Z]{3} \d{2} \d{2}:\d{2}:\d{2} 
        Wed Nov 17 22:28:33 EET 2021 | [a-zA-Z]{3} [a-zA-Z]{3} \d{2} \d{2}:\d{2}:\d{2} [a-zA-Z]{3,4} \d{4} 
        Tue May 13 2014 23:30:00.789 | [a-zA-Z]{3} [a-zA-Z]{3} \d{2} \d{4} \d{2}:\d{2}:\d{2}.\d{3} 
        Tue May 13 16:30:00 -0800 2014 | [a-zA-Z]{3} [a-zA-Z]{3} \d{2} \d{2}:\d{2}:\d{2} -\d{4} \d{4} 
        13 May 2014 23:50:49,999 | \d{2} [a-zA-Z]{3} \d{4} \d{2}:\d{2}:\d{2},\d{3} 
        May 13, 2014 11:30:00 PM PST | [a-zA-Z]{3} \d{2}, \d{4} \d{2}:\d{2}:\d{2} [a-zA-Z]{2} [a-zA-Z]{3} 
        23:30:00 | \d{2}:\d{2}:\d{2} 
        2014/05/13 16:30:59.786 | \d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}.\d{2}\d 
        2020-9-10T08:07Z | \d{4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{2}Z 
        2020-09-10T08:07:89Z | \d{4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{2}:\d{2}Z 
        2020-09-10T01:23:45.678Z | \d{4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{2}\:\d{2}\.\d{3}Z 
        2023-07-16 17:39:03.293919 | \d{4}-\d{1,2}-\d{1,2}(?:T| )\d{1,2}:\d{2}:\d{2}\.\d{6} 
        20210505T091112Z | \d{8}T\d{6}Z 
        Tue May 13 16:30:00 2014 | (Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s([0-3]?\d)\s([0-1]\d:[0-5]\d:[0-5]\d)\s(\d{4}) 
        2021-09-10T08:07:00+03:00 | \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2} 
        20250527_125703 | [12]\d{3}[01]\d[0-3]\d_[0-2]\d[0-5]\d[0-5]\d 
        2025-07-20 | \d{4}-\d{2}-\d{2} 
    This date format is not recognized: '07-20-2025'
    If you would like to use this format, please add it to the list of supported formats.
    You can do this by using:
         DateScrubber.add_scrubber("07-20-2025", "<your regex pattern>")
    for additional help, see: https://github.com/approvals/ApprovalTests.Python/blob/main/docs/how_to/add_scrubbers.md
    """
    def call():
        DateScrubber.get_scrubber_for("07-20-2025")
    verify_exception(call, options=Options().inline())


def test_unsupported_format() -> None:
    verify_exception(lambda: DateScrubber.get_scrubber_for("an unsupported format"))


def test_supported_formats_as_table() -> None:
    table = markdown_table.MarkdownTable.with_headers("Example Date", "Regex Pattern")
    supported_formats = DateScrubber.get_supported_formats()
    for date_regex, examples in supported_formats:
        table.add_rows(examples[0], date_regex)
    verify(table)
