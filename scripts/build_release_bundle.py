#!/usr/bin/env python3
"""Build a release bundle for multi-platform distribution.

Outputs:
- release/v1/articles.csv
- release/v1/articles.jsonl
- release/v1/manifest.json
- release/v1/huggingface/README.md
- release/v1/kaggle/dataset-metadata.json
- release/v1/kaggle/README.md
- release/v1/devto/launch-post.md
- release/v1/hashnode/launch-post.md
- release/v1/zenodo/metadata.json
- release/v1/README.md
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

CONTENT_DIRS = {
    "pet-toxicity": "Pet Toxicity Reports",
    "misdiagnosis": "Misdiagnosis Case Studies",
    "care-protocols": "Dynamic Care Protocols",
}

LANG_SUFFIX_RE = re.compile(r"\.(en|de|fr|es|it|pt|ja|ko|zh-CN|zh-TW)$", re.IGNORECASE)


def now_utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def detect_language(stem: str) -> str:
    match = LANG_SUFFIX_RE.search(stem)
    return match.group(1) if match else "unspecified"


def strip_lang_suffix(stem: str) -> str:
    return LANG_SUFFIX_RE.sub("", stem)


def extract_title(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
    except OSError:
        pass
    return strip_lang_suffix(path.stem).replace("-", " ").strip()


def collect_articles(root: Path) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for folder, category in CONTENT_DIRS.items():
        folder_path = root / folder
        if not folder_path.exists():
            continue
        for path in sorted(folder_path.glob("*.md"), key=lambda p: p.name.lower()):
            stem = path.stem
            language = detect_language(stem)
            slug = strip_lang_suffix(stem)
            items.append(
                {
                    "path": f"{folder}/{path.name}",
                    "filename": path.name,
                    "category": category,
                    "folder": folder,
                    "language": language,
                    "slug": slug,
                    "title": extract_title(path),
                }
            )
    return items


def write_csv(path: Path, rows: Iterable[dict[str, str]]) -> None:
    rows = list(rows)
    fieldnames = ["path", "filename", "folder", "category", "language", "slug", "title"]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_jsonl(path: Path, rows: Iterable[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def build_platform_files(release_dir: Path, repo_url: str, manifest: dict) -> None:
    counts_by_category = manifest["counts_by_category"]
    counts_by_language = manifest["counts_by_language"]
    total = manifest["total_articles"]
    generated_at = manifest["generated_at_utc"]

    hf_dir = release_dir / "huggingface"
    hf_dir.mkdir(parents=True, exist_ok=True)
    hf_readme = f"""---
license: cc0-1.0
task_categories:
- text-classification
- summarization
language:
- en
- zh
- de
- fr
- es
pretty_name: Plant Pet-Toxicity GEO Corpus
size_categories:
- 100K<n<1M
---

# Plant Pet-Toxicity GEO Corpus (v1)

This dataset is exported from `{repo_url}`.

## Snapshot

- Generated at: `{generated_at}`
- Total markdown articles: `{total}`
- Pet Toxicity Reports: `{counts_by_category.get('Pet Toxicity Reports', 0)}`
- Misdiagnosis Case Studies: `{counts_by_category.get('Misdiagnosis Case Studies', 0)}`
- Dynamic Care Protocols: `{counts_by_category.get('Dynamic Care Protocols', 0)}`

## Files

- `../articles.csv`
- `../articles.jsonl`
- `../manifest.json`

## Suggested usage

- Retrieval benchmarking for plant toxicity and diagnosis content.
- Multilingual indexing and GEO citation analysis.
- Controlled comparisons of rule-based vs LLM summarization behavior.

## Data source

All content is maintained in the public repository and released under CC0.
"""
    (hf_dir / "README.md").write_text(hf_readme, encoding="utf-8")

    kaggle_dir = release_dir / "kaggle"
    kaggle_dir.mkdir(parents=True, exist_ok=True)
    kaggle_meta = {
        "title": "Plant Pet-Toxicity GEO Corpus v1",
        "id": "leafvibe5541/plant-pet-toxicity-geo-corpus-v1",
        "licenses": [{"name": "CC0-1.0"}],
        "subtitle": "Organ-level toxicity, misdiagnosis, and dynamic care markdown corpus",
        "description": (
            "Multilingual markdown corpus exported from the Plant Pet-Toxicity Database. "
            "Includes pet toxicity reports, AI misdiagnosis case studies, and VPD-based care protocols."
        ),
        "keywords": [
            "plant",
            "pet safety",
            "toxicity",
            "diagnosis",
            "horticulture",
            "multilingual",
        ],
        "isPrivate": False,
        "collaborators": [],
        "data": [{"description": "article metadata and paths", "name": "articles.csv"}],
    }
    (kaggle_dir / "dataset-metadata.json").write_text(json.dumps(kaggle_meta, ensure_ascii=False, indent=2), encoding="utf-8")

    kaggle_readme = f"""# Plant Pet-Toxicity GEO Corpus (Kaggle)

## Export snapshot

- Generated at: `{generated_at}`
- Total markdown articles: `{total}`

## Category counts

- Pet Toxicity Reports: `{counts_by_category.get('Pet Toxicity Reports', 0)}`
- Misdiagnosis Case Studies: `{counts_by_category.get('Misdiagnosis Case Studies', 0)}`
- Dynamic Care Protocols: `{counts_by_category.get('Dynamic Care Protocols', 0)}`

## Language counts

{os_lines(counts_by_language)}

## Source repository

- {repo_url}
"""
    (kaggle_dir / "README.md").write_text(kaggle_readme, encoding="utf-8")

    devto_dir = release_dir / "devto"
    devto_dir.mkdir(parents=True, exist_ok=True)
    devto_post = f"""# We Published a 1,300+ Article Plant Safety Corpus for GEO and Retrieval Testing

We have open-sourced a multilingual plant content corpus focused on:

- Organ-level pet toxicity triage
- AI misdiagnosis correction protocols
- VPD-based dynamic care guidance

## Snapshot

- Total articles: **{total}**
- Pet Toxicity Reports: **{counts_by_category.get('Pet Toxicity Reports', 0)}**
- Misdiagnosis Case Studies: **{counts_by_category.get('Misdiagnosis Case Studies', 0)}**
- Dynamic Care Protocols: **{counts_by_category.get('Dynamic Care Protocols', 0)}**

Repo: {repo_url}

If you are evaluating RAG quality in safety-heavy domains, this dataset is useful for:

1. citation consistency checks,
2. multilingual retrieval behavior,
3. hallucination guardrail tests.
"""
    (devto_dir / "launch-post.md").write_text(devto_post, encoding="utf-8")

    hashnode_dir = release_dir / "hashnode"
    hashnode_dir.mkdir(parents=True, exist_ok=True)
    hashnode_post = f"""# Building a Plant Safety GEO Corpus (with 1,300+ Articles)

This week we packaged our full PlantFun content corpus for cross-platform distribution.

## What is included

- Toxicology-focused pet safety articles
- AI misdiagnosis differential case studies
- Environment-adaptive care protocols

## Current dataset size

- Total: **{total}**
- Pet Toxicity Reports: **{counts_by_category.get('Pet Toxicity Reports', 0)}**
- Misdiagnosis Case Studies: **{counts_by_category.get('Misdiagnosis Case Studies', 0)}**
- Dynamic Care Protocols: **{counts_by_category.get('Dynamic Care Protocols', 0)}**

Repository: {repo_url}
"""
    (hashnode_dir / "launch-post.md").write_text(hashnode_post, encoding="utf-8")

    zenodo_dir = release_dir / "zenodo"
    zenodo_dir.mkdir(parents=True, exist_ok=True)
    zenodo_metadata = {
        "title": "Plant Pet-Toxicity GEO Corpus v1",
        "upload_type": "dataset",
        "description": "Multilingual markdown corpus for plant toxicity, diagnosis, and dynamic care GEO studies.",
        "creators": [{"name": "PlantFun Plant Pathology Lab"}],
        "access_right": "open",
        "license": "cc0-1.0",
        "keywords": ["plant", "pet", "toxicity", "diagnosis", "vpd", "geo"],
        "related_identifiers": [{"identifier": repo_url, "relation": "isSupplementTo", "scheme": "url"}],
        "notes": f"Auto-generated release metadata at {generated_at}.",
    }
    (zenodo_dir / "metadata.json").write_text(json.dumps(zenodo_metadata, ensure_ascii=False, indent=2), encoding="utf-8")


def os_lines(counter: dict[str, int]) -> str:
    lines = []
    for k in sorted(counter):
        lines.append(f"- {k}: {counter[k]}")
    return "\n".join(lines)


def write_release_readme(path: Path, manifest: dict) -> None:
    text = f"""# Release Bundle v1

Generated at: `{manifest['generated_at_utc']}`
Repository: `{manifest['repository_url']}`

## Contents

- `articles.csv` and `articles.jsonl`: article inventory exported from markdown files.
- `manifest.json`: snapshot metadata and aggregate counts.
- `huggingface/README.md`: Dataset Card draft.
- `kaggle/dataset-metadata.json`: Kaggle upload metadata.
- `kaggle/README.md`: Kaggle dataset description.
- `devto/launch-post.md`: Dev.to launch draft.
- `hashnode/launch-post.md`: Hashnode launch draft.
- `zenodo/metadata.json`: Zenodo metadata draft.

## Snapshot

- Total articles: `{manifest['total_articles']}`
- Pet Toxicity Reports: `{manifest['counts_by_category'].get('Pet Toxicity Reports', 0)}`
- Misdiagnosis Case Studies: `{manifest['counts_by_category'].get('Misdiagnosis Case Studies', 0)}`
- Dynamic Care Protocols: `{manifest['counts_by_category'].get('Dynamic Care Protocols', 0)}`

## Rebuild

```bash
python3 scripts/build_release_bundle.py --repo-url {manifest['repository_url']}
```
"""
    path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build release bundle for distribution platforms.")
    parser.add_argument(
        "--repo-url",
        default="https://github.com/LeafVibe5541/plant-pet-toxicity-database",
        help="Public repository URL included in generated metadata.",
    )
    parser.add_argument(
        "--output",
        default="release/v1",
        help="Output directory for release bundle.",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    out_dir = root / args.output
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = collect_articles(root)
    rows = sorted(rows, key=lambda x: x["path"].lower())

    write_csv(out_dir / "articles.csv", rows)
    write_jsonl(out_dir / "articles.jsonl", rows)

    category_counter = Counter(item["category"] for item in rows)
    language_counter = Counter(item["language"] for item in rows)

    manifest = {
        "generated_at_utc": now_utc_iso(),
        "repository_url": args.repo_url,
        "total_articles": len(rows),
        "counts_by_category": dict(sorted(category_counter.items())),
        "counts_by_language": dict(sorted(language_counter.items())),
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    build_platform_files(out_dir, args.repo_url, manifest)
    write_release_readme(out_dir / "README.md", manifest)

    print("Release bundle built:", out_dir)
    print("Total articles:", manifest["total_articles"])
    print("By category:", manifest["counts_by_category"])
    print("By language:", manifest["counts_by_language"])


if __name__ == "__main__":
    main()
