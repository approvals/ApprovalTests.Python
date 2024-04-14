from approvaltests import Options, verify_all
from approvaltests.inline.parse import Parse


def test_single_strings():
    """
    Sam -> SAM
    Llewellyn -> LLEWELLYN
    """
    parse = Parse.doc_string()
    verify_all(
        "",
        parse.get_inputs(),
        lambda s: f"{s} -> {s.upper()}",
        options=Options().inline(),
    )
    parse.verify_all(lambda s: s.upper())


def test_with_types_transformers_and_both():
    """
    1 -> 0b1
    9 -> 0b1001
    """
    parse = Parse.doc_string()
    verify_all(
        "",
        parse.get_inputs(),
        lambda s: f"{s} -> {bin(int(s))}",
        options=Options().inline(),
    )
    parse.transform(lambda a: int(a)).verify_all(lambda i: bin(i))


# parse.transform(int).transform(str).transform(int).verify_all(lambda i: bin(i), options= Options().with_reporter(ReporterThatAutomaticallyApproves())


def test_with_2_types_transformers_and_both():
    """
    1, 5.0 -> 5.0
    4, 0.5 -> 2.0
    """
    parse = Parse.doc_string(auto_approve=True)
    parse.transform2(int, float).verify_all(lambda i, f: i * f)
    parse.transform2(str, str).transform2(int, float).verify_all(lambda i, f: i * f)


def test_example_step_1():
    # begin-snippet: parse_input_step_2
    """
    Kody -> 0
    """

    # end-snippet
    # begin-snippet: parse_input_step_1
    def count_vowels(s: str) -> int:
        return 0

    def test_count_vowels():
        """
        Kody
        """
        parse = Parse.doc_string(auto_approve=True)
        parse.verify_all(count_vowels)

    # end-snippet
    test_count_vowels()


def test_example_step_2():
    """
    Kody -> 1
    Teresa -> 3
    Green -> 2
    """

    # begin-snippet: parse_input_step_3
    def count_vowels(s: str) -> int:
        return sum(1 for c in s if c in "aeo")

    def test_count_vowels():
        """
        Kody -> 1
        Teresa -> 3
        Green -> 2
        """
        parse = Parse.doc_string(auto_approve=True)
        parse.verify_all(count_vowels)

    # end-snippet
    test_count_vowels()


# begin-snippet: parse_input_transformation
def test_with_transformation():
    """
    1 -> 0b1
    9 -> 0b1001
    """
    parse = Parse.doc_string(auto_approve=True)
    parse.transform(int).verify_all(bin)


# end-snippet


# begin-snippet: parse_input_two_parameters
def test_with_two_parameters():
    """
    a, 3 -> aaa
    !, 7 -> !!!!!!!
    """
    parse = Parse.doc_string(auto_approve=True)
    parse.transform2(str, int).verify_all(lambda s, i: s * i)


# end-snippet


# long-term intention: get the test to fail, randomSauce is incorrect
def test_with_3_parameters():
    """
    a, 3, 1 -> aaaa
    """

    counter = 0

    def to(tin: type, tout: type):
        def wrapped(input):
            nonlocal counter
            counter += 1
            assert type(input) is tin
            return tout(input)

        return wrapped

    parse = Parse.doc_string(auto_approve=True)
    parse.transform3(to(str, str), to(str, str), to(str, str)).transform3(
        to(str, str), to(str, int), to(str, int)
    ).verify_all(lambda a, b, c: to(str, str)(a) * (to(int, int)(b) + to(int, int)(c)))

    assert counter == 9


# assert on all the paramaters
