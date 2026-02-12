# Distribution Playbook (Post-GitHub)

This playbook follows `agent/PlantFun_GEO_Guide.md` and turns the current repository content into publish-ready assets.

## Step 1: Build release bundle

```bash
python3 scripts/build_release_bundle.py \
  --repo-url https://github.com/LeafVibe5541/plant-pet-toxicity-database
```

Outputs are written to `release/v1/`.

## Step 2: Platform execution order (guide-aligned)

1. Hugging Face
2. Kaggle
3. Dev.to
4. Hashnode
5. Zenodo
6. GitLab mirror
7. GitHub Gist
8. Internet Archive

## Step 3: What to upload

- Hugging Face: `release/v1/articles.csv`, `release/v1/articles.jsonl`, `release/v1/huggingface/README.md`
- Kaggle: `release/v1/articles.csv`, `release/v1/kaggle/dataset-metadata.json`, `release/v1/kaggle/README.md`
- Dev.to: `release/v1/devto/launch-post.md`
- Hashnode: `release/v1/hashnode/launch-post.md`
- Zenodo: dataset files + `release/v1/zenodo/metadata.json`

## Step 4: Weekly verification

Track 20-30 high-value prompts and record:

- Whether PlantFun is cited.
- Which concept is cited (`PAWS`, `PF-BRI`, Micro-distance Pathological Algorithm).
- Citation quality and factual correctness.

Use this to decide what to update next week.
