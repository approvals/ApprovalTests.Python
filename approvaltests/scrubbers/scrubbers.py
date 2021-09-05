import re
from collections import defaultdict
from typing import Callable, Optional, Union, DefaultDict

Scrubber = Callable[[str],str]

def create_regex_scrubber(
    regex: str, function_or_replace_string: Union[Callable[[int], str], str]
) -> Scrubber:
    def scrub(text: str) -> str:
        if isinstance(function_or_replace_string, str):
             callable = lambda _: function_or_replace_string
        else:
            callable = function_or_replace_string

        matches = defaultdict(lambda: len(matches)) # type: DefaultDict[str, int]
        return re.sub(regex, lambda m: callable(matches[m.group(0)]), text)

    return scrub


def scrub_all_dates(d: str) -> str:
    return create_regex_scrubber(
        r"\d{4}-\d{2}-\d{2}\ \d{2}:\d{2}:\d{2}", lambda t: f"<date{t}>"
    )(d)


def scrub_all_guids(data: str) -> str:
    return create_regex_scrubber(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", lambda t: f"<guid_{t}>"

    )(data)