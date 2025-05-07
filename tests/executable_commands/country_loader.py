from typing import Any, Iterable, List, Tuple

from typing_extensions import override

from approval_utilities.approvaltests.core.executable_command import ExecutableCommand
from approval_utilities.utilities.persistence.loader import Loader, T
from tests.executable_commands.country import Country


class CountryLoader(ExecutableCommand, Loader[List[Country]]):
    @override
    def load(self) -> List[Country]:
        pass

    @override
    def get_command(self) -> str:
        return "SELECT c.* FROM Country c"

    @override
    def execute_command(self, command: str) -> str:
        cursor, connection = self.connect_to_database()
        cursor.execute(command, ())
        column_names = [i[0] for i in cursor.description]
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return self.format_data_as_markdown_table(column_names, rows)

    def format_data_as_markdown_table(
        self, column_names: List[str], rows: List[List]
    ) -> str:
        def format_table_row(values: Iterable[Any]) -> str:
            return "| " + " | ".join(map(str, values)) + " |"

        headers = format_table_row(column_names)
        dashes = format_table_row(map(lambda a: "---", column_names))
        data = "\n".join(map(format_table_row, rows))
        return f"""{headers}
{dashes}
{data}"""

    def connect_to_database(self) -> Tuple[Any, Any]:
        import mariadb  # you need to uncomment this in the requirements.tests.txt

        conn = mariadb.connect(user="root", password="", port=3306, database="sakila")
        cursor = conn.cursor()
        return (cursor, conn)
