from pathlib import Path
import ast

def test_main_is_valid_python():
    source = (Path(__file__).parents[1] / "main.py").read_text(encoding="utf-8")
    ast.parse(source)

def test_main_references_existing_shared_framework():
    project = Path(__file__).parents[1]
    assert (project.parent / "common_app.py").is_file()
