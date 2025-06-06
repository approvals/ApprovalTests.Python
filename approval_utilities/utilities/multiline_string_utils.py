import textwrap
from typing import Optional

from approval_utilities.utilities.logger.simple_logger import SimpleLogger


def remove_indentation_from(text: Optional[str]) -> str:
    SimpleLogger.variable("text", text)
    if not text:
        return ""
    cleaned = textwrap.dedent(text + "|")
    if cleaned.startswith("\n"):
        cleaned = cleaned[1:]
    return cleaned[:-1]
