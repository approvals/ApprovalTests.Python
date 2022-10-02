from approvaltests.scrubbers.date_scrubber import DateScrubber


def test_supported_formats():
    # assertEquals("[Date1]", dateScrubber.scrub(example()
    supported_formats = DateScrubber.get_supported_formats()
    date_regex, examples = supported_formats[0]
    assert DateScrubber(date_regex).scrub(examples[0]) == "<date0>"

def test_supported_formats_arbitrary_string():
    # assertEquals("[Date1]", dateScrubber.scrub(example()
    assert DateScrubber("[a-zA-Z]{3} [a-zA-Z]{3} \\d{2} \\d{2}:\\d{2}:\\d{2}").scrub(
        "arbitrary string") == "arbitrary string"


