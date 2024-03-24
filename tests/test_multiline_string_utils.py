from approvaltests import verify
from approval_utilities.utilities.multiline_string_utils import remove_indentation_from


def test_remove_indentation_from_works_perfectly() -> None:
    text = remove_indentation_from(
        """

        ^^ Blank line above ^^

        Here is some text
          1. with some indentation
          2. and more
            a. even more
          3. little less

        VV Blank line Below VV 

        """
    )
    verify("remove_indentation_from\n" + text)


def test_remove_indentation_uses_the_last_line_as_max_whitespace():
    input = """
        4 whitespaces
    """
    assert "    4 whitespaces\n" == remove_indentation_from(input)


def test_trailing_whitespace():
    input = """
    4 trailing whitespaces    
    """
    assert "4 trailing whitespaces    \n" == remove_indentation_from(input)
