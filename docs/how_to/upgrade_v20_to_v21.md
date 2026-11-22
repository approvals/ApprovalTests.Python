<a id="top"></a>

# Upgrade from 20.0.1 to 21.0.0

21.0.0 has two breaking changes so far: custom `Writer` subclasses need two more methods, and `TemplatedCustomNamer.namer_parts` is gone.
Approved files keep their names. You do not need to re-approve anything.

## For AI coding agents

Apply the sections below in order. For each section:

1. Run its search command from the root of the project.
2. Rewrite each match as shown in **After**.
3. Run the tests. They should pass without new `.received.` files.

## Contents

1. [Custom Writer subclasses](#custom-writer-subclasses)
2. [TemplatedCustomNamer.namer_parts](#templatedcustomnamernamer_parts)
3. [Coming in this release (still in progress)](#coming-in-this-release-still-in-progress)

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

## Coming in this release (still in progress)

- The extension will come from the writer. A namer built with its own extension, such as `StackFrameNamer(".json")`, will no longer control the extension.
- Most namers will become a `TemplatedCustomNamer`.

---

[Back to User Guide](../README.md#top)
