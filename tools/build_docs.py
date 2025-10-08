#!/usr/bin/env python3
"""Generate MkDocs-ready lesson pages from the Day_* READMEs."""

from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path, PurePosixPath
from typing import Iterable
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
LESSONS_DIR = DOCS_DIR / "lessons"
DAY_PATTERN = re.compile(r"Day_(\d+)_?.*")
LINK_PATTERN = re.compile(r"\]\((?!https?://|mailto:|#)([^)]+)\)")
MATERIAL_EXTENSIONS = {".ipynb", ".py"}


def _repo_slug() -> str:
    slug = os.environ.get("GITHUB_REPOSITORY")
    if slug:
        return slug

    try:
        completed = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.SubprocessError, FileNotFoundError):
        completed = None

    if completed:
        candidate = _slug_from_git_url(completed.stdout.strip())
        if candidate:
            return candidate

    return "saint2706/Coding-For-MBA"


def _slug_from_git_url(url: str) -> str | None:
    if not url:
        return None

    if url.startswith("git@"):
        _, _, path = url.partition(":")
    else:
        parsed = urlsplit(url)
        path = parsed.path

    path = path.rstrip("/")
    if path.endswith(".git"):
        path = path[:-4]
    path = path.lstrip("/")

    if path.count("/") == 1:
        return path
    return None


def _slug_from_folder(folder: str) -> str:
    return folder.lower().replace("_", "-")


def _extract_first_heading(content: str) -> str | None:
    for line in content.splitlines():
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return None


def _nav_label(day_dir: Path, day_number: int, first_heading: str | None) -> str:
    if first_heading:
        return first_heading

    descriptor = ""
    parts = day_dir.name.split("_", 2)
    if len(parts) == 3:
        descriptor = " ".join(parts[2].replace("_", " ").split())

    if descriptor:
        return f"Day {day_number:02d} – {descriptor}"
    return f"Day {day_number:02d}"


def _resolve_day_number(day_dir: Path) -> int:
    match = DAY_PATTERN.match(day_dir.name)
    if match:
        return int(match.group(1))
    raise ValueError(f"Cannot determine day number from {day_dir}")


def _resolve_repo_target(
    base_dir: Path, relative_target: str
) -> tuple[PurePosixPath | None, bool]:
    base_relative = base_dir.relative_to(ROOT)
    stack = list(PurePosixPath(base_relative.as_posix()).parts)
    for part in PurePosixPath(relative_target).parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if stack:
                stack.pop()
            continue
        stack.append(part)

    candidate = PurePosixPath(*stack) if stack else PurePosixPath()
    candidate_path = ROOT / candidate
    if candidate_path.exists():
        return candidate, candidate_path.is_dir()
    return None, False


def _rewrite_relative_links(markdown: str, base_dir: Path, repo_slug: str) -> str:
    def replace(match: re.Match[str]) -> str:
        target_and_title = match.group(1).strip()
        if not target_and_title:
            return match.group(0)

        title = ""
        path = target_and_title
        if '"' in target_and_title:
            first_quote = target_and_title.find('"')
            path = target_and_title[:first_quote].strip()
            title = target_and_title[first_quote:].strip()
        elif "'" in target_and_title:
            first_quote = target_and_title.find("'")
            path = target_and_title[:first_quote].strip()
            title = target_and_title[first_quote:].strip()

        if not path or path.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        parsed = urlsplit(path)
        if parsed.scheme or parsed.netloc:
            return match.group(0)

        relative_target = parsed.path
        resolved, is_dir = _resolve_repo_target(base_dir, relative_target)
        if resolved is None:
            return match.group(0)

        target_path = resolved.as_posix()
        base = "tree" if is_dir else "blob"
        new_url = (
            f"https://github.com/{repo_slug}/{base}/main/{quote(target_path, safe='/')}"
        )
        if parsed.fragment:
            new_url += f"#{parsed.fragment}"
        if parsed.query:
            new_url += f"?{parsed.query}"

        title_suffix = f" {title}" if title else ""
        return f"]({new_url}{title_suffix})"

    return LINK_PATTERN.sub(replace, markdown)


def _material_links(day_dir: Path, repo_slug: str) -> Iterable[str]:
    base_blob = f"https://github.com/{repo_slug}/blob/main/"
    for candidate in sorted(day_dir.glob("*")):
        if not candidate.is_file():
            continue
        if candidate.name == "README.md":
            continue
        if candidate.suffix.lower() not in MATERIAL_EXTENSIONS:
            continue
        if candidate.name == "__init__.py":
            continue
        relative = candidate.relative_to(ROOT).as_posix()
        url = base_blob + quote(relative, safe="/")
        yield f"- [{candidate.name}]({url})"


def _nav_entry(label: str, output_name: str) -> str:
    quoted_label = json.dumps(label, ensure_ascii=False)
    return f"      - {quoted_label}: lessons/{output_name}"


def build() -> None:
    repo_slug = _repo_slug()
    LESSONS_DIR.mkdir(parents=True, exist_ok=True)

    for generated in LESSONS_DIR.glob("day-*.md"):
        generated.unlink()

    day_dirs = sorted(
        (p for p in ROOT.glob("Day_*") if p.is_dir()), key=_resolve_day_number
    )
    nav_entries: list[str] = [_nav_entry("Lesson Library", "index.md")]

    for day_dir in day_dirs:
        readme = day_dir / "README.md"
        if not readme.exists():
            continue
        day_number = _resolve_day_number(day_dir)
        content = readme.read_text(encoding="utf-8")
        heading = _extract_first_heading(content)
        content = _rewrite_relative_links(content, day_dir, repo_slug)
        content = _strip_first_heading(content)

        materials = list(_material_links(day_dir, repo_slug))
        if materials:
            materials_section = (
                "\n\n## Additional Materials\n\n" + "\n".join(materials) + "\n"
            )
        else:
            materials_section = ""

        output_name = f"{_slug_from_folder(day_dir.name)}.md"
        output_path = LESSONS_DIR / output_name
        nav_label = _nav_label(day_dir, day_number, heading)
        nav_entries.append(_nav_entry(nav_label, output_name))
        output_path.write_text(content + materials_section, encoding="utf-8")

    generated_count = len(list(LESSONS_DIR.glob("day-*.md")))
    _update_mkdocs_nav(nav_entries)
    print(f"Generated {generated_count} MkDocs lesson pages and refreshed navigation.")


def _strip_first_heading(content: str) -> str:
    lines = content.splitlines()
    stripped: list[str] = []
    removed = False
    for line in lines:
        if not removed and line.lstrip().startswith("#"):
            removed = True
            continue
        if not removed and not line.strip():
            # Skip leading blank lines before the first heading is removed
            continue
        stripped.append(line)
    return "\n".join(stripped).lstrip()


def _update_mkdocs_nav(entries: list[str]) -> None:
    config_path = ROOT / "mkdocs.yml"
    contents = config_path.read_text(encoding="utf-8").splitlines()

    try:
        start = next(
            i
            for i, line in enumerate(contents)
            if line.strip() == "# AUTOGENERATED LESSON NAV START"
        )
        end = next(
            i
            for i, line in enumerate(contents)
            if line.strip() == "# AUTOGENERATED LESSON NAV END"
        )
    except StopIteration as exc:  # pragma: no cover - guard against manual edits
        raise RuntimeError(
            "Could not locate AUTOGENERATED markers in mkdocs.yml"
        ) from exc

    if end <= start:
        raise RuntimeError("Invalid AUTOGENERATED markers ordering in mkdocs.yml")

    new_lines = contents[: start + 1]
    new_lines.extend(entries)
    new_lines.extend(contents[end:])
    config_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
