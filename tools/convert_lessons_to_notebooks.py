"""Utility for converting lesson Python scripts into Jupyter notebooks.

The curriculum historically distributed runnable ``.py`` files under each
``Day_*`` directory. To make the project more notebook-friendly we generate a
matching ``.ipynb`` that mirrors the original source.  The conversion keeps
module docstrings as a leading Markdown cell and respects ``# %%`` cell markers
for people who edited lessons in IDE notebook modes.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from typing import Iterable, Tuple

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

CELL_PATTERN = re.compile(
    r"(?m)^#\s*%%(?:\s*\[(?P<kind>markdown)\])?(?:\s*(?P<title>.*))?$"
)


def extract_module_docstring(source: str) -> Tuple[str | None, str]:
    """Return the module docstring (if any) and the remaining source.

    If parsing fails we fall back to returning the untouched source so that we
    never block conversion.
    """

    try:
        module = ast.parse(source)
    except SyntaxError:
        return None, source

    docstring = ast.get_docstring(module)
    if not docstring or not module.body:
        return None, source

    first_statement = module.body[0]
    if not isinstance(first_statement, ast.Expr):
        return None, source

    value = getattr(first_statement, "value", None)
    if isinstance(value, ast.Constant) and isinstance(value.value, str):
        literal = ast.get_source_segment(source, first_statement)
    elif isinstance(value, ast.Str):  # pragma: no cover  # Py<3.8 compatibility
        literal = ast.get_source_segment(source, first_statement)
    else:
        return None, source

    if not literal:
        return docstring, source

    prefix, _, remainder = source.partition(literal)
    if remainder.startswith("\n"):
        remainder = remainder[1:]
    return docstring, prefix + remainder


def iter_cells(source: str) -> Iterable[Tuple[str, str]]:
    """Yield ``(cell_type, cell_source)`` pairs for the given source text."""

    position = 0
    current_type = "code"
    for match in CELL_PATTERN.finditer(source):
        segment = source[position : match.start()]
        if segment.strip():
            yield current_type, segment.rstrip("\n") + "\n"
        marker_type = match.group("kind")
        current_type = "markdown" if marker_type == "markdown" else "code"
        position = match.end()

    tail = source[position:]
    if tail.strip():
        yield current_type, tail.rstrip("\n") + "\n"


def build_notebook(path: Path) -> nbformat.NotebookNode:
    source = path.read_text()
    docstring, code_body = extract_module_docstring(source)
    notebook = new_notebook(
        metadata={
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            },
        }
    )

    readme_path = path.parent / "README.md"
    if readme_path.is_file():
        try:
            readme_text = readme_path.read_text(encoding="utf-8")
        except OSError as exc:  # pragma: no cover - depends on filesystem errors
            print(f"Warning: Could not read {readme_path}: {exc}", file=sys.stderr)
        else:
            cleaned_readme = readme_text.lstrip("\ufeff").rstrip("\n")
            if cleaned_readme:
                notebook.cells.append(new_markdown_cell(cleaned_readme))

    if docstring:
        notebook.cells.append(new_markdown_cell(docstring.strip()))

    for cell_type, cell_source in iter_cells(code_body):
        if cell_type == "markdown":
            notebook.cells.append(new_markdown_cell(cell_source.strip()))
        else:
            notebook.cells.append(new_code_cell(cell_source))

    if not notebook.cells:
        notebook.cells.append(
            new_markdown_cell("_This lesson does not contain executable code._")
        )

    return notebook


def convert_file(path: Path) -> Path:
    target = path.with_suffix(".ipynb")
    notebook = build_notebook(path)
    nbformat.write(notebook, target)
    return target


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    converted: list[Path] = []

    for day_dir in sorted(root.glob("Day_*")):
        if not day_dir.is_dir():
            continue
        for py_file in sorted(day_dir.rglob("*.py")):
            if py_file.name == "__init__.py":
                continue
            target = convert_file(py_file)
            converted.append(target.relative_to(root))

    if converted:
        print("Generated notebooks:")
        for path in converted:
            print(f" - {path}")
    else:
        print("No lesson scripts were converted. Double-check the directory structure.")


if __name__ == "__main__":
    main()
