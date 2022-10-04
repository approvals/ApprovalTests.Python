# How to scrub dates

toc

### How to do it

The easiest way to scrub a date is by calling 
<!-- snippet: scrub-date-example -->
<a id='snippet-scrub-date-example'></a>
```java
Approvals.verify("created at 03:14:15", new Options().withScrubber(DateScrubber.getScrubberFor("00:00:00")));
```
<sup><a href='/approvaltests-tests/src/test/java/org/approvaltests/scrubbers/DateScrubberTest.java#L46-L48' title='Snippet source file'>snippet source</a> | <a href='#snippet-scrub-date-example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

which will produce

<!-- snippet: test_date_scrubber.test_supported_format_example.approved.txt -->
<a id='snippet-DateScrubberTest.exampleForDocumentation.approved.txt'></a>
```txt
created at [Date1]
```
<sup><a href='/approvaltests-tests/src/test/java/org/approvaltests/scrubbers/DateScrubberTest.exampleForDocumentation.approved.txt#L1-L1' title='Snippet source file'>snippet source</a> | <a href='#snippet-DateScrubberTest.exampleForDocumentation.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Supported formats

<!-- include: test_date_scrubber.test_supported_formats.approved.md -->
| Example Date | RegEx Pattern |
| :-------------------- | :----------------------- | 
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
| 20210505T091112Z | \d{8}T\d{6}Z |
<!-- endInclude -->

## Scrubbing multiple parts of a string

If you need to do scrubbing of multiple things, the easiest way is to create multiple scrubbers and then combine them.
