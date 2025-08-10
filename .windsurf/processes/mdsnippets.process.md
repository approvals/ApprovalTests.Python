# Markdown Snippets

STARTER_CHARACTER = ✍️

We use [MdSnippets](https://raw.githubusercontent.com/SimonCropp/MarkdownSnippets/refs/heads/main/readme.md) to generate markdown snippets from our code. 

ALL code blocks in documentation should be surrounded with `<!-- snippet: ... -->` and `<!-- endSnippet -->`.

If a code block is not surrounded with these tags, it should be extracted into a unit test and replace with a snippet.

## Steps

1. Identify any code block that is missing the snippet tags.
1. Check if the code or a reasonably similar example already exists in a unit test.
1. If the test code already has a snippet, reuse the snippet. 
1. If the test code doesn't have a snippet, add the snippet and use it.
1. If the code is not in an existing test, make a test add the code and the snippet.
1. If the test is purefuly for an example, start the name of the test with `test_...._example`.


## Snippet styles

Snippet names are all done in `snake_case`. They need to be unique.

