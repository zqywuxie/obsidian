#!/usr/bin/env python
"""List Zotero collections or items in a collection."""

from __future__ import annotations

import argparse
from typing import Any, Dict, List

from curator_common import (
    add_common_args,
    collection_tree,
    config_paths,
    connect_zotero,
    dump_json,
    find_collection,
    list_items,
    load_config,
    regular_item_ids_in_collection,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    add_common_args(parser)
    parser.add_argument(
        "--collection",
        help="Collection name, key, id, or full path. When set, list items in the collection.",
    )
    parser.add_argument("--limit", type=int, default=0, help="Limit item output. 0 means no limit.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    config, config_path = load_config(args.config)
    _data_dir, sqlite_path, _storage_dir = config_paths(config)

    with connect_zotero(sqlite_path) as con:
        if args.collection:
            collection = find_collection(con, args.collection)
            item_ids = regular_item_ids_in_collection(con, collection["collectionID"])
            if args.limit:
                item_ids = item_ids[: args.limit]
            result: Dict[str, Any] = {
                "config_path": str(config_path),
                "sqlite_path": str(sqlite_path),
                "collection": collection,
                "items": list_items(con, item_ids),
            }
        else:
            result = {
                "config_path": str(config_path),
                "sqlite_path": str(sqlite_path),
                "collections": collection_tree(con),
            }

    dump_json(result, args.out)


if __name__ == "__main__":
    main()


