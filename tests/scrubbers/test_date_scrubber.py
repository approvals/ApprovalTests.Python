from pytest import CaptureFixture

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


def test_adds_valid_date_scrubber() -> None:
    """
    Hello on <date0>
    """
    text = "02025-007-020"
    try:
        DateScrubber.add_scrubber(text, r"\d{5}-\d{3}-\d{3}", display_message=False)
        verify(
            f"Hello on {text}",
            options=Options()
            .with_scrubber(DateScrubber.get_scrubber_for(text))
            .inline(),
        )
    finally:
        DateScrubber._clear_custom_scrubbers()  # Clean up after test, even if it fails


def test_raises_error_if_regex_does_not_match_example() -> None:
    """
    Exception: Regex '\d{2}/\d{2}/\d{4}' does not match example '2025-07-20'
    """

    def call() -> None:
        DateScrubber.add_scrubber("2025-07-20", r"\d{2}/\d{2}/\d{4}")

    verify_exception(call, options=Options().inline())


def test_handles_invalid_regex_patterns_gracefully() -> None:
    """
    Exception: Invalid regex pattern '[invalid-regex': unterminated character set at position 0
    """

    def call() -> None:
        DateScrubber.add_scrubber("2025-07-20", "[invalid-regex")

    verify_exception(call, options=Options().inline())


def test_unsupported_format() -> None:
    verify_exception(
        lambda: DateScrubber.get_scrubber_for("AN_UNSUPPORTED_DATE_FORMAT")
    )


def test_custom_date_format_example() -> None:
    # begin-snippet: custom_date_format_example
    from approvaltests.scrubbers.date_scrubber import DateScrubber

    # Add a custom date format
    DateScrubber.add_scrubber("2025-07-20", r"\d{4}-\d{2}-\d{2}", display_message=False)

    # Now you can use it in your tests
    verify(
        "Event scheduled for 2025-07-20",
        options=Options().with_scrubber(DateScrubber.get_scrubber_for("2025-07-20")),
    )
    # end-snippet
    # Clean up after test
    DateScrubber._clear_custom_scrubbers()


def test_supported_formats_as_table() -> None:
    table = markdown_table.MarkdownTable.with_headers("Example Date", "Regex Pattern")
    supported_formats = DateScrubber.get_supported_formats()
    for date_regex, examples in supported_formats:
        table.add_rows(examples[0], date_regex)
    verify(table)


def test_custom_scrubber_displays_message(capsys: CaptureFixture[str]) -> None:
    """
    You are using a custom date scrubber. If you think the format you want to scrub would be useful for others, please add it to https://github.com/approvals/ApprovalTests.Python/issues/124.

    To suppress this message, use
        DateScrubber.add_scrubber("2023-Dec-25", "\d{4}-[A-Za-z]{3}-\d{2}", display_message=False)

    """
    try:
        DateScrubber.add_scrubber("2023-Dec-25", r"\d{4}-[A-Za-z]{3}-\d{2}")
        captured = capsys.readouterr()
        verify(captured.out, options=Options().inline())
    finally:
        DateScrubber._clear_custom_scrubbers()


def test_custom_scrubber_message_can_be_suppressed(capsys: CaptureFixture[str]) -> None:
    """ """
    try:
        DateScrubber.add_scrubber(
            "2023-Dec-25", r"\d{4}-[A-Za-z]{3}-\d{2}", display_message=False
        )
        captured = capsys.readouterr()
        verify(captured.out, options=Options().inline())
    finally:
        DateScrubber._clear_custom_scrubbers()
