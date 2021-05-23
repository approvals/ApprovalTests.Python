import re
from collections import defaultdict
from typing import Callable


def scrub_with_regex(
    regex: str, callable: Callable[[int], str]
) -> Callable[[str], str]:
    def scrub(text: str) -> str:
        matches = defaultdict(lambda: len(matches))
        return re.sub(regex, lambda m: callable(matches[m.group(0)]), text)

    return scrub


def scrub_all_dates(d: str) -> str:
    return scrub_with_regex(
        r"\d{4}-\d{2}-\d{2}\ \d{2}:\d{2}:\d{2}", lambda t: f"<date{t}>"
    )(d)
