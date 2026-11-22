# Namer architecture

Every approved and received file name is built from one template. The template has named fields, and the namers only differ in how they fill those fields in.

- `TemplateFieldValues` holds the field values. `with_` sets approved/received and the extension. `add_additional_information` adds a ".more" part to the name.
- `TemplatedCustomNamer` owns `DEFAULT_TEMPLATE` and the static `create_filename`, which fills a template. It reads the fields from the stack through `stack_walker`.
- `StackFrameNamer`, `PyTestNamer` and `CliNamer` are thin shells: they only supply field values (and sometimes their own template) and let `create_filename` do the work. `FilePathNamer` is a `StackFrameNamer` that only changes the approved file.
- `Options.for_file.add_additional_information` is passed on by `Options.namer` to `get_default_namer`, which hands it to `StackFrameNamer`.
- The writer removes its own received file (`clean_up_received`) and knows its extension (`get_file_extension_with_dot`). For now `Options.namer` still sets the extension on the namer with `set_extension`; Phase 3 of the refactor moves it to the writer.

```mermaid
classDiagram
    class Namer {
        +get_received_filename(): str
        +get_approved_filename(): str
    }

    class TemplateFieldValues {
        <<dataclass>>
        approved_or_received: str
        approvals_subdirectory: str
        file_extension: str
        relative_test_source_directory: str
        test_case_name: str
        test_file_name: str
        test_source_directory: str
        additional_information: str
        +with_(approved_or_received, file_extension): TemplateFieldValues
        +add_additional_information(more): TemplateFieldValues
    }

    class TemplatedCustomNamer {
        +DEFAULT_TEMPLATE: str
        +create_filename(template, values)$ str
        +get_template_fields_from_stacktrace()$ TemplateFieldValues
        +get_template(): str
        +get_template_field_values(): TemplateFieldValues
    }
    Namer <|-- TemplatedCustomNamer
    TemplatedCustomNamer ..> TemplateFieldValues : fills

    class StackFrameNamer {
        +get_template(): str
        +get_template_field_values(): TemplateFieldValues
    }
    Namer <|-- StackFrameNamer
    class FilePathNamer {
        approved file only
    }
    StackFrameNamer <|-- FilePathNamer

    class PyTestNamer {
        +get_template_field_values(): TemplateFieldValues
    }
    Namer <|-- PyTestNamer

    class CliNamer {
        +TEMPLATE: str
    }
    Namer <|-- CliNamer

    class stack_walker {
        +get_test_frame()
        +get_test_frame_index(caller)
        +load_config(directory)
    }

    class Writer {
        +get_file_extension_with_dot(): str
        +clean_up_received(received_file)
    }

    StackFrameNamer ..> TemplatedCustomNamer : create_filename
    PyTestNamer ..> TemplatedCustomNamer : create_filename
    CliNamer ..> TemplatedCustomNamer : create_filename
    TemplatedCustomNamer ..> stack_walker : uses
    StackFrameNamer ..> stack_walker : uses
    Writer ..> Namer : will supply the extension (Phase 3)
```
