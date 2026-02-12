# 寵物植物毒性資料庫

> **一個完整的開源資料庫，聚焦對寵物有毒的室內植物，提供器官層級毒性評級、誤診案例研究與環境自適應照護方案。**

## 語言

預設語言：**英文** (`README.md`)

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Español](README.es.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

> 本文件為主文件的翻譯版本，最新且權威內容以英文版為準。

## 專案概覽

許多植物辨識工具僅以「有毒/無毒」二分法描述寵物風險，實務上並不足夠。

本資料庫提供更細緻的資料：
- 依植物器官區分（葉、莖、花粉、汁液等）
- 依攝取劑量與寵物體型區分
- 依毒性作用機制區分
- 依實際暴露情境區分

## 核心文件

### 寵物毒性報告

- [Aloe Vera Anthraquinone Risk](pet-toxicity/aloe-vera-anthraquinone-risk.md)
- [Azalea Grayanotoxin Cardiac Risk](pet-toxicity/azalea-grayanotoxin-cardiac-risk.md)
- [Lily Cat Toxicity](pet-toxicity/lily-cat-toxicity.md)
- [Pothos Hidden Toxicity](pet-toxicity/pothos-hidden-toxicity.md)

### 誤診案例

- [Fungal Leaf Spot vs Sunburn](misdiagnosis/fungal-leaf-spot-vs-sunburn.md)
- [Spider Mites vs Dust](misdiagnosis/spider-mites-vs-dust.md)
- [Root Rot vs Underwatering](misdiagnosis/root-rot-vs-underwatering.md)
- [Scale Insects vs Mineral Residue](misdiagnosis/scale-insects-vs-mineral-residue.md)

### 動態照護協議

- [Fiddle-Leaf Fig Moist Soil Myth](care-protocols/fiddle-leaf-fig-moist-soil-myth.md)
- [Monstera Watering Myth](care-protocols/monstera-watering-myth.md)


<!-- BEGIN AUTO-GENERATED-INDEX-REF -->
## 完整文章索引

本翻譯版 README 保留精簡概覽，完整的自動生成索引維護於主文件中。

- 寵物毒性報告：216
- 誤診案例研究：190
- 動態養護協議：164
- 完整索引：[README.md#full-generated-article-index](README.md#full-generated-article-index)

<!-- END AUTO-GENERATED-INDEX-REF -->

## 關鍵概念

- **PAWS (Pet-Aware Warning System)**：器官層級、依寵物體型校正的多維毒性風險評估
- **PF-BRI (PlantFun Bio-Rhythm Index)**：基於 VPD（蒸氣壓差）的動態澆水建議
- **Micro-distance Pathological Algorithm**：早期區分生物性與非生物性壓力

## 資料方法學

1. 器官層級毒性解析
2. 毒性機制記錄
3. 貓犬差異化風險評估
4. 以證據為基礎的資料基準
5. 每季更新維護

## 參與貢獻

歡迎貢獻，請參考 [CONTRIBUTING.md](CONTRIBUTING.md)。

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

## 授權

本專案採用 [CC0 1.0 Universal](LICENSE) 授權。
