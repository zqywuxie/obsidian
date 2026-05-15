#!/usr/bin/env python3
"""Validate literature-note frontmatter against a domain taxonomy."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

try:
    import yaml  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required: pip install pyyaml") from exc


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8-sig"))


def iter_note_paths(paths: Iterable[Path]) -> List[Path]:
    out: List[Path] = []
    for path in paths:
        if path.is_dir():
            out.extend(sorted(path.rglob("*.md")))
        elif path.suffix.lower() == ".md":
            out.append(path)
    return out


def frontmatter(path: Path) -> Optional[Dict[str, Any]]:
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("malformed YAML frontmatter fence")
    data = yaml.safe_load(parts[1])
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data


def as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def category_terms(spec: Any) -> Set[str]:
    if isinstance(spec, dict) and isinstance(spec.get("tags"), dict):
        return set(str(k) for k in spec["tags"].keys())
    if isinstance(spec, dict):
        return set(str(k) for k in spec.keys() if k not in {"description", "label"})
    return set()


def taxonomy_fields(taxonomy: Dict[str, Any]) -> Tuple[List[str], Dict[str, Set[str]]]:
    categories = taxonomy.get("categories", {})
    if not isinstance(categories, dict):
        return [], {}
    fields: List[str] = []
    terms: Dict[str, Set[str]] = {}
    for field, spec in categories.items():
        fields.append(str(field))
        terms[str(field)] = category_terms(spec)
    return fields, terms


def candidate_terms(taxonomy: Dict[str, Any]) -> Set[str]:
    out: Set[str] = set()
    for item in taxonomy.get("candidate_terms", []) or []:
        if isinstance(item, str):
            out.add(item)
        elif isinstance(item, dict) and item.get("tag"):
            out.add(str(item["tag"]))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--taxonomy", required=True, type=Path)
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    taxonomy = load_yaml(args.taxonomy)
    if not isinstance(taxonomy, dict):
        raise SystemExit("taxonomy root must be a mapping")

    fields, field_terms = taxonomy_fields(taxonomy)
    all_canonical = set().union(*field_terms.values()) if field_terms else set()
    base_tags = set(str(x) for x in taxonomy.get("base_tags", []) or [])
    candidates = candidate_terms(taxonomy)

    errors: List[str] = []
    warnings: List[str] = []

    for path in iter_note_paths(args.paths):
        try:
            fm = frontmatter(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: {exc}")
            continue
        if fm is None:
            continue

        label = str(path)
        tags = set(str(x) for x in as_list(fm.get("tags")))
        missing_base = sorted(base_tags - tags)
        if missing_base:
            errors.append(f"{label}: missing base tags: {missing_base}")

        field_union: Set[str] = set()
        for field in fields:
            values = [str(x) for x in as_list(fm.get(field))]
            for tag in values:
                if tag and tag not in field_terms[field]:
                    errors.append(f"{label}: {field} contains non-canonical tag {tag!r}")
                elif tag:
                    field_union.add(tag)

        canonical = set(str(x) for x in as_list(fm.get("canonical_tags")))
        unknown = sorted(tag for tag in canonical if tag not in all_canonical)
        if unknown:
            errors.append(f"{label}: canonical_tags not in taxonomy: {unknown}")

        if canonical and field_union and canonical != field_union:
            warnings.append(
                f"{label}: canonical_tags differ from category field union; "
                f"canonical={sorted(canonical)} field_union={sorted(field_union)}"
            )

        note_candidates = set(str(x) for x in as_list(fm.get("candidate_tags")))
        undocumented = sorted(tag for tag in note_candidates if candidates and tag not in candidates)
        if undocumented:
            warnings.append(f"{label}: candidate_tags not listed in taxonomy candidate_terms: {undocumented}")

    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"OK: {len(iter_note_paths(args.paths))} note path(s), {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

