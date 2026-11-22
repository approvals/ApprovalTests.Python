<a id="top"></a>

# Upgrade from 20.0.1 to 21.0.0

21.0.0 has three breaking changes so far: custom `Writer` subclasses need two more methods, `TemplatedCustomNamer.namer_parts` is gone, and `TemplatedCustomNamer` must be created inside a test.
Approved files keep their names. You do not need to re-approve anything.

## For AI coding agents

Apply the sections below in order. For each section:

1. Run its search command from the root of the project.
2. Rewrite each match as shown in **After**.
3. Run the tests. They should pass without new `.received.` files.

## Contents

1. [Custom Writer subclasses](#custom-writer-subclasses)
2. [TemplatedCustomNamer.namer_parts](#templatedcustomnamernamer_parts)
3. [Create TemplatedCustomNamer inside the test](#create-templatedcustomnamer-inside-the-test)
4. [Coming in this release (still in progress)](#coming-in-this-release-still-in-progress)

## Custom Writer subclasses

`Writer` (in `approvaltests/core/writer.py`) now has two more abstract methods:

- `get_file_extension_with_dot(self) -> str` returns the extension of the file, such as `".txt"`.
- `clean_up_received(self, received_file: str) -> None` removes the received file after a passing test. Usually this is `os.remove(received_file)`.

If your writer does not implement both, creating it raises `TypeError`.

Search:

```sh
rg -n "\(Writer\)" --type py
```

Before:

```py
from approvaltests.core.writer import Writer


class MyWriter(Writer):
    def write_received_file(self, received_file: str) -> str:
        with open(received_file, mode="w", encoding="utf-8") as file:
            file.write("my content\n")
        return received_file
```

After:

```py
import os

from typing_extensions import override

from approvaltests.core.writer import Writer


class MyWriter(Writer):
    @override
    def get_file_extension_with_dot(self) -> str:
        return ".txt"

    @override
    def clean_up_received(self, received_file: str) -> None:
        os.remove(received_file)

    @override
    def write_received_file(self, received_file: str) -> str:
        with open(received_file, mode="w", encoding="utf-8") as file:
            file.write("my content\n")
        return received_file
```

`StringWriter` in `approvaltests/string_writer.py` is a real example.

## TemplatedCustomNamer.namer_parts

`TemplatedCustomNamer` no longer holds a `StackFrameNamer`, so the `namer_parts` attribute is gone.

Search:

```sh
rg -n "namer_parts" --type py
```

| Before | After |
|---|---|
| `namer.namer_parts.config = {"subdirectory": "my_subdir"}` | `namer.approvals_subdirectory = "my_subdir"` |
| `namer.namer_parts.set_extension(".json")` | `namer.set_extension(".json")` |

## Create TemplatedCustomNamer inside the test

`TemplatedCustomNamer` now reads the test name from the call stack once, when it is created. Before, it read it each time it built a file name.
So create it inside the test function. A namer created at module level, or in a pytest fixture, no longer finds the test.

Search:

```sh
rg -n "TemplatedCustomNamer\(" --type py
```

Before:

```py
NAMER = TemplatedCustomNamer("{test_case_name}.{approved_or_received}.{file_extension}")


def test_something() -> None:
    verify("hello", options=Options().with_namer(NAMER))
```

After:

```py
def test_something() -> None:
    namer = TemplatedCustomNamer("{test_case_name}.{approved_or_received}.{file_extension}")
    verify("hello", options=Options().with_namer(namer))
```

## Coming in this release (still in progress)

- The extension will come from the writer. A namer built with its own extension, such as `StackFrameNamer(".json")`, will no longer control the extension.
- Most namers will become a `TemplatedCustomNamer`.

---

[Back to User Guide](../README.md#top)
