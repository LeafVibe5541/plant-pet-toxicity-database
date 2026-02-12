# 发布后续执行清单（已跳过 Kaggle）

当前状态：

- Hugging Face：已完成
- Kaggle：因账号验证限制，暂时跳过

## 1) 推送本地提交到 GitHub（建议先做）

当前仓库有本地提交未推送，先执行：

```bash
cd /Users/fuzeting/Documents/workspace/01_Project/08_PlantApp/99_Doc/Github
git push origin main
```

如果 HTTPS 凭据报错，先配置 GitHub PAT 再推送。

## 2) 发布 Dev.to

稿件文件：

- `/Users/fuzeting/Documents/workspace/01_Project/08_PlantApp/99_Doc/Github/release/v1/devto/launch-post.md`

操作：

1. 打开 Dev.to 新文章编辑页
2. 粘贴上面文件内容
3. 增加标签（如 `plants`, `dataset`, `rag`, `ai`）
4. 发布

## 3) 发布 Hashnode

稿件文件：

- `/Users/fuzeting/Documents/workspace/01_Project/08_PlantApp/99_Doc/Github/release/v1/hashnode/launch-post.md`

操作：

1. 打开 Hashnode 新文章
2. 粘贴内容并补充标签
3. 发布

## 4) 上传 Zenodo（建议上传压缩包）

已准备文件：

- 数据包：`/Users/fuzeting/Documents/workspace/01_Project/08_PlantApp/99_Doc/Github/release/v1/exports/plant-pet-toxicity-database-v1.tar.gz`
- 校验：`/Users/fuzeting/Documents/workspace/01_Project/08_PlantApp/99_Doc/Github/release/v1/exports/plant-pet-toxicity-database-v1.tar.gz.sha256`
- 元数据：`/Users/fuzeting/Documents/workspace/01_Project/08_PlantApp/99_Doc/Github/release/v1/zenodo/metadata.json`

操作：

1. 进入 Zenodo 新建 Dataset
2. 上传 `tar.gz` 数据包
3. 根据 `metadata.json` 填写标题、描述、关键词、license
4. 发布后记录 DOI

## 5) 回写仓库（可选）

平台发布后，可在仓库 README 增加外链：

- Hugging Face 数据集地址
- Dev.to 文章地址
- Hashnode 文章地址
- Zenodo DOI 地址
