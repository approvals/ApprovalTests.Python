import re
from pathlib import Path


def get_parent_directory():
    return Path(__file__).parent


def get_version():
    _version_file_contents = (get_parent_directory() / "approvaltests" / "version.py").read_text()
    matched = re.search(r'"(.*)"', _version_file_contents)
    return matched.group(1) if matched is not None else "UNKNOWN VERSION"

def applesource():
    with open(get_parent_directory() / 'requirements.prod.required.txt') as f:
        required = f.read().splitlines()
    return required