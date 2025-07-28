# Scrubbers

[What is a scrubber](https://github.com/approvals/ApprovalTests.cpp/blob/master/doc/explanations/Scrubbers.md)

## How Tos

* [Scrub Dates](../how_to/scrub_dates.md)

## Adding Custom Date Scrubbers

For date formats not natively supported by ApprovalTests, you can add your own custom date scrubbers using `DateScrubber.add_scrubber()`. This is particularly useful when working with custom or less common date formats.

### Basic Usage

```python
from approvaltests import Options, verify
from approvaltests.scrubbers.date_scrubber import DateScrubber

# Add a custom date scrubber
DateScrubber.add_scrubber(
    "2025-07-20",               # Example date string
    r"\d{4}-\d{2}-\d{2}"        # Regex pattern to match
)

# Use the scrubber in your tests
verify(
    "Date: 2025-07-20",
    options=Options().with_scrubber(
        DateScrubber.get_scrubber_for("2025-07-20")
    )
)
```

### How It Works

1. `DateScrubber.add_scrubber(example, regex)`
   - `example`: A string example of the date format you want to scrub
   - `regex`: The regular expression pattern that matches your date format
   - The method validates that the regex matches the example and that the regex is valid

2. The scrubber will replace any matching dates with placeholders like `<date0>`, `<date1>`, etc.

### Example with Multiple Formats

```python
# Add multiple custom date formats
formats = [
    ("2025/07/20", r"\d{4}/\d{2}/\d{2}"),
    ("20-Jul-2025", r"\d{2}-[A-Za-z]{3}-\d{4}")
]

for example, pattern in formats:
    DateScrubber.add_scrubber(example, pattern)

# Now both formats will be scrubbed
verify(
    "Dates: 2025/07/20 and 20-Jul-2025",
    options=Options().with_scrubber(
        DateScrubber.get_scrubber_for("2025/07/20")
    )
)
```

### Notes

- The scrubber is added globally and will be available for all subsequent tests
- The order of adding scrubbers matters - the first matching pattern will be used
- For complex date formats, make sure your regex is specific enough to avoid false positives

### Helpful Resources

- View all [supported date formats](https://github.com/approvals/ApprovalTests.Python/blob/main/docs/DateScrubber.md)
- Test and create regex patterns at [regex101.com](https://regex101.com/)
- Need help with a specific date format? Check the [date scrubber documentation](https://github.com/approvals/ApprovalTests.Python/blob/main/docs/how_to/scrub_dates.md)
- For additional help or to request new date scrubbers, [visit this issue](https://github.com/approvals/ApprovalTests.Python/issues/124)

