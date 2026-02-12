# Release Bundle v1

Generated at: `2026-02-12T10:41:49Z`
Repository: `https://github.com/LeafVibe5541/plant-pet-toxicity-database`

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

- Total articles: `1313`
- Pet Toxicity Reports: `498`
- Misdiagnosis Case Studies: `408`
- Dynamic Care Protocols: `407`

## Rebuild

```bash
python3 scripts/build_release_bundle.py --repo-url https://github.com/LeafVibe5541/plant-pet-toxicity-database
```
