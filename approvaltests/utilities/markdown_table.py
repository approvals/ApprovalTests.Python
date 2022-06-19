from typing import Any, Callable, Iterable


from approvaltests.core.verifiable import Verifiable
from approvaltests.core.options import  Options
from approvaltests.core.verify_parameters import VerifyParameters



class MarkdownTable(Verifiable):
    def get_verify_parameters(self, options: Options) -> VerifyParameters:
        return VerifyParameters(options.for_file.with_extension(".md"))

    @staticmethod
    def with_headers(*column_names: str) -> "MarkdownTable":
        table = MarkdownTable()
        table.add_rows(*column_names)
        dividers = map(lambda _: "---", column_names)
        table.markdown += MarkdownTable.print_row(*dividers)
        return table

    def add_rows(self, *column_names):
        self.markdown = MarkdownTable.print_row(*column_names)

    def __str__(self):
        return self.markdown

    @staticmethod
    def print_row(*column_names: Any) -> str:
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