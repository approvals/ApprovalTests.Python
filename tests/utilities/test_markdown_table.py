from typing import Any, Callable, Iterable

from numpy.core.defchararray import upper

from approvaltests import verify, Verifiable, Options
from approvaltests.core.verify_parameters import VerifyParameters


class MarkdownTable(Verifiable):
    def get_verify_parameters(self, options: Options) -> VerifyParameters:
        return VerifyParameters(options.for_file.with_extension(".md"))

    @staticmethod
    def with_headers(*column_names: str) -> "MarkdownTable":
        table = MarkdownTable()
        table.markdown = MarkdownTable.print_row(*column_names)
        dividers = map(lambda _: "---", column_names)
        table.markdown += MarkdownTable.print_row(*dividers)
        return table

    def __str__(self):
        return self.markdown

    @staticmethod
    def print_row(*column_names: Any):
        row = "|"
        for column in column_names:
            row += f" {column} |"
        return row + "\n"

    def add_rows_for_inputs(self, inputs: Iterable[Any], *varargs: Callable[[Any], Any]) -> "MarkdownTable":
        for input in inputs:
            #Create a list with the input and all the conversions, using varargs.map
            row = [input]
            row += map(lambda callable: callable(input), varargs)
            self.markdown += MarkdownTable.print_row(*row)
        pass


def test_markdown_table():
    '''
    String[] inputs = {"verify json", "verify all", "verify parameters", "verify as json"};
MarkdownTable table = MarkdownTable.withHeaders("Input", "Camel Case", "Snake Case", "Kebab Case");
table.addRowsForInputs(inputs, this::toCamelCase, this::toSnakeCase, this::toKebabCase);
Approvals.verify(table);
    '''
    inputs = ["verify json", "verify all", "verify parameters", "verify as json"]
    table = MarkdownTable.with_headers("Input", "Camel Case", "Snake Case", "Kebab Case")
    table.add_rows_for_inputs(inputs, to_camel_case, to_snake_case, to_kebab_case)
    verify(table)

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