<a id="top"></a>

# Upgrade from 20.0.1 to 21.0.0

21.0.0 has eight breaking changes so far: custom `Writer` subclasses need two more methods, `TemplatedCustomNamer.namer_parts` is gone, `TemplatedCustomNamer` must be created inside a test, `ScenarioNamer` is removed, `NamerBase` is removed, custom `Namer` subclasses need two more methods, the extension now comes from the writer, and `get_approved_filename`, `get_received_filename` and `set_extension` are removed.
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
4. [Custom templates with scenarios](#custom-templates-with-scenarios)
5. [ScenarioNamer is removed](#scenarionamer-is-removed)
6. [NamerBase is removed](#namerbase-is-removed)
7. [Custom Namer subclasses](#custom-namer-subclasses)
8. [The extension comes from the writer](#the-extension-comes-from-the-writer)
9. [get_approved_filename, get_received_filename and set_extension are removed](#get_approved_filename-get_received_filename-and-set_extension-are-removed)
10. [Coming in this release (still in progress)](#coming-in-this-release-still-in-progress)

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
| `namer.namer_parts.set_extension(".json")` | `namer.get_approved_file(".json")` (see [below](#get_approved_filename-get_received_filename-and-set_extension-are-removed)) |

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

## Custom templates with scenarios

A `ScenarioNamer` (used by `NamerFactory.with_parameters` and `get_scenario_namer`) wrapped around a `TemplatedCustomNamer` now uses that namer's own template. The scenario names go into `{additional_information}`.
If your template does not have `{additional_information}`, the scenario names are left out, and every scenario writes to the same file.

Search:

```sh
rg -n "TemplatedCustomNamer\(" --type py
```

Before:

```py
TemplatedCustomNamer("{test_case_name}.{approved_or_received}.{file_extension}")
```

After:

```py
TemplatedCustomNamer("{test_case_name}{additional_information}.{approved_or_received}.{file_extension}")
```

## ScenarioNamer is removed

`ScenarioNamer` (`approvaltests/core/scenario_namer.py`) is gone. Scenario names are now additional information on the default namer.

Search:

```sh
rg -n "ScenarioNamer|get_scenario_namer|with_parameters" --type py
```

| Before | After |
|---|---|
| `ScenarioNamer(get_default_namer(), "a", 2)` | `get_scenario_namer("a", 2)` (or `options=NamerFactory.with_parameters("a", 2)`) |
| `from approvaltests.core.scenario_namer import ScenarioNamer` | remove the import |

Two behaviors to know about:

- `NamerFactory.with_parameters(...)` no longer sets a namer. If you add `.with_namer(x)` after it, `x` wins and the parameters are ignored (like Java).
- `.namer.get_basename()` no longer includes the parameters.

## NamerBase is removed

`NamerBase` (`approvaltests/namer/namer_base.py`) is gone. `StackFrameNamer` and `PyTestNamer` now inherit `Namer` directly.

Search:

```sh
rg -n "NamerBase" --type py
```

Before:

```py
from approvaltests.namer.namer_base import NamerBase


class MyNamer(NamerBase):
    ...


def is_namer(x) -> bool:
    return isinstance(x, NamerBase)
```

After:

```py
from approvaltests.core.namer import Namer


class MyNamer(Namer):
    # implement get_approved_file and get_received_file yourself
    ...


def is_namer(x) -> bool:
    return isinstance(x, Namer)
```

Or subclass `StackFrameNamer` if you want the default naming.

## Custom Namer subclasses

`Namer` (in `approvaltests/core/namer.py`) now has two more abstract methods. The extension includes the dot, such as `".txt"`.

- `get_approved_file(self, extension_with_dot: str) -> str`
- `get_received_file(self, extension_with_dot: str) -> str`

If your namer does not implement both, creating it raises `TypeError`.

Search:

```sh
rg -n "\(Namer\)" --type py
```

Before:

```py
from approvaltests.core.namer import Namer


class MyNamer(Namer):
    def get_approved_filename(self) -> str:
        return "my_test.approved.txt"

    def get_received_filename(self) -> str:
        return "my_test.received.txt"
```

After (see also the section on removed methods below):

```py
from typing_extensions import override

from approvaltests.core.namer import Namer


class MyNamer(Namer):
    @override
    def get_approved_file(self, extension_with_dot: str) -> str:
        return f"my_test.approved{extension_with_dot}"

    @override
    def get_received_file(self, extension_with_dot: str) -> str:
        return f"my_test.received{extension_with_dot}"
```

## The extension comes from the writer

`FileApprover.verify` now asks the writer for its extension and passes it to `namer.get_approved_file(...)` and `namer.get_received_file(...)`.
A namer built with its own extension, such as `StackFrameNamer(".json")`, or one that had `set_extension` called on it, no longer controls the extension. The writer does.
`StackFrameNamer(".json")` and `get_default_namer(".json")` no longer accept an extension; use `options.for_file.with_extension(".json")`.
For `verify`, the writer's extension is `options.for_file.file_extention`. For files, it is the file's own extension.
`Options.namer` no longer sets the extension on the namer. If you ask it for names yourself, pass the extension: use `options.namer.get_approved_file(options.for_file.file_extention)`.

Search:

```sh
rg -n "Namer\(\"\.|set_extension" --type py
```

Before:

```py
verify(data, options=Options().with_namer(StackFrameNamer(".json")))
```

After:

```py
verify(data, options=Options().for_file.with_extension(".json"))
```

## get_approved_filename, get_received_filename and set_extension are removed

`Namer` and all the namers that ship with ApprovalTests no longer have `get_approved_filename()`, `get_received_filename()` or `set_extension()`.
Ask for a file name with the extension you want: `get_approved_file(extension_with_dot)` and `get_received_file(extension_with_dot)`. The default extension used to be `.txt`.
The constructor parameter `extension` of `StackFrameNamer` is still accepted but ignored. `PyTestNamer` no longer has the `extension` parameter. `TemplatedCustomNamer.format_filename` is removed too.

Search:

```sh
rg -n "get_approved_filename|get_received_filename|set_extension" --type py
```

| Before | After |
|---|---|
| `namer.get_approved_filename()` | `namer.get_approved_file(".txt")` |
| `namer.get_received_filename()` | `namer.get_received_file(".txt")` |
| `namer.set_extension(".json")` then `namer.get_approved_filename()` | `namer.get_approved_file(".json")` |
| `namer.format_filename("approved")` | `namer.get_approved_file(".txt")` |

## Coming in this release (still in progress)

- Most namers will become a `TemplatedCustomNamer`.

---

[Back to User Guide](../README.md#top)
