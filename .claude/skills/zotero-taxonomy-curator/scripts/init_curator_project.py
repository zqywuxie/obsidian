#!/usr/bin/env python3
"""Initialize a local Zotero Taxonomy Curator project.

The script creates a private local config, an empty taxonomy, a literature-note
template, and an output note folder. It tries to detect Zotero's local database
from environment variables, Zotero profile prefs, or common default locations.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


LOCAL_CONFIG_TEMPLATE = """zotero:
  sqlite_path: {sqlite_path}
  storage_dir: {storage_dir}

output:
  note_root: {note_root}
  index_file: {index_file}

taxonomy:
  path: {taxonomy_path}

template:
  path: {template_path}
"""


EMPTY_TAXONOMY = """version: "0.1.0"
domain:
  name: "my-research-domain"
  description: "Describe your research field here."

canonical_tag_style: lowercase-hyphen

base_tags:
  - literature-note
  - reading-note

usage_rules:
  principle: "Use the smallest set of stable tags that still supports retrieval, comparison, and review writing."
  evidence_required: true
  promote_candidate_when:
    - "The concept appears across multiple papers."
    - "The concept improves retrieval or comparison beyond existing tags."
    - "The concept is supported by explicit evidence in the paper."

categories:
  document_type:
    description: "Publication type. Add stable tags only when they are useful for retrieval."
    tags: {}

  research_topic:
    description: "Main domain topic, problem family, or research stream."
    tags: {}

  theory_or_framework:
    description: "Theory, conceptual framework, or analytical perspective."
    tags: {}

  method_family:
    description: "Methods, models, algorithms, or analytical approaches."
    tags: {}

  data_and_evidence:
    description: "Data source, evidence type, benchmark, case, or experiment design."
    tags: {}

  contribution_type:
    description: "Main contribution type."
    tags: {}

aliases: {}

candidate_terms: []
"""


def q(value: str) -> str:
    """Return a YAML double-quoted scalar."""
    return json.dumps(value.replace("\\", "/"), ensure_ascii=False)


def write_text(path: Path, text: str, overwrite: bool) -> bool:
    if path.exists() and not overwrite:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def decode_js_string(raw: str) -> str:
    try:
        return str(json.loads('"' + raw + '"'))
    except Exception:
        return raw.replace("\\\\", "\\").replace('\\"', '"')


def prefs_candidates() -> List[Path]:
    home = Path.home()
    candidates: List[Path] = []

    appdata = os.environ.get("APPDATA")
    if appdata:
        candidates.extend(Path(appdata).glob("Zotero/Zotero/Profiles/*/prefs.js"))

    candidates.extend((home / "AppData/Roaming/Zotero/Zotero/Profiles").glob("*/prefs.js"))
    candidates.extend((home / "Library/Application Support/Zotero/Profiles").glob("*/prefs.js"))
    candidates.extend((home / ".zotero/zotero").glob("*/prefs.js"))
    return [p for p in candidates if p.exists()]


def data_dirs_from_prefs() -> List[Path]:
    out: List[Path] = []
    pattern = re.compile(r'user_pref\("extensions\.zotero\.dataDir",\s*"((?:\\.|[^"\\])*)"\)')
    for prefs in prefs_candidates():
        try:
            text = prefs.read_text(encoding="utf-8-sig", errors="replace")
        except Exception:
            continue
        for match in pattern.finditer(text):
            value = decode_js_string(match.group(1))
            if value:
                out.append(Path(value).expanduser())
    return out


def env_candidates() -> List[Path]:
    out: List[Path] = []
    sqlite = os.environ.get("ZOTERO_SQLITE")
    data_dir = os.environ.get("ZOTERO_DATA_DIR")
    if sqlite:
        out.append(Path(sqlite).expanduser())
    if data_dir:
        out.append(Path(data_dir).expanduser() / "zotero.sqlite")
    return out


def default_candidates() -> List[Path]:
    home = Path.home()
    return [
        home / "Zotero" / "zotero.sqlite",
        home / "Zotero" / "backups" / "zotero.sqlite",
    ]


def detect_zotero_sqlite() -> Tuple[Optional[Path], List[str]]:
    checked: List[str] = []
    candidates: List[Path] = []
    candidates.extend(env_candidates())
    candidates.extend(d / "zotero.sqlite" for d in data_dirs_from_prefs())
    candidates.extend(default_candidates())

    seen = set()
    unique: List[Path] = []
    for path in candidates:
        key = str(path)
        if key not in seen:
            seen.add(key)
            unique.append(path)

    for path in unique:
        checked.append(str(path))
        if path.exists():
            return path.resolve(), checked
    return None, checked


def infer_storage_dir(sqlite_path: Optional[Path], explicit: Optional[str]) -> str:
    if explicit:
        return str(Path(explicit).expanduser())
    env_storage = os.environ.get("ZOTERO_STORAGE_DIR")
    if env_storage:
        return env_storage
    if sqlite_path is not None:
        storage = sqlite_path.parent / "storage"
        if storage.exists():
            return str(storage)
        return str(storage)
    return ""


def read_bundled_template() -> str:
    here = Path(__file__).resolve()
    template = here.parent.parent / "templates" / "literature-note-template.md"
    if template.exists():
        return template.read_text(encoding="utf-8-sig")
    return "# {{title}}\n\n## 基本信息\n\n## 一句话摘要\n"


def build_local_config(
    sqlite_path: str,
    storage_dir: str,
    note_root: str,
    index_file: str,
    taxonomy_path: str,
    template_path: str,
) -> str:
    return LOCAL_CONFIG_TEMPLATE.format(
        sqlite_path=q(sqlite_path),
        storage_dir=q(storage_dir),
        note_root=q(note_root),
        index_file=q(index_file),
        taxonomy_path=q(taxonomy_path),
        template_path=q(template_path),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize a Zotero Taxonomy Curator project.")
    parser.add_argument("--project-root", default=".", help="Project root where config/templates/notes will be created.")
    parser.add_argument("--zotero-sqlite", help="Explicit path to zotero.sqlite.")
    parser.add_argument("--zotero-storage", help="Explicit path to Zotero storage directory.")
    parser.add_argument("--note-root", default="notes/literature", help="Output folder for literature notes.")
    parser.add_argument("--index-file", default="notes/literature/Literature Index.md", help="Literature index path.")
    parser.add_argument("--local-config", default="config/local.yaml", help="Private local config path.")
    parser.add_argument("--taxonomy", default="config/taxonomy.yaml", help="Taxonomy path to initialize.")
    parser.add_argument("--template", default="templates/literature-note-template.md", help="Project-level note template path.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing local config, taxonomy, and template.")
    parser.add_argument("--no-auto-detect", action="store_true", help="Do not try to detect Zotero paths.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    project_root.mkdir(parents=True, exist_ok=True)

    detected: Optional[Path] = None
    checked: List[str] = []
    if args.zotero_sqlite:
        detected = Path(args.zotero_sqlite).expanduser().resolve()
    elif not args.no_auto_detect:
        detected, checked = detect_zotero_sqlite()

    sqlite_value = str(detected) if detected is not None else ""
    storage_value = infer_storage_dir(detected, args.zotero_storage)

    note_root = Path(args.note_root)
    index_file = Path(args.index_file)
    taxonomy_path = Path(args.taxonomy)
    local_config_path = Path(args.local_config)
    template_path = Path(args.template)

    created: List[str] = []
    skipped: List[str] = []

    if write_text(project_root / taxonomy_path, EMPTY_TAXONOMY, args.overwrite):
        created.append(str(taxonomy_path))
    else:
        skipped.append(str(taxonomy_path))

    template_text = read_bundled_template()
    if write_text(project_root / template_path, template_text, args.overwrite):
        created.append(str(template_path))
    else:
        skipped.append(str(template_path))

    local_config = build_local_config(
        sqlite_path=sqlite_value,
        storage_dir=storage_value,
        note_root=str(note_root),
        index_file=str(index_file),
        taxonomy_path=str(taxonomy_path),
        template_path=str(template_path),
    )
    if write_text(project_root / local_config_path, local_config, args.overwrite):
        created.append(str(local_config_path))
    else:
        skipped.append(str(local_config_path))

    (project_root / note_root).mkdir(parents=True, exist_ok=True)
    created.append(str(note_root) + "/")

    if not (project_root / index_file).exists():
        write_text(project_root / index_file, "# Literature Index\n\n", False)
        created.append(str(index_file))

    print("Initialized Zotero Taxonomy Curator project")
    print("Project root:", project_root)
    print("Created or ensured:")
    for item in created:
        print("-", item)
    if skipped:
        print("Skipped existing files:")
        for item in skipped:
            print("-", item)
    if sqlite_value:
        print("Zotero sqlite:", sqlite_value)
        print("Zotero storage:", storage_value)
    else:
        print("WARNING: Zotero sqlite was not detected.")
        print("Edit", str(local_config_path), "and set zotero.sqlite_path and zotero.storage_dir.")
        if checked:
            print("Checked paths:")
            for item in checked:
                print("-", item)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
