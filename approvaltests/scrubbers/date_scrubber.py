import re
from datetime import datetime
from typing import List, Tuple

from approvaltests.scrubbers import create_regex_scrubber
from approvaltests.scrubbers.scrubbers import Scrubber


class DateScrubber:
    @staticmethod
    def _get_internal_formats() -> List[Tuple[str, List[str], List[str]]]:
        """Returns (datetime_format, parsing_examples, display_examples)."""
        return [
            ("%a %b %d %H:%M:%S", ["Tue May 13 16:30:00"], ["Tue May 13 16:30:00"]),
            (
                "%a %b %d %Y %H:%M:%S.%f",
                ["Tue May 13 2014 23:30:00.789000"],
                ["Tue May 13 2014 23:30:00.789"],
            ),
            (
                "%d %b %Y %H:%M:%S,%f",
                ["13 May 2014 23:50:49,999000"],
                ["13 May 2014 23:50:49,999"],
            ),
            ("%H:%M:%S", ["23:30:00"], ["23:30:00"]),
            (
                "%Y/%m/%d %H:%M:%S.%f",
                ["2014/05/13 16:30:59.786000"],
                ["2014/05/13 16:30:59.786"],
            ),
            ("%Y-%m-%dT%H:%M:%SZ", ["2020-09-10T08:07:00Z"], ["2020-09-10T08:07:00Z"]),
            (
                "%Y-%m-%dT%H:%M:%S.%fZ",
                ["2020-09-10T01:23:45.678000Z"],
                ["2020-09-10T01:23:45.678Z"],
            ),
            (
                "%Y-%m-%d %H:%M:%S.%f",
                ["2023-07-16 17:39:03.293919"],
                ["2023-07-16 17:39:03.293919"],
            ),
            (
                "%Y-%m-%dT%H:%M:%S.%f",
                ["2023-12-06T11:59:47.090226"],
                ["2023-12-06T11:59:47.090226"],
            ),
            ("%Y%m%dT%H%M%SZ", ["20210505T091112Z"], ["20210505T091112Z"]),
            (
                "%a %b %d %H:%M:%S %Y",
                ["Tue May 13 16:30:00 2014"],
                ["Tue May 13 16:30:00 2014", "Wed Dec 11 14:59:44 2024"],
            ),
            (
                "%Y-%m-%dT%H:%M:%S%z",
                ["2021-09-10T08:07:00+0300"],
                ["2021-09-10T08:07:00+03:00", "2021-01-01T00:00:00+00:00"],
            ),
            ("%Y%m%d_%H%M%S", ["20250527_125703"], ["20250527_125703"]),
        ]

    @staticmethod
    def get_supported_formats() -> List[Tuple[str, List[str]]]:
        """Returns regex patterns and example dates for external API compatibility."""
        formats = []
        for (
            date_format,
            parsing_examples,
            display_examples,
        ) in DateScrubber._get_internal_formats():
            scrubber = DateScrubber.from_format(date_format)
            regex_pattern = scrubber.date_regex
            formats.append((regex_pattern, display_examples))
        return formats

    def __init__(self, date_regex: str):
        self.date_regex = date_regex

    @classmethod
    def from_format(cls, date_format: str) -> "DateScrubber":
        """Create a DateScrubber from a datetime format string like '%Y%m%d_%H%M%S'."""
        instance = cls.__new__(cls)
        instance.date_format = date_format
        instance.date_regex = instance._convert_format_to_regex(date_format)
        return instance

    def _convert_format_to_regex(self, date_format: str) -> str:
        """Convert datetime format string to a regex pattern for scrubbing."""
        format_to_regex = {
            "%a": r"[A-Za-z]{3}",  # Abbreviated weekday
            "%A": r"[A-Za-z]+",  # Full weekday
            "%b": r"[A-Za-z]{3}",  # Abbreviated month
            "%B": r"[A-Za-z]+",  # Full month
            "%d": r"\d{2}",  # Day of month (01-31)
            "%H": r"\d{2}",  # Hour (00-23)
            "%I": r"\d{2}",  # Hour (01-12)
            "%m": r"\d{2}",  # Month (01-12)
            "%M": r"\d{2}",  # Minute (00-59)
            "%p": r"[AP]M",  # AM/PM
            "%S": r"\d{2}",  # Second (00-59)
            "%Y": r"\d{4}",  # Year (4 digits)
            "%y": r"\d{2}",  # Year (2 digits)
            "%Z": r"[A-Z]{3,4}",  # Timezone abbreviation
            "%z": r"[+\-]\d{4}",  # Timezone offset
            "%f": r"\d{6}",  # Microsecond (6 digits)
        }

        # Replace format codes with regex patterns first
        regex_pattern = date_format
        for format_code, regex in format_to_regex.items():
            regex_pattern = regex_pattern.replace(format_code, f"__{format_code[1:]}__")

        # Escape special regex characters in the remaining format
        regex_pattern = re.escape(regex_pattern)

        # Replace placeholders with actual regex patterns
        for format_code, regex in format_to_regex.items():
            placeholder = f"__{format_code[1:]}__"
            escaped_placeholder = re.escape(placeholder)
            regex_pattern = regex_pattern.replace(escaped_placeholder, regex)

        return regex_pattern

    def scrub(self, date_str: str) -> str:
        return create_regex_scrubber(self.date_regex, lambda t: f"<date{t}>")(date_str)

    @staticmethod
    def get_scrubber_for_format(date_format: str) -> Scrubber:
        """Create a scrubber using a datetime format string like '%Y%m%d_%H%M%S'."""
        scrubber = DateScrubber.from_format(date_format)
        return scrubber.scrub

    @staticmethod
    def get_scrubber_for(example: str) -> Scrubber:
        # Build error message with regex patterns for external display
        supported = ""
        for date_regex, examples in DateScrubber.get_supported_formats():
            supported += f"    {examples[0]} | {date_regex} \n"

        # Try to parse with internal datetime formats
        for (
            date_format,
            parsing_examples,
            display_examples,
        ) in DateScrubber._get_internal_formats():
            try:
                datetime.strptime(example, date_format)
                scrubber = DateScrubber.from_format(date_format)
                return scrubber.scrub
            except ValueError:
                continue

        raise Exception(
            f"No match found for '{example}'.\n Feel free to add your date at https://github.com/approvals/ApprovalTests.Python/issues/124 \n Current supported formats are: \n{supported}"
        )
