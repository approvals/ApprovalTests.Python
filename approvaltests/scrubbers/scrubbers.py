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



def templates_regex_scrubber_with_lambda() -> Scrubber:
    '''
     This method exists as a convient way to get an example scrubber for you to use.
     To use this template, simply inline the method in your IDE.
    '''
    return  create_regex_scrubber("your pattern here: [a-zA-Z]+/d{4}", lambda t: f"<your replacement_{t}>");
def templates_regex_scrubber_with_replacement() -> Scrubber:
    '''
     This method exists as a convient way to get an example scrubber for you to use.
     To use this template, simply inline the method in your IDE.
    '''
    return  create_regex_scrubber("your pattern here: [a-zA-Z]+/d{4}", "<your replacement>");