# Refactor Checklist: Namers on the Template, Extension from the Writer

Goal: line Python up with ApprovalTests.Java's `internal_documentation/DesiredNamerArchitecture.md`.
- Most namers become `TemplatedCustomNamer` with a template.
- The writer says what extension it has, and the approver passes that extension to the namer.

## Target shape

```python
class Writer(ABC):  # purely abstract
    def get_file_extension_with_dot(self) -> str: ...
    def write_received_file(self, received_file: str) -> str: ...
    def clean_up_received(self, received_file: str) -> None: ...


class Namer(ABC):
    def get_approved_file(self, extension_with_dot: str) -> str: ...
    def get_received_file(self, extension_with_dot: str) -> str: ...


class TemplatedCustomNamer(Namer):
    @staticmethod
    def get_template_fields_from_stacktrace() -> dict[
        str, str
    ]: ...  # the test-discovery seam


# FileApprover.verify
extension = writer.get_file_extension_with_dot()
approved = namer.get_approved_file(extension)
received = namer.get_received_file(extension)
...
writer.clean_up_received(received)  # instead of os.remove
```

## Rules for each step
- One small refactoring per step. File names must not change.
- The existing tests already cover file naming. An extra test that pins names is optional; if you add one, make it an approval test with `verify_all`.
- Run `mise exec -- python -m pytest --quiet` after each step (about 5 seconds).
- Run `./build_and_test` before each commit (about 20 seconds). Treat any `Traceback` in the output as a failure, even when the exit code is 0.
- Check in with the human before each commit. Use the notation in `internal_documentation/commit_notation.md`.

## Steps

### Phase 1: Writer (doesn't touch the namers)
- [x] Add `get_file_extension_with_dot()` to `StringWriter` and `BinaryWriter`
- [x] Add `get_file_extension_with_dot()` to `ExistingFileWriter` (it comes from `options.for_file.file_extention`)
- [x] `verify_with_namer` passes the options extension to `StringWriter` (today it always gets `.txt`)
- [x] Add `clean_up_received()` to each of the 3 writers (`os.remove`)
- [x] Add both methods as `@abstractmethod` on `Writer`
- [x] `FileApprover` calls `writer.clean_up_received` instead of `os.remove` (keep `verify_files` backward compatible: optional `writer` as the last parameter, falling back to `os.remove`)

### Phase 2: Namers onto the template
- [x] Extract `TemplatedCustomNamer.get_template_fields_from_stacktrace()`. It returns the fields dict that `format_filename` builds today, without the per-call fields (approved_or_received, extension).
- [x] Move the stack-walking it needs out of `StackFrameNamer`, so the template namer no longer creates a `StackFrameNamer` (this removes the circular dependency below)
- [x] Add a `DEFAULT_TEMPLATE` that reproduces today's names:
  - class methods: `ClassName.method`; functions: `test_file.function` (decision: keep today's names)
  - an empty subdirectory must not leave `//` in the path
- [x] Add an `{additional_information}` field (`.` + the parameters joined with `.`, or empty)
- [x] Make sure the callers of `get_file_name()` / `get_basename()` (`approvals.py`, `asserts.py`, `ScenarioNamer`) work with the template namer
- [x] Add a `TemplateFieldValues` dataclass (the 8 fields, like Java) with `with_(approved_or_received, file_extension)` and `with_additional_information(...)`; `get_template_fields_from_stacktrace()` returns it and `create_filename(template, values)` takes it
- [x] `get_file_name()` and `get_basename()` are each just a call to `create_filename` with their own template string (`"{test_file_name}.{test_case_name}"` and `"{test_source_directory}/{approvals_subdirectory}/{test_file_name}.{test_case_name}"`)
- [-] ~~`create_filename` raises `Unknown template field: {x}` for fields it doesn't know (like Java's `resolveTemplate`)~~ (skipped)
- [x] Read the stack once when the namer is built and keep the `TemplateFieldValues` (like Java's `StackTraceNamer`), instead of on every call
- [x] The default namer (`StackFrameNamer`) becomes a shell around the template: it keeps its API, but its file names come from `TemplatedCustomNamer.create_filename(DEFAULT_TEMPLATE, values)` (like Java's `StackTraceNamer`)
- [x] Replace `ScenarioNamer` with the template namer plus additional information (`NamerFactory.with_parameters`, `get_scenario_namer`)
- [x] `PyTestNamer` builds its fields from the pytest `request` (a second way to get fields) and uses the template
- [x] Add `options.for_file.add_additional_information(x)` (adds `.x` each time, like Java's `forFile().withAdditionalInformation`) and a property to read it back
- [x] `Options.namer` passes that additional information to the default namer when no namer was set (`get_default_namer(additional_information)`, `StackFrameNamer` accepts it)
- [x] `NamerFactory.with_parameters(*args)` becomes a loop of `add_additional_information` (and so `as_ci_specific_test`)
- [ ] `get_scenario_namer(...)` returns the default namer with that additional information instead of a `ScenarioNamer`
- [ ] Remove `ScenarioNamer` (upgrade guide: what to write instead)
- [ ] `CliNamer` becomes a template: `"{test_id}.{approved_or_received}.{file_extension}"`
- [ ] `FilePathNamer` uses `get_template_fields_from_stacktrace()` for the received file and keeps its fixed approved path
- [ ] `InlineComparator` uses `get_template_fields_from_stacktrace()` where it can (it still writes the docstring to a temporary approved file)

### Phase 3: The extension comes from the writer
- [ ] Add `get_approved_file(ext)` / `get_received_file(ext)` to `TemplatedCustomNamer` (ext fills `{file_extension}`)
- [ ] Add them to whatever is left outside the template (`FilePathNamer`, `InlineComparator`)
- [ ] Add both as `@abstractmethod` on `Namer`
- [ ] `FileApprover.verify` calls `namer.get_*_file(writer.get_file_extension_with_dot())`. This is the only step that changes behavior.
- [ ] `Options.namer` stops calling `set_extension`

### Later (not in this round)
- [ ] Remove `get_approved_filename` / `get_received_filename` / `set_extension`
- [ ] Remove `NamerBase` and `StackFrameNamer` if nothing uses them
- [ ] Stop returning a path from `write_received_file`
- [ ] Creator per `verify`, `with_subdirectory` and `with_template` on `Options`

## Known traps (found in the first attempt)
- **pylint prints a hidden crash.** pylint 4.1.4 with astroid 4.3.4 prints `Exception ignored ... ValueError: generator already executing` and still exits 0 with a 10/10 score. In our first attempt it was triggered by a non-abstract method on `Namer` that calls another `self` method, such as `return self.get_approved_filename()`. Don't give `Namer` default methods that delegate.
- **ruff ARG002** flags unused method arguments.
- **Circular dependency:** `TemplatedCustomNamer` creates a `StackFrameNamer` inside it today. Extract the stack walking before making the default namer a template.
- **Paths on Windows:** `NamerBase` uses `os.path.join` (backslashes on Windows), but templates use `/`. Watch for tests that approve file paths.
- **`FilePathNamer` overrides only the approved file.** Its received file must keep the default name.
- **Behavior change to tell users about:** once the extension comes from the writer, a namer built with its own extension, such as `StackFrameNamer(".json")`, no longer controls the extension.
- **Breaking change to tell users about:** `Writer` now has two more abstract methods, `get_file_extension_with_dot()` and `clean_up_received()`. A custom `Writer` subclass fails with `TypeError` until it implements both.
