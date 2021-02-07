import inspect
import json
import os


def get_adjacent_file(name):
    calling_file = inspect.stack(1)[1][1]
    directory = os.path.dirname(os.path.abspath(calling_file))
    filename = os.path.join(directory, name)
    return filename


def write_to_temporary_file(expected, name):
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+b', suffix='.txt', prefix=name, delete=False) as temp:
        temp.write(expected.encode('utf-8-sig'))
        return temp.name


def to_json(object):
    return json.dumps(
        object,
        sort_keys=True,
        indent=4,
        separators=(',', ': '),
        default=lambda o: o.__dict__,
        ensure_ascii=True,
    )


def is_windows_os():
    return os.name == 'nt'


def create_empty_file(file_path):
    open(file_path, 'w').close()


def ensure_file_exists(approved_path):
    if not os.path.isfile(approved_path):
        create_empty_file(approved_path)