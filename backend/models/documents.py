"""Document-type catalog shared by the AI prompt and the API.

The catalog is the repo-root catalog.json (single source of truth). The
companion "Mutual NDA Cover Page" is excluded so exactly 11 document types
are offered, matching the frontend showcase.
"""

import json
from pathlib import Path

# backend/models/documents.py -> repo root is two parents up from backend/.
_CATALOG_PATH = Path(__file__).parent.parent.parent / "catalog.json"

_EXCLUDED_FILENAMES = {"Mutual-NDA-coverpage.md"}


def _load_templates() -> list[dict]:
    data = json.loads(_CATALOG_PATH.read_text(encoding="utf-8"))
    return [
        t
        for t in data.get("templates", [])
        if t.get("filename") not in _EXCLUDED_FILENAMES
    ]


DOCUMENT_TEMPLATES: list[dict] = _load_templates()


def get_document_catalog_text() -> str:
    """Render the catalog as a bulleted list for the AI system prompt."""
    lines = []
    for t in DOCUMENT_TEMPLATES:
        lines.append(f"- {t['name']}: {t['description']}")
    return "\n".join(lines)
