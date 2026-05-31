from pathlib import Path

_SCRIPT_DIR = Path(__file__).parent

for req_file in _SCRIPT_DIR.glob("requirements*.txt"):
    content = req_file.read_text()
    if ">=" in content:
        req_file.write_text(content.replace(">=", "=="))
