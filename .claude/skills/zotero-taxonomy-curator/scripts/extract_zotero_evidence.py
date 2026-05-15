#!/usr/bin/env python
"""Extract one Zotero item into a JSON Raw_Data_Buffer."""

from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

from curator_common import (
    TEXT_FIELDS,
    add_common_args,
    clean_html,
    collection_paths_for_item,
    config_paths,
    connect_zotero,
    dump_json,
    extract_year,
    find_collection,
    item_fields,
    list_items,
    load_config,
    regular_item_ids_in_collection,
    resolve_attachment_path,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    add_common_args(parser)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--item-key", help="Zotero parent item key")
    target.add_argument("--title", help="Exact or partial paper title")
    target.add_argument("--collection", help="Extract the first N items from a collection")
    parser.add_argument("--limit", type=int, default=1, help="Limit for --title or --collection")
    parser.add_argument(
        "--cache-chars",
        type=int,
        default=12000,
        help="Maximum characters to include from each .zotero-ft-cache file.",
    )
    return parser


def find_item_ids(con: sqlite3.Connection, args: argparse.Namespace) -> List[int]:
    cur = con.cursor()
    if args.item_key:
        cur.execute("select itemID from items where key=?", (args.item_key,))
        rows = cur.fetchall()
        if not rows:
            raise ValueError(f"No Zotero item matched key: {args.item_key}")
        return [rows[0]["itemID"]]

    if args.title:
        cur.execute(
            """
            select i.itemID
            from items i
            join itemData d on d.itemID = i.itemID
            join fields f on f.fieldID = d.fieldID and f.fieldName = 'title'
            join itemDataValues v on v.valueID = d.valueID
            join itemTypes it on it.itemTypeID = i.itemTypeID
            where it.typeName not in ('attachment', 'note', 'annotation')
              and lower(v.value) like lower(?)
            order by length(v.value), i.itemID
            limit ?
            """,
            (f"%{args.title}%", args.limit),
        )
        rows = cur.fetchall()
        if not rows:
            raise ValueError(f"No Zotero item title matched: {args.title}")
        return [row["itemID"] for row in rows]

    collection = find_collection(con, args.collection)
    return regular_item_ids_in_collection(con, collection["collectionID"])[: args.limit]


def get_creators(con: sqlite3.Connection, item_id: int) -> List[Dict[str, Any]]:
    cur = con.cursor()
    cur.execute(
        """
        select c.creatorID, ct.creatorType, c.firstName, c.lastName, c.fieldMode, ic.orderIndex
        from itemCreators ic
        join creators c on c.creatorID = ic.creatorID
        join creatorTypes ct on ct.creatorTypeID = ic.creatorTypeID
        where ic.itemID = ?
        order by ic.orderIndex
        """,
        (item_id,),
    )
    creators = []
    for row in cur.fetchall():
        first = row["firstName"] or ""
        last = row["lastName"] or ""
        name = last if row["fieldMode"] == 1 or not first else f"{first} {last}".strip()
        creators.append(
            {
                "creatorID": row["creatorID"],
                "creatorType": row["creatorType"],
                "firstName": first,
                "lastName": last,
                "name": name,
            }
        )
    return creators


def get_tags(con: sqlite3.Connection, item_id: int) -> List[str]:
    cur = con.cursor()
    cur.execute(
        """
        select t.name
        from itemTags it
        join tags t on t.tagID = it.tagID
        where it.itemID = ?
        order by lower(t.name)
        """,
        (item_id,),
    )
    return [row["name"] for row in cur.fetchall()]


def get_attachments(
    con: sqlite3.Connection, item_id: int, storage_dir: Path, cache_chars: int
) -> List[Dict[str, Any]]:
    cur = con.cursor()
    cur.execute(
        """
        select a.itemID, child.key as attachmentKey, a.path, a.contentType, a.linkMode,
               a.storageModTime, a.storageHash
        from itemAttachments a
        join items child on child.itemID = a.itemID
        where a.parentItemID = ?
        order by a.itemID
        """,
        (item_id,),
    )
    attachments = []
    for row in cur.fetchall():
        resolved = resolve_attachment_path(storage_dir, row["attachmentKey"], row["path"] or "")
        cache_path = storage_dir / row["attachmentKey"] / ".zotero-ft-cache"
        cache_text = ""
        if cache_path.exists() and cache_chars != 0:
            text = cache_path.read_text(encoding="utf-8", errors="replace")
            cache_text = text if cache_chars < 0 else text[:cache_chars]
        attachments.append(
            {
                "itemID": row["itemID"],
                "attachmentKey": row["attachmentKey"],
                "contentType": row["contentType"],
                "path": row["path"],
                "resolved_path": str(resolved) if resolved else "",
                "exists": bool(resolved and resolved.exists()),
                "cache_path": str(cache_path),
                "cache_exists": cache_path.exists(),
                "cache_text": cache_text,
                "zotero_pdf_link": f"zotero://open-pdf/library/items/{row['attachmentKey']}",
            }
        )
    return attachments


def get_notes(con: sqlite3.Connection, item_id: int) -> List[Dict[str, Any]]:
    cur = con.cursor()
    cur.execute(
        """
        select n.itemID, child.key as noteKey, n.title, n.note
        from itemNotes n
        join items child on child.itemID = n.itemID
        where n.parentItemID = ?
        order by n.itemID
        """,
        (item_id,),
    )
    return [
        {
            "itemID": row["itemID"],
            "noteKey": row["noteKey"],
            "title": row["title"],
            "text": clean_html(row["note"]),
        }
        for row in cur.fetchall()
    ]


def get_annotations(con: sqlite3.Connection, item_id: int) -> List[Dict[str, Any]]:
    cur = con.cursor()
    cur.execute(
        """
        select ann.itemID, ann_item.key as annotationKey, parent_item.key as attachmentKey,
               ann.type, ann.authorName, ann.text, ann.comment, ann.color,
               ann.pageLabel, ann.sortIndex, ann.position
        from itemAnnotations ann
        join items ann_item on ann_item.itemID = ann.itemID
        join itemAttachments attach on attach.itemID = ann.parentItemID
        join items parent_item on parent_item.itemID = attach.itemID
        where attach.parentItemID = ?
        order by parent_item.key, ann.sortIndex
        """,
        (item_id,),
    )
    annotations = []
    for row in cur.fetchall():
        page = row["pageLabel"] or ""
        link = f"zotero://open-pdf/library/items/{row['attachmentKey']}"
        if page:
            link += f"?page={page}"
        annotations.append(
            {
                "itemID": row["itemID"],
                "annotationKey": row["annotationKey"],
                "attachmentKey": row["attachmentKey"],
                "type": row["type"],
                "text": clean_html(row["text"]),
                "comment": clean_html(row["comment"]),
                "color": row["color"],
                "pageLabel": page,
                "sortIndex": row["sortIndex"],
                "position": row["position"],
                "zotero_pdf_link": link,
            }
        )
    return annotations


def format_raw_buffer(record: Dict[str, Any]) -> str:
    meta = record["metadata"]
    lines = [
        "# Raw_Data_Buffer",
        "",
        "## Metadata",
        f"- Item Key: {meta.get('itemKey', '')}",
        f"- Title: {meta.get('title', '')}",
        f"- Year: {meta.get('year', '')}",
        f"- Publication: {meta.get('publicationTitle', '')}",
        f"- DOI: {meta.get('DOI', '')}",
        f"- Zotero Tags: {', '.join(record.get('zotero_tags', []))}",
        "",
        "## Abstract",
        meta.get("abstractNote", "") or "",
    ]
    if record.get("annotations"):
        lines.extend(["", "## Annotations"])
        for ann in record["annotations"]:
            text = ann.get("text") or ann.get("comment") or ""
            if text:
                lines.append(f"- p.{ann.get('pageLabel', '')} {text} ({ann.get('zotero_pdf_link', '')})")
    if record.get("notes"):
        lines.extend(["", "## Notes"])
        for note in record["notes"]:
            if note.get("text"):
                lines.append(note["text"])
    for att in record.get("attachments", []):
        cache_text = att.get("cache_text", "")
        if cache_text:
            lines.extend(["", f"## Fulltext Cache: {att.get('attachmentKey', '')}", cache_text])
    return "\n".join(lines).strip() + "\n"


def extract_record(
    con: sqlite3.Connection, item_id: int, storage_dir: Path, cache_chars: int
) -> Dict[str, Any]:
    item_summary = list_items(con, [item_id])[0]
    fields = item_fields(con, [item_id]).get(item_id, {})
    metadata = {key: fields.get(key, "") for key in TEXT_FIELDS}
    metadata.update(item_summary)
    metadata["year"] = extract_year(metadata.get("date", ""))

    record: Dict[str, Any] = {
        "metadata": metadata,
        "creators": get_creators(con, item_id),
        "zotero_tags": get_tags(con, item_id),
        "collections": collection_paths_for_item(con, item_id),
        "attachments": get_attachments(con, item_id, storage_dir, cache_chars),
        "notes": get_notes(con, item_id),
        "annotations": get_annotations(con, item_id),
    }
    record["pdf_keys"] = [
        att["attachmentKey"]
        for att in record["attachments"]
        if "pdf" in (att.get("contentType") or "").lower()
    ]
    record["raw_data_buffer"] = format_raw_buffer(record)
    return record


def main() -> None:
    args = build_parser().parse_args()
    config, config_path = load_config(args.config)
    _data_dir, sqlite_path, storage_dir = config_paths(config)
    with connect_zotero(sqlite_path) as con:
        item_ids = find_item_ids(con, args)
        records = [extract_record(con, item_id, storage_dir, args.cache_chars) for item_id in item_ids]
    result: Dict[str, Any] = {
        "config_path": str(config_path),
        "sqlite_path": str(sqlite_path),
        "storage_dir": str(storage_dir),
        "items": records,
    }
    dump_json(result, args.out)


if __name__ == "__main__":
    main()


