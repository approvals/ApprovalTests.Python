import textwrap


def remove_indentation_from(text: str) -> str:
    if not text:
        return ""
    cleaned = textwrap.dedent(text)
    if cleaned.startswith("\n"):
        cleaned = cleaned[1:]
    return cleaned
