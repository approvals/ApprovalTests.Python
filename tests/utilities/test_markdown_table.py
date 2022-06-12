from collections.abc import Sequence
from typing import Any

from approvaltests import verify, Verifiable, Options
from approvaltests.core.verify_parameters import VerifyParameters


class MarkdownTable(Verifiable):
    def get_verify_parameters(self, options: Options) -> VerifyParameters:
        return VerifyParameters(options.for_file.with_extension(".md"))

    @staticmethod
    def with_headers(*column_names: str) -> "MarkdownTable":
        table = MarkdownTable()
        table.markdown = MarkdownTable.print_row(*column_names)
        dividers = map(lambda _ :"---", column_names)
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


def test_markdown_table():
    '''
    String[] inputs = {"verify json", "verify all", "verify parameters", "verify as json"};
MarkdownTable table = MarkdownTable.withHeaders("Input", "Camel Case", "Snake Case", "Kebab Case");
table.addRowsForInputs(inputs, this::toCamelCase, this::toSnakeCase, this::toKebabCase);
Approvals.verify(table);
    '''
    inputs = ["verify json", "verify all", "verify parameters", "verify as json"]
    table = MarkdownTable.with_headers("Input", "Camel Case", "Snake Case", "Kebab Case")
    verify(table)