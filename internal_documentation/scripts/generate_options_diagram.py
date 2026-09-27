import html
import re
from pathlib import Path

_SCRIPT_DIR = Path(__file__).parent
_REPO_ROOT = _SCRIPT_DIR.parent.parent
assert _REPO_ROOT.joinpath(".gitattributes").exists()

_SOURCE_PATH = _REPO_ROOT / "tests" / "test_options.py"
_DIAGRAM_PATH = _REPO_ROOT / "docs" / "images" / "options_diagram.html"

_BEGIN_SNIPPET_MARKER = "# begin-snippet: options_with_all_options"
_END_SNIPPET_MARKER = "# end-snippet"

_GENERATED_BEGIN = "<!-- GENERATED:CODE:BEGIN"
_GENERATED_END = "<!-- GENERATED:CODE:END -->"

# (marker substring that starts the stripped line, css color variable, data-option)
# data-option of None means: box it, but it isn't one of the hoverable options.
_BOX_RULES = [
    ("Options()", "c-core", None),
    (".for_file.with_extension(", "c-extension", "extension"),
    (".with_scrubber(", "c-scrubber", "scrubber"),
    (".add_scrubber(", "c-add-scrubber", "add-scrubber"),
    (".with_namer(", "c-namer", "namer"),
    (".with_comparator(", "c-comparator", "comparator"),
    (".with_reporter(", "c-reporter", "reporter"),
]

_KEYWORDS = ["lambda", "None", "return", "True", "False"]


def _highlight(text: str) -> str:
    escaped = html.escape(text, quote=False)

    strings: list[str] = []

    def _stash_string(match: re.Match[str]) -> str:
        strings.append(match.group(0))
        return f"\x00STR{len(strings) - 1}\x00"

    escaped = re.sub(r'"[^"]*"', _stash_string, escaped)

    escaped = re.sub(
        r"\bdef (\w+)",
        r'<span class="kw">def</span> <span class="fn">\1</span>',
        escaped,
    )
    escaped = re.sub(
        r"\bclass (\w+)",
        r'<span class="kw">class</span> <span class="fn">\1</span>',
        escaped,
    )
    for keyword in _KEYWORDS:
        escaped = re.sub(
            rf"\b{keyword}\b", f'<span class="kw">{keyword}</span>', escaped
        )

    for index, string_literal in enumerate(strings):
        escaped = escaped.replace(
            f"\x00STR{index}\x00",
            f'<span class="str">{html.escape(string_literal, quote=False)}</span>',
        )

    return escaped


def _render_line(line_number: int, raw_line: str) -> str:
    stripped = raw_line.lstrip(" ")
    indent = len(raw_line) - len(stripped)
    prefix = "&nbsp;" * indent
    content = stripped.rstrip("\n")

    if content == "":
        body = ""
    elif content.startswith("#"):
        body = f'<span class="com">{html.escape(content, quote=False)}</span>'
    elif content.startswith("verify("):
        body = f'<span class="hover-target" data-option="verdict">{_highlight(content)}</span>'
    else:
        body = _highlight(content)
        for marker, color, option in _BOX_RULES:
            if content.startswith(marker):
                classes = "box-line hover-target" if option else "box-line"
                option_attr = f' data-option="{option}"' if option else ""
                body = (
                    f'<span class="{classes}"{option_attr} '
                    f'style="border-color:var(--{color});">{body}</span>'
                )
                break

    return f'<div class="code-line"><span class="num">{line_number}</span>{prefix}{body}</div>'


def _extract_snippet(lines: list[str]) -> tuple[int, list[str]]:
    begin_index = next(
        i for i, line in enumerate(lines) if _BEGIN_SNIPPET_MARKER in line
    )
    def_index = next(
        i for i in range(begin_index, -1, -1) if lines[i].lstrip().startswith("def ")
    )
    end_index = next(
        i for i in range(begin_index, len(lines)) if _END_SNIPPET_MARKER in lines[i]
    )
    return def_index + 1, lines[def_index : end_index + 1]


def main() -> None:
    source_lines = _SOURCE_PATH.read_text().splitlines(keepends=True)
    first_line_number, snippet_lines = _extract_snippet(source_lines)

    rendered = "\n".join(
        _render_line(first_line_number + offset, line)
        for offset, line in enumerate(snippet_lines)
    )

    diagram_html = _DIAGRAM_PATH.read_text()
    begin_marker_end = (
        diagram_html.index("-->", diagram_html.index(_GENERATED_BEGIN)) + 3
    )
    end_marker_start = diagram_html.index(_GENERATED_END)

    new_diagram_html = (
        diagram_html[:begin_marker_end]
        + "\n"
        + rendered
        + "\n"
        + diagram_html[end_marker_start:]
    )
    _DIAGRAM_PATH.write_text(new_diagram_html)

    print(f"Wrote {len(snippet_lines)} lines to {_DIAGRAM_PATH}")


if __name__ == "__main__":
    main()
