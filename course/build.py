"""Build the course into a single self-contained HTML file (dist/index.html).

Usage: python course/build.py
No third-party dependencies. Lessons are the Markdown files in content/ (sorted by name),
plus PROMPT-AULA.md as the last lesson.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "dist" / "index.html"


def lesson(path: Path, slug: str | None = None) -> dict:
    md = path.read_text(encoding="utf-8")
    m = re.search(r"^#\s+(.+)$", md, re.M)
    title = m.group(1).strip() if m else path.stem
    return {"id": slug or path.stem, "title": title, "md": md}


def main() -> None:
    lessons = [lesson(p) for p in sorted((ROOT / "content").glob("*.md"))]
    lessons.append(lesson(ROOT / "PROMPT-AULA.md", "14-prompt-de-aula"))
    data = json.dumps(lessons, ensure_ascii=False).replace("</", "<\\/")
    html = (ROOT / "template.html").read_text(encoding="utf-8").replace("__DATA__", data)
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"built {OUT} ({len(lessons)} lessons, {OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
