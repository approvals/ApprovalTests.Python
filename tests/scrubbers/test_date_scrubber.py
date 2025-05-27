from approval_utilities.utilities import markdown_table
from approvaltests import Options, verify, verify_exception
from approvaltests.scrubbers.date_scrubber import DateScrubber


def test_supported_formats() -> None:
    internal_formats = DateScrubber._get_internal_formats()
    for date_format, parsing_examples, display_examples in internal_formats:
        for example in parsing_examples:
            assert DateScrubber.from_format(date_format).scrub(example) == "<date0>"


def test_supported_formats_arbitrary_string() -> None:
    assert (
        DateScrubber.from_format("%a %b %d %H:%M:%S").scrub("arbitrary string")
        == "arbitrary string"
    )


def test_supported_format_example() -> None:
    # begin-snippet: scrub-date-example
    verify(
        "created at 03:14:15",
        options=Options().with_scrubber(DateScrubber.get_scrubber_for("00:00:00")),
    )
    # end-snippet


def test_unsupported_format() -> None:
    verify_exception(lambda: DateScrubber.get_scrubber_for("an unsupported format"))


def test_supported_formats_as_table() -> None:
    table = markdown_table.MarkdownTable.with_headers("Example Date", "Regex Pattern")
    supported_formats = DateScrubber.get_supported_formats()
    for date_regex, examples in supported_formats:
        table.add_rows(examples[0], date_regex)
    verify(table)


def test_get_scrubber_for_format() -> None:
    """Test the new API that accepts datetime format strings directly."""
    # Test common datetime format patterns
    test_cases = [
        ("%Y%m%d_%H%M%S", "20250527_125703", "Log: 20250527_125703 - System started"),
        (
            "%Y-%m-%dT%H:%M:%SZ",
            "2021-01-01T12:34:56Z",
            "Timestamp: 2021-01-01T12:34:56Z end",
        ),
        ("%H:%M:%S", "23:59:59", "Time is 23:59:59 now"),
        (
            "%a %b %d %H:%M:%S %Y",
            "Mon Jan 01 12:00:00 2024",
            "Event: Mon Jan 01 12:00:00 2024",
        ),
    ]

    results = []
    for format_pattern, test_date, test_string in test_cases:
        scrubber = DateScrubber.get_scrubber_for_format(format_pattern)
        result = scrubber(test_string)
        results.extend((
            f"Format: {format_pattern}",
            f"Input:  {test_string}",
            f"Output: {result}",
            "",  # Empty line for readability
        ))

    verify("\n".join(results))


def test_get_scrubber_for_format_with_options() -> None:
    """Test the new API works with Options pattern like existing scrubbers."""
    verify(
        "Event logged at 20250527_125703 by system",
        options=Options().with_scrubber(
            DateScrubber.get_scrubber_for_format("%Y%m%d_%H%M%S")
        ),
    )
