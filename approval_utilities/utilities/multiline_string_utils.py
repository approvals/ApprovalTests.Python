import textwrap


def remove_indentation_from(text: str | None) -> str:
    if not text:
        return ""
    cleaned = textwrap.dedent(text + "|")
    cleaned = cleaned.removeprefix("\n")
    return cleaned[:-1]
