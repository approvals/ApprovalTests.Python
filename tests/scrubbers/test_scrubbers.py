import datetime

from approvaltests.approvals import verify, verify_all, verify_as_json, verify_exception
from approvaltests.core.options import Options
from approvaltests.scrubbers import combine_scrubbers
from approvaltests.scrubbers.scrubbers import (
    create_line_scrubber,
    create_regex_scrubber,
    scrub_all_dates,
    scrub_all_guids,
)


def test_full_stack_scrubbing() -> None:
    verify_all(
        "expanding twos",
        [1, 2, 12, 21, 121, 131, 222],
        options=Options().with_scrubber(lambda t: t.replace("2", "two")),
    )


def test_date_scrubbing() -> None:
    date1 = str(datetime.datetime(year=2000, month=1, day=2))
    date2 = str(datetime.datetime(year=2000, month=1, day=3))
    date3 = str(datetime.datetime(year=2000, month=1, day=4))
    mydict = {"start": date1, "pause": date2, "resume": date2, "end": date3}
    verify_as_json(mydict, options=Options().with_scrubber(scrub_all_dates))


def test_regex() -> None:
    verify(
        'and then jane said "blah blah blah "',
        options=Options().with_scrubber(
            create_regex_scrubber("(blah )+", "[nonsense]")
        ),
    )


def test_invalid_argument_to_create_regex_scrubber() -> None:
    verify_exception(
        lambda: verify(
            'and then jane said "blah blah blah "',
            options=Options().with_scrubber(create_regex_scrubber("(blah )+", 1)),
        )
    )


def test_regex_by_lambda() -> None:
    verify(
        'and then jane said "blah blah blah "',
        options=Options().with_scrubber(
            create_regex_scrubber("(blah )+", lambda n: f"[nonsense_{n}]")
        ),
    )


def test_guid() -> None:
    guids = [
        "2fd78d4a-ad49-447d-96a8-deda585a9aa5",
        "2fd78d4a-1111-1111-1111-deda585a9aa5",
        "2fd78d4a-3333-3333-3333-deda585a9aa5",
        "2fd78d4a-ad49-447d-96a8-deda585a9aa5",
        "2fd78d4a-ad49-447d-96a8-deda585a9aa5 and text",
    ]
    verify_all("guids", guids, options=Options().with_scrubber(scrub_all_guids))


def test_combine_scrubbers() -> None:
    verify(
        f"blah {str(datetime.datetime(year=2000, month=1, day=2))} 2fd78d4a-ad49-447d-96a8-deda585a9aa5",
        options=Options().with_scrubber(
            combine_scrubbers(
                scrub_all_guids,
                scrub_all_dates,
                create_regex_scrubber("(blah )+", "[nonsense] "),
            )
        ),
    )


def test_line_scrubber() -> None:
    text = """
    line 1
    remove me
    line 2
    also remove me
    line 3
    """
    text_to_remove = "remove"

    verify(text, options=Options().with_scrubber(create_line_scrubber(text_to_remove)))
