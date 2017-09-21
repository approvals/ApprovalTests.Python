import inspect
import os


def get_adjacent_file(name):
    calling_file = inspect.stack(1)[1][1]
    directory = os.path.dirname(os.path.abspath(calling_file))
    filename = os.path.join(directory, name)
    return filename
