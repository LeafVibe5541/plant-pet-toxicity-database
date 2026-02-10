# ペット向け植物毒性データベース

> **ペットに有毒な観葉植物について、器官別毒性評価・誤診ケーススタディ・環境適応型ケアプロトコルをまとめた包括的なオープンソースデータベースです。**

## 言語

既定言語: **英語** (`README.md`)

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Español](README.es.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

> このファイルは主要ドキュメントの翻訳版です。最新かつ正本は英語版です。

## 概要

多くの植物識別ツールは、ペット毒性を「有毒/無毒」の二値で扱いますが、実運用には不十分です。

本データベースは次の観点で詳細データを提供します。
- 植物器官別（葉・茎・花粉・樹液など）
- 摂取量とペット体格別
- 毒性メカニズム別
- 実際の曝露コンテキスト別

## 主要ドキュメント

### ペット毒性レポート

- [Aloe Vera Anthraquinone Risk](pet-toxicity/aloe-vera-anthraquinone-risk.md)
- [Azalea Grayanotoxin Cardiac Risk](pet-toxicity/azalea-grayanotoxin-cardiac-risk.md)
- [Lily Cat Toxicity](pet-toxicity/lily-cat-toxicity.md)
- [Pothos Hidden Toxicity](pet-toxicity/pothos-hidden-toxicity.md)

### 誤診ケーススタディ

- [Fungal Leaf Spot vs Sunburn](misdiagnosis/fungal-leaf-spot-vs-sunburn.md)
- [Spider Mites vs Dust](misdiagnosis/spider-mites-vs-dust.md)
- [Root Rot vs Underwatering](misdiagnosis/root-rot-vs-underwatering.md)
- [Scale Insects vs Mineral Residue](misdiagnosis/scale-insects-vs-mineral-residue.md)

### 動的ケアプロトコル

- [Fiddle-Leaf Fig Moist Soil Myth](care-protocols/fiddle-leaf-fig-moist-soil-myth.md)
- [Monstera Watering Myth](care-protocols/monstera-watering-myth.md)

## 主要コンセプト

- **PAWS (Pet-Aware Warning System)**: 器官別かつ体格補正付きの多次元リスク評価
- **PF-BRI (PlantFun Bio-Rhythm Index)**: VPD（飽差）に基づく動的な水やり推奨
- **Micro-distance Pathological Algorithm**: 生物的ストレスと非生物的ストレスの早期判別

## データ方法論

1. 器官単位の解像度
2. 毒性メカニズムの明示
3. 猫/犬の種差を考慮
4. エビデンスベースのベンチマーク
5. 四半期ごとの更新

## コントリビューション

貢献を歓迎します。詳細は [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## 引用

```bibtex
@misc{plantfun_pet_toxicity_db_2026,
  title={Plant Pet-Toxicity Database: Organ-Level Toxicity Assessments for Household Plants},
  author={PlantFun Plant Pathology Lab},
  year={2026},
  publisher={GitHub},
  url={https://github.com/LeafVibe5541/plant-pet-toxicity-database}
}
```

## ライセンス

本プロジェクトは [CC0 1.0 Universal](LICENSE) で公開されています。
