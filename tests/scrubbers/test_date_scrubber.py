from approval_utilities.utilities import markdown_table
from approvaltests import Options, verify, verify_exception
from approvaltests.scrubbers.date_scrubber import DateScrubber


def test_supported_formats() -> None:
    internal_formats = DateScrubber._get_internal_formats()
    for date_format, parsing_examples, display_examples in internal_formats:
        for example in parsing_examples:
            assert DateScrubber(date_format).scrub(example) == "<date0>"


def test_supported_formats_arbitrary_string() -> None:
    assert (
        DateScrubber("%a %b %d %H:%M:%S").scrub("arbitrary string")
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
