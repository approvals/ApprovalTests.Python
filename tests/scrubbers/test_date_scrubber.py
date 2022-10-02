from approvaltests import Options, verify, verify_exception
from approvaltests.scrubbers.date_scrubber import DateScrubber


def test_supported_formats():
    supported_formats = DateScrubber.get_supported_formats()
    for date_regex, examples in supported_formats:
        for example in examples:
            assert DateScrubber(date_regex).scrub(example) == "<date0>"


def test_supported_formats_arbitrary_string():
    assert DateScrubber("[a-zA-Z]{3} [a-zA-Z]{3} \\d{2} \\d{2}:\\d{2}:\\d{2}").scrub(
        "arbitrary string") == "arbitrary string"


def test_supported_format_example() -> None:
    verify("created at 03:14:15", options=Options().with_scrubber(DateScrubber.get_scrubber_for("00:00:00")))


def test_unsupported_format() -> None:
    verify_exception(lambda: DateScrubber.get_scrubber_for("an unsupported format"))