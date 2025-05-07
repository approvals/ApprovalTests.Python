import ast
import os


def test_no_imports_from_build_directory() -> None:
    # Make sure no file imports from build
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude directories that start with '.'
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "build"]
        # also exclude venv
        dirnames[:] = [d for d in dirnames if not d.startswith("venv")]
        for filename in filenames:
            # Skip files that start with '.' and non-Python files
            if filename.startswith(".") or not filename.endswith(".py"):
                continue
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                source = file.read()
            try:
                tree = ast.parse(source, filename=file_path)
            except SyntaxError:
                continue  # Skip files with syntax errors
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name == "build" or alias.name.startswith("build."):
                            assert False, f"{file_path} imports 'build'"
                elif isinstance(node, ast.ImportFrom):
                    if node.module == "build" or (
                        node.module and node.module.startswith("build.")
                    ):
                        assert False, f"{file_path} imports from 'build'"
