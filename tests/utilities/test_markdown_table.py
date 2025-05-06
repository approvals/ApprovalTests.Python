from approvaltests import verify
from approval_utilities.utilities.markdown_table import MarkdownTable


def test_markdown_table() -> None:
    # begin-snippet: markdown_table_example
    inputs = ["verify json", "verify all", "verify parameters", "verify as json"]
    table = MarkdownTable.with_headers(
        "Input", "Camel Case", "Snake Case", "Kebab Case"
    )
    table.add_rows_for_inputs(inputs, to_camel_case, to_snake_case, to_kebab_case)
    verify(table)
    # end-snippet


def to_camel_case(text: str) -> str:
    words = text.split()
    output = ""
    for w in words:
        output += w[0].capitalize() + w[1:]
    return output[0].lower() + output[1:]


def to_snake_case(text: str) -> str:
    return text.lower().replace(" ", "_")


def to_kebab_case(text: str) -> str:
    return text.lower().replace(" ", "-")
