from approvaltests import verify_all, Options


def test_full_stack_scrubbing():
    verify_all('expanding twos', [1, 2, 12, 21, 121, 131, 222],
               options=Options().with_scrubber(lambda t: t.replace('2', 'two')))
