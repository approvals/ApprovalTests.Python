import inspect
import json
import os
from copy import deepcopy


def get_adjacent_file(name: str) -> str:
    calling_file = inspect.stack(1)[1][1]
    directory = os.path.dirname(os.path.abspath(calling_file))
    filename = os.path.join(directory, name)
    return filename


def write_to_temporary_file(expected: str, name: str):
    import tempfile

    with tempfile.NamedTemporaryFile(
        mode="w+b", suffix=".txt", prefix=name, delete=False
    ) as temp:
        temp.write(expected.encode("utf-8-sig"))
        return temp.name


def to_json(object) -> str:
    return json.dumps(
        object,
        sort_keys=True,
        indent=4,
        separators=(",", ": "),
        default=lambda o: o.__dict__,
        ensure_ascii=True,
    )

def deserialize_json_fields(a_dict: dict) -> dict:
    a_dict = deepcopy(a_dict)
    for key, val in a_dict.items():
        if isinstance(val, str) and val.startswith('{'):
            try:
                deserialized_val = json.loads(val)
            except:
                # leave field unchanged on exception
                pass
            else:
                a_dict[key] = deserialized_val
        elif isinstance(val, dict):
            a_dict[key] = deserialize_json_fields(val)
    return a_dict



def is_windows_os() -> bool:
    return os.name == "nt"


def create_empty_file(file_path: str) -> None:
    from empty_files.empty_files import create_empty_file
    create_empty_file(file_path)


def ensure_file_exists(approved_path: str) -> None:
    if not os.path.isfile(approved_path):
        create_empty_file(approved_path)


def create_directory_if_needed(received_file: str) -> None:
    directory = os.path.dirname(received_file)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
