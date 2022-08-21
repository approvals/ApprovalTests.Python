import datetime

from approvaltests import verify_all, Options, verify_as_json, verify
from approvaltests.scrubbers import combine_scrubbers
from approvaltests.scrubbers.scrubbers import (
    scrub_all_dates,
    create_regex_scrubber,
    scrub_all_guids,
)


def test_full_stack_scrubbing():
    verify_all(
        "expanding twos",
        [1, 2, 12, 21, 121, 131, 222],
        options=Options().with_scrubber(lambda t: t.replace("2", "two")),
    )


def test_date_scrubbing():
    date1 = str(datetime.datetime(year=2000, month=1, day=2))
    date2 = str(datetime.datetime(year=2000, month=1, day=3))
    date3 = str(datetime.datetime(year=2000, month=1, day=4))
    mydict = {"start": date1, "pause": date2, "resume": date2, "end": date3}
    verify_as_json(mydict, options=Options().with_scrubber(scrub_all_dates))


def test_regex():
    verify(
        'and then jane said "blah blah blah "',
        options=Options().with_scrubber(
            create_regex_scrubber("(blah )+", "[nonsense]")
        ),
    )


def test_regex_by_lambda():
    verify(
        'and then jane said "blah blah blah "',
        options=Options().with_scrubber(
            create_regex_scrubber("(blah )+", lambda n: f"[nonsense_{n}]")
        ),
    )


def test_guid():
    guids = [
        "2fd78d4a-ad49-447d-96a8-deda585a9aa5",
        "2fd78d4a-1111-1111-1111-deda585a9aa5",
        "2fd78d4a-3333-3333-3333-deda585a9aa5",
        "2fd78d4a-ad49-447d-96a8-deda585a9aa5",
        "2fd78d4a-ad49-447d-96a8-deda585a9aa5 and text",
    ]
    verify_all("guids", guids, options=Options().with_scrubber(scrub_all_guids))


def test_combine_scrubbers():
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
