  ```mermaid
classDiagram
    class Namer {
        +get_received_filename(base: Optional[str]): str
        +get_approved_filename(base: Optional[str]): str
    }

    class NamerBase {
        -extension_with_dot: Optional[str]
        -config_loaded: bool
        -config: Optional[Dict]
        +__init__(extension: Optional[str]): None
        +get_file_name(): None
        +get_directory(): None
        +config_directory(): str
        +get_config(): Dict
        +get_basename(): str
        +get_received_filename(base: Optional[str]): str
        +get_approved_filename(base: Optional[str]): str
        +set_extension(extension: str): None
    }
    Namer <|-- NamerBase

    class StackFrameNamer {
        -directory: str
        -method_name: str
        -class_name: str
        +__init__(extension: Optional[str]): None
        +set_for_stack(caller: List): None
        +get_test_frame(caller: List): int
        +is_test_method(frame: FrameInfo): bool
        +get_class_name(): str
        +get_method_name(): str
        +get_directory(): str
        +config_directory(): str
        +get_file_name(): str
        +get_extension_with_dot(): str
        +get_extension_without_dot(): str
    }
    NamerBase <|-- StackFrameNamer

    class TemplatedCustomNamer {
        -template: str
        -namer_parts: StackFrameNamer
        +__init__(template: str): None
        +set_extension(extension_with_dot: str): None
        +get_received_filename(base: Optional[str]): str
        +get_approved_filename(base: Optional[str]): str
        +format_filename(approved_or_received: str): str
    }
    Namer <|-- TemplatedCustomNamer
    TemplatedCustomNamer ..> StackFrameNamer : uses
```
