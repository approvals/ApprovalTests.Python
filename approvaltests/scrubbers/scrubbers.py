import re
from collections import defaultdict
from typing import Callable, Union, DefaultDict

Scrubber = Callable[[str], str]


def create_regex_scrubber(
    regex: str, function_or_replace_string: Union[Callable[[int], str], str]
) -> Scrubber:
    def scrub(text: str) -> str:
        if isinstance(function_or_replace_string, str):
            replacement_function = lambda _: function_or_replace_string
        else:
            replacement_function = function_or_replace_string

        matches = defaultdict(lambda: len(matches))  # type: DefaultDict[str, int]
        return re.sub(regex, lambda m: replacement_function(matches[m.group(0)]), text)

    return scrub


def scrub_all_dates(date: str) -> str:
    return create_regex_scrubber(
        r"\d{4}-\d{2}-\d{2}\ \d{2}:\d{2}:\d{2}", lambda t: f"<date{t}>"
    )(date)


def scrub_all_guids(data: str) -> str:
    return create_regex_scrubber(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        lambda t: f"<guid_{t}>",
    )(data)


def combine_scrubbers(*scrubbers):
    def combined(data: str) -> str:
        for scrubber in scrubbers:
            data = scrubber(data)
        return data

    return combined


def templates_regex_scrubber_with_lambda() -> Scrubber:
    """
    This method exists as a convenient way to get an example scrubber for you to use.
    To use this template, simply inline the method in your IDE.
    """
    return create_regex_scrubber(
        "your pattern here: [a-zA-Z]+/d{4}", lambda t: f"<your replacement_{t}>"
    )


def templates_regex_scrubber_with_replacement() -> Scrubber:
    """
    This method exists as a convient way to get an example scrubber for you to use.
    To use this template, simply inline the method in your IDE.
    """
    return create_regex_scrubber(
        "your pattern here: [a-zA-Z]+/d{4}", "<your replacement>"
    )
