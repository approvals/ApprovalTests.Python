from pathlib import Path

reg_prod_path = Path(__file__).parent / "requirements.prod.txt"
min_prod_path = Path(__file__).parent / "requirements.prod.min.txt"

reg_prod = reg_prod_path.read_text()
min_prod = reg_prod.replace(">=", "==")

min_prod_path.write_text(min_prod)
