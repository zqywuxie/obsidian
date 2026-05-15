#!/usr/bin/env python
"""Shared read-only Zotero helpers for Zotero Taxonomy Curator."""

from __future__ import annotations

import argparse
import contextlib
import html
import json
import os
import re
import shutil
import sqlite3
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple


TEXT_FIELDS = [
    "title",
    "abstractNote",
    "date",
    "publicationTitle",
    "DOI",
    "url",
    "shortTitle",
    "extra",
    "pages",
    "volume",
    "issue",
    "publisher",
    "place",
    "ISBN",
    "ISSN",
]


def find_repo_root(start: Optional[Path] = None) -> Path:
    """Find a parent containing config/ or fall back to the current directory."""
    start = (start or Path(__file__)).resolve()
    for parent in [start] + list(start.parents):
        if (parent / "config").exists():
            return parent
        if parent.name == "skills" and (parent.parent / "config").exists():
            return parent.parent
    return Path.cwd()


def find_config_path(explicit: Optional[str] = None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()

    root = find_repo_root()
    candidates = [
        root / "config" / "local.yaml",
        Path.cwd() / "config" / "local.yaml",
    ]
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError("Cannot find config/local.yaml. Pass --config explicitly.")


def _parse_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def load_simple_yaml(path: Path) -> Dict[str, Any]:
    """Load the small local.yaml structure without requiring PyYAML."""
    data: Dict[str, Any] = {}
    stack: List[Tuple[int, Dict[str, Any]]] = [(-1, data)]
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, sep, value = line.strip().partition(":")
        if not sep:
            continue
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if value.strip():
            parent[key] = _parse_scalar(value)
        else:
            child: Dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))
    return data


def load_config(explicit: Optional[str] = None) -> Tuple[Dict[str, Any], Path]:
    path = find_config_path(explicit)
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        data = load_simple_yaml(path)
    return data, path


def config_paths(config: Dict[str, Any]) -> Tuple[Path, Path, Path]:
    zotero = config.get("zotero", {})
    sqlite_path = Path(zotero.get("sqlite_path", "")).expanduser()
    data_dir = Path(zotero.get("data_dir", sqlite_path.parent)).expanduser()
    storage_dir = Path(zotero.get("storage_dir", data_dir / "storage")).expanduser()
    if not sqlite_path:
        raise ValueError("config/local.yaml is missing zotero.sqlite_path")
    return data_dir, sqlite_path, storage_dir


@contextlib.contextmanager
def connect_zotero(sqlite_path: Path) -> Iterator[sqlite3.Connection]:
    """Open Zotero read-only. Prefer a temporary snapshot; fall back to immutable."""
    sqlite_path = sqlite_path.resolve()
    temp_dir: Optional[tempfile.TemporaryDirectory[str]] = None
    con: Optional[sqlite3.Connection] = None
    try:
        temp_dir = tempfile.TemporaryDirectory(prefix="zotero_ro_")
        snapshot = Path(temp_dir.name) / "zotero.sqlite"
        shutil.copy2(sqlite_path, snapshot)
        for suffix in ["-wal", "-shm", "-journal"]:
            sidecar = Path(str(sqlite_path) + suffix)
            if sidecar.exists():
                shutil.copy2(sidecar, Path(str(snapshot) + suffix))
        con = sqlite3.connect(str(snapshot))
        con.row_factory = sqlite3.Row
        yield con
    except Exception:
        if con is not None:
            con.close()
        if temp_dir is not None:
            temp_dir.cleanup()
        uri = f"file:{sqlite_path.as_posix()}?mode=ro&immutable=1"
        con = sqlite3.connect(uri, uri=True)
        con.row_factory = sqlite3.Row
        try:
            yield con
        finally:
            con.close()
        return
    finally:
        if con is not None:
            con.close()
        if temp_dir is not None:
            temp_dir.cleanup()


def clean_html(value: Optional[str]) -> str:
    if not value:
        return ""
    text = re.sub(r"<br\s*/?>", "\n", value, flags=re.I)
    text = re.sub(r"</p\s*>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def rows_to_dicts(rows: Iterable[sqlite3.Row]) -> List[Dict[str, Any]]:
    return [dict(row) for row in rows]


def collection_tree(con: sqlite3.Connection) -> List[Dict[str, Any]]:
    cur = con.cursor()
    cur.execute(
        """
        select collectionID, collectionName, parentCollectionID, key
        from collections
        order by lower(collectionName), collectionID
        """
    )
    rows = rows_to_dicts(cur.fetchall())
    by_id = {row["collectionID"]: row for row in rows}

    def path_for(row: Dict[str, Any]) -> str:
        parts = [row["collectionName"]]
        parent_id = row["parentCollectionID"]
        seen = set()
        while parent_id and parent_id in by_id and parent_id not in seen:
            seen.add(parent_id)
            parent = by_id[parent_id]
            parts.append(parent["collectionName"])
            parent_id = parent["parentCollectionID"]
        return "/".join(reversed(parts))

    cur.execute("select collectionID, count(*) as itemCount from collectionItems group by collectionID")
    counts = {row["collectionID"]: row["itemCount"] for row in cur.fetchall()}
    for row in rows:
        row["path"] = path_for(row)
        row["itemCount"] = counts.get(row["collectionID"], 0)
    return rows


def find_collection(con: sqlite3.Connection, identifier: str) -> Dict[str, Any]:
    ident = identifier.strip()
    collections = collection_tree(con)
    matches = [
        row
        for row in collections
        if str(row["collectionID"]) == ident
        or row["key"] == ident
        or row["collectionName"].lower() == ident.lower()
        or row["path"].lower() == ident.lower()
    ]
    if not matches:
        raise ValueError(f"No Zotero collection matched: {identifier}")
    if len(matches) > 1:
        paths = ", ".join(row["path"] for row in matches)
        raise ValueError(f"Ambiguous collection {identifier!r}. Use one full path: {paths}")
    return matches[0]


def item_fields(con: sqlite3.Connection, item_ids: Sequence[int]) -> Dict[int, Dict[str, str]]:
    if not item_ids:
        return {}
    placeholders = ",".join("?" for _ in item_ids)
    cur = con.cursor()
    cur.execute(
        f"""
        select d.itemID, f.fieldName, v.value
        from itemData d
        join fields f on f.fieldID = d.fieldID
        join itemDataValues v on v.valueID = d.valueID
        where d.itemID in ({placeholders})
        """,
        list(item_ids),
    )
    out: Dict[int, Dict[str, str]] = {int(i): {} for i in item_ids}
    for row in cur.fetchall():
        out.setdefault(row["itemID"], {})[row["fieldName"]] = row["value"]
    return out


def collection_paths_for_item(con: sqlite3.Connection, item_id: int) -> List[str]:
    cur = con.cursor()
    cur.execute("select collectionID from collectionItems where itemID=?", (item_id,))
    ids = {row["collectionID"] for row in cur.fetchall()}
    return [row["path"] for row in collection_tree(con) if row["collectionID"] in ids]


def regular_item_ids_in_collection(con: sqlite3.Connection, collection_id: int) -> List[int]:
    cur = con.cursor()
    cur.execute(
        """
        select i.itemID
        from collectionItems ci
        join items i on i.itemID = ci.itemID
        join itemTypes it on it.itemTypeID = i.itemTypeID
        where ci.collectionID = ?
          and it.typeName not in ('attachment', 'note', 'annotation')
        order by ci.orderIndex, i.itemID
        """,
        (collection_id,),
    )
    return [row["itemID"] for row in cur.fetchall()]


def list_items(con: sqlite3.Connection, item_ids: Sequence[int]) -> List[Dict[str, Any]]:
    if not item_ids:
        return []
    placeholders = ",".join("?" for _ in item_ids)
    cur = con.cursor()
    cur.execute(
        f"""
        select i.itemID, i.key as itemKey, it.typeName as itemType, i.dateAdded, i.dateModified
        from items i
        join itemTypes it on it.itemTypeID = i.itemTypeID
        where i.itemID in ({placeholders})
        """,
        list(item_ids),
    )
    base = {row["itemID"]: dict(row) for row in cur.fetchall()}
    fields = item_fields(con, item_ids)
    for item_id in item_ids:
        row = base.get(item_id)
        if not row:
            continue
        row.update(
            {
                "title": fields.get(item_id, {}).get("title", ""),
                "date": fields.get(item_id, {}).get("date", ""),
                "year": extract_year(fields.get(item_id, {}).get("date", "")),
                "publicationTitle": fields.get(item_id, {}).get("publicationTitle", ""),
                "DOI": fields.get(item_id, {}).get("DOI", ""),
            }
        )
    return [base[item_id] for item_id in item_ids if item_id in base]


def extract_year(date_value: str) -> str:
    match = re.search(r"(19|20)\d{2}", date_value or "")
    return match.group(0) if match else ""


def resolve_attachment_path(storage_dir: Path, attachment_key: str, zotero_path: str) -> Optional[Path]:
    if not zotero_path:
        return None
    if zotero_path.startswith("storage:"):
        return storage_dir / attachment_key / zotero_path.split(":", 1)[1]
    path = Path(zotero_path)
    if path.is_absolute():
        return path
    return storage_dir / attachment_key / zotero_path


def dump_json(data: Any, out: Optional[str] = None) -> None:
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if out:
        Path(out).expanduser().write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--config", help="Path to config/local.yaml")
    parser.add_argument("--out", help="Write JSON output to this file")
