# How to scrub dates

<!-- toc -->
## Contents

  * [How to do it](#how-to-do-it)
  * [Adding custom date formats](#adding-custom-date-formats)
    * [Contributing Back:](#contributing-back)
  * [Supported formats](#supported-formats)<!-- endToc -->

## How to do it

The easiest way to scrub a date is by calling 
<!-- snippet: scrub-date-example -->
<a id='snippet-scrub-date-example'></a>
```py
verify(
    "created at 03:14:15",
    options=Options().with_scrubber(DateScrubber.get_scrubber_for("00:00:00")),
)
```
<sup><a href='/tests/scrubbers/test_date_scrubber.py#L25-L30' title='Snippet source file'>snippet source</a> | <a href='#snippet-scrub-date-example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

which will produce

<!-- snippet: test_date_scrubber.test_supported_format_example.approved.txt -->
<a id='snippet-test_date_scrubber.test_supported_format_example.approved.txt'></a>
```txt
created at <date0>
```
<sup><a href='/tests/scrubbers/test_date_scrubber.test_supported_format_example.approved.txt#L1-L1' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_date_scrubber.test_supported_format_example.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Adding custom date formats

If you encounter a date format that isn't supported by the built-in formats, you can easily add your own custom date scrubber using the `add_scrubber` method:

<!-- snippet: custom_date_format_example -->
<a id='snippet-custom_date_format_example'></a>
```py
from approvaltests.scrubbers.date_scrubber import DateScrubber

# Add a custom date format
DateScrubber.add_scrubber("2025-07-20", r"\d{4}-\d{2}-\d{2}", display_message=False)

# Now you can use it in your tests
verify(
    "Event scheduled for 2025-07-20",
    options=Options().with_scrubber(DateScrubber.get_scrubber_for("2025-07-20")),
)
```
<sup><a href='/tests/scrubbers/test_date_scrubber.py#L79-L90' title='Snippet source file'>snippet source</a> | <a href='#snippet-custom_date_format_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->
**Global scope**: Custom scrubbers are available globally once added

### Contributing Back:

If you think the format you want to scrub would be useful for others, please add it to https://github.com/approvals/ApprovalTests.Python/issues/124.


## Supported formats

<!-- include: test_date_scrubber.test_supported_formats_as_table.approved.md -->
| Example Date | Regex Pattern |
| --- | --- |
| Tue May 13 16:30:00 | [a-zA-Z]{3} [a-zA-Z]{3} \d{2} \d{2}:\d{2}:\d{2} |
| Wed Nov 17 22:28:33 EET 2021 | [a-zA-Z]{3} [a-zA-Z]{3} \d{2} \d{2}:\d{2}:\d{2} [a-zA-Z]{3,4} \d{4} |
| Tue May 13 2014 23:30:00.789 | [a-zA-Z]{3} [a-zA-Z]{3} \d{2} \d{4} \d{2}:\d{2}:\d{2}.\d{3} |
| Tue May 13 16:30:00 -0800 2014 | [a-zA-Z]{3} [a-zA-Z]{3} \d{2} \d{2}:\d{2}:\d{2} -\d{4} \d{4} |
| 13 May 2014 23:50:49,999 | \d{2} [a-zA-Z]{3} \d{4} \d{2}:\d{2}:\d{2},\d{3} |
| May 13, 2014 11:30:00 PM PST | [a-zA-Z]{3} \d{2}, \d{4} \d{2}:\d{2}:\d{2} [a-zA-Z]{2} [a-zA-Z]{3} |
| 23:30:00 | \d{2}:\d{2}:\d{2} |
| 2014/05/13 16:30:59.786 | \d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}.\d{2}\d |
| 2020-9-10T08:07Z | \d{4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{2}Z |
| 2020-09-10T08:07:89Z | \d{4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{2}:\d{2}Z |
| 2020-09-10T01:23:45.678Z | \d{4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{2}\:\d{2}\.\d{3}Z |
| 2023-07-16 17:39:03.293919 | \d{4}-\d{1,2}-\d{1,2}(?:T| )\d{1,2}:\d{2}:\d{2}\.\d{6} |
| 20210505T091112Z | \d{8}T\d{6}Z |
| Tue May 13 16:30:00 2014 | (Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s([0-3]?\d)\s([0-1]\d:[0-5]\d:[0-5]\d)\s(\d{4}) |
| 2021-09-10T08:07:00+03:00 | \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2} |
| 20250527_125703 | [12]\d{3}[01]\d[0-3]\d_[0-2]\d[0-5]\d[0-5]\d |
<!-- endInclude -->
