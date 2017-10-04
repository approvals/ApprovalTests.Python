import inspect
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
