from pathlib import Path

_SCRIPT_DIR = Path(__file__).parent

reg_prod_path = _SCRIPT_DIR / "requirements.prod.txt"
min_prod_path = _SCRIPT_DIR / "requirements.prod.min.txt"

reg_prod = reg_prod_path.read_text()
min_prod = reg_prod.replace(">=", "==")

min_prod_path.write_text(min_prod)
