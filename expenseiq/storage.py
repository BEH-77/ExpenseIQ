"""Local JSON persistence for expenses."""

import json
from pathlib import Path
from typing import Any


def load_data(path: Path) -> dict[str, Any]:
    """Read saved expense data, or return an empty collection for a new file."""
    if not path.exists():
        return {"next_id": 1, "expenses": []}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}") from exc

    if not isinstance(data, dict) or not isinstance(data.get("expenses"), list):
        raise ValueError(f"Invalid expense data in {path}")
    if type(data.get("next_id")) is not int or data["next_id"] < 1:
        raise ValueError(f"Invalid next expense ID in {path}")
    return data


def save_data(path: Path, data: dict[str, Any]) -> None:
    """Write expense data to a local JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
