from approvaltests.scrubbers.date_scrubber import DateScrubber


def test_supported_formats():
    supported_formats = DateScrubber.get_supported_formats()
    for date_regex, examples in supported_formats:
        for example in examples:
            assert DateScrubber(date_regex).scrub(example) == "<date0>"


def test_supported_formats_arbitrary_string():
    assert DateScrubber("[a-zA-Z]{3} [a-zA-Z]{3} \\d{2} \\d{2}:\\d{2}:\\d{2}").scrub(
        "arbitrary string") == "arbitrary string"
