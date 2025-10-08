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
from bs4 import BeautifulSoup
from nbconvert.exporters import HTMLExporter, MarkdownExporter
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


def ensure_accessible_html(html: str, title: str) -> str:
    """Post-process HTML to inject accessibility affordances."""

    soup = BeautifulSoup(html, "html.parser")

    html_tag = soup.find("html")
    if html_tag and not html_tag.get("lang"):
        html_tag["lang"] = "en"

    head = soup.find("head")
    if head and not head.find("style", attrs={"id": "accessibility-styles"}):
        style = soup.new_tag("style", id="accessibility-styles")
        style.string = (
            ".skip-link{position:absolute;left:-1000px;top:auto;width:1px;height:1px;"
            "overflow:hidden;}"
            ".skip-link:focus{position:static;width:auto;height:auto;padding:0.5rem;"
            "background:#000;color:#fff;z-index:1000;}"
            "main:focus{outline:3px solid #005fcc;}"
        )
        head.append(style)

    body = soup.find("body")
    if body and not body.find("a", class_="skip-link"):
        skip_link = soup.new_tag("a", href="#main-content")
        skip_link["class"] = ["skip-link"]
        skip_link.string = "Skip to main content"
        body.insert(0, skip_link)

    main = soup.find(id="main-content")
    if body and not main:
        main = soup.new_tag("main", id="main-content", tabindex="-1")
        for child in list(body.contents):
            if getattr(child, "name", None) == "a" and "skip-link" in child.get("class", []):
                continue
            main.append(child.extract())
        body.append(main)
    elif main:
        main["tabindex"] = "-1"

    if main and not main.find("h1"):
        heading = soup.new_tag("h1")
        heading.string = title
        main.insert(0, heading)

    last_level = 1
    for heading in soup.find_all(re.compile(r"^h[1-6]$")):
        current_level = int(heading.name[1])
        if current_level > last_level + 1:
            current_level = last_level + 1
            heading.name = f"h{current_level}"
        last_level = current_level

    for image in soup.find_all("img"):
        if not image.get("alt"):
            image["alt"] = "TODO: Provide descriptive alt text."

    return str(soup)


def validate_accessibility(html: str, notebook_name: str) -> list[str]:
    """Return any basic WCAG compliance issues detected in the HTML."""

    soup = BeautifulSoup(html, "html.parser")
    warnings: list[str] = []

    if not soup.find("a", class_="skip-link"):
        warnings.append(f"{notebook_name}: Missing skip navigation link.")
    if not soup.find(id="main-content"):
        warnings.append(f"{notebook_name}: Missing identifiable main content region.")

    headings = [int(tag.name[1]) for tag in soup.find_all(re.compile(r"^h[1-6]$"))]
    if headings:
        if headings[0] != 1:
            warnings.append(
                f"{notebook_name}: First heading should be level 1, found h{headings[0]}."
            )
        for previous, current in zip(headings, headings[1:]):
            if current - previous > 1:
                warnings.append(
                    f"{notebook_name}: Heading level jumps from h{previous} to h{current}."
                )

    for image in soup.find_all("img"):
        if not image.get("alt"):
            warnings.append(f"{notebook_name}: Image missing alt text.")

    return warnings


def export_static_content(notebook: Path, output_root: Path, template_dir: Path) -> list[Path]:
    """Render notebook to Markdown and accessible HTML outputs."""

    relative = notebook.relative_to(Path(__file__).resolve().parents[1])
    output_dir = output_root / relative.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    generated: list[Path] = []

    md_exporter = MarkdownExporter()
    md_exporter.exclude_input_prompt = True
    md_exporter.exclude_output_prompt = True
    markdown_body, _ = md_exporter.from_filename(str(notebook))
    markdown_path = output_dir / f"{notebook.stem}.md"
    markdown_path.write_text(markdown_body, encoding="utf-8")
    generated.append(markdown_path)

    html_exporter = HTMLExporter()
    html_exporter.extra_template_paths = [str(template_dir)]
    html_exporter.template_name = "accessible_html"
    html_exporter.exclude_input_prompt = True
    html_exporter.exclude_output_prompt = True
    html_body, _ = html_exporter.from_filename(str(notebook))
    accessible_html = ensure_accessible_html(html_body, notebook.stem.replace("_", " ").title())
    warnings = validate_accessibility(accessible_html, notebook.stem)
    if warnings:
        formatted = "\n".join(f" - {message}" for message in warnings)
        raise RuntimeError(
            "Accessibility validation failed for "
            f"{notebook}:\n{formatted}\n"
            "Fix the notebook structure or extend the exporter to resolve these issues."
        )
    html_path = output_dir / f"{notebook.stem}.html"
    html_path.write_text(accessible_html, encoding="utf-8")
    generated.append(html_path)

    return generated


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    converted: list[Path] = []
    exported: list[Path] = []
    output_root = root / "docs" / "lessons"
    template_dir = Path(__file__).resolve().parent / "templates"

    for day_dir in sorted(root.glob("Day_*")):
        if not day_dir.is_dir():
            continue
        for py_file in sorted(day_dir.rglob("*.py")):
            if py_file.name == "__init__.py":
                continue
            target = convert_file(py_file)
            converted.append(target.relative_to(root))
            try:
                assets = export_static_content(target, output_root, template_dir)
            except Exception as exc:  # pragma: no cover - runtime validation
                print(f"Error exporting {target}: {exc}", file=sys.stderr)
                raise
            else:
                exported.extend(asset.relative_to(root) for asset in assets)

    if converted:
        print("Generated notebooks:")
        for path in converted:
            print(f" - {path}")
    else:
        print("No lesson scripts were converted. Double-check the directory structure.")

    if exported:
        print("Rendered static content:")
        for path in exported:
            print(f" - {path}")
    else:
        print("No static lesson content was generated.")


if __name__ == "__main__":
    main()
