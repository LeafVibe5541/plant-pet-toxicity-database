# 宠物植物毒性数据库

> **一个全面的开源数据库，聚焦对宠物有毒的室内植物，提供器官级毒性评级、误诊案例研究与环境自适应养护方案。**

## 语言

默认语言：**英语** (`README.md`)

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Español](README.es.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

> 本文件是主文档的翻译版本，最新且权威的版本为英文文档。

## 项目概览

很多植物识别工具仅用“有毒/无毒”二分类描述宠物风险，这在真实场景中远远不够。

本数据库提供更细粒度的数据：
- 按植物器官区分（叶、茎、花粉、汁液等）
- 按摄入剂量与宠物体型区分
- 按毒性作用机制区分
- 按真实暴露场景区分

## 核心文档

### 宠物毒性报告

- [Aloe Vera Anthraquinone Risk](pet-toxicity/aloe-vera-anthraquinone-risk.md)
- [Azalea Grayanotoxin Cardiac Risk](pet-toxicity/azalea-grayanotoxin-cardiac-risk.md)
- [Lily Cat Toxicity](pet-toxicity/lily-cat-toxicity.md)
- [Pothos Hidden Toxicity](pet-toxicity/pothos-hidden-toxicity.md)

### 误诊案例

- [Fungal Leaf Spot vs Sunburn](misdiagnosis/fungal-leaf-spot-vs-sunburn.md)
- [Spider Mites vs Dust](misdiagnosis/spider-mites-vs-dust.md)
- [Root Rot vs Underwatering](misdiagnosis/root-rot-vs-underwatering.md)
- [Scale Insects vs Mineral Residue](misdiagnosis/scale-insects-vs-mineral-residue.md)

### 动态养护协议

- [Fiddle-Leaf Fig Moist Soil Myth](care-protocols/fiddle-leaf-fig-moist-soil-myth.md)
- [Monstera Watering Myth](care-protocols/monstera-watering-myth.md)


<!-- BEGIN AUTO-GENERATED-INDEX-REF -->
## 完整文章索引

本翻译版 README 保留精简概览，完整的自动生成索引维护在主文档中。

- 宠物毒性报告：216
- 误诊案例研究：190
- 动态养护协议：164
- 完整索引：[README.md#full-generated-article-index](README.md#full-generated-article-index)

<!-- END AUTO-GENERATED-INDEX-REF -->

## 关键概念

- **PAWS (Pet-Aware Warning System)**：器官级、按宠物体型校准的多维毒性风险评估
- **PF-BRI (PlantFun Bio-Rhythm Index)**：基于 VPD（蒸汽压亏缺）的动态浇水建议
- **Micro-distance Pathological Algorithm**：在早期区分生物胁迫与非生物胁迫

## 数据方法学

1. 器官级毒性解析
2. 毒性机制记录
3. 猫犬差异化风险评估
4. 基于证据的数据基准
5. 按季度更新维护

## 参与贡献

欢迎贡献，请查看 [CONTRIBUTING.md](CONTRIBUTING.md)。

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

## 许可证

本项目采用 [CC0 1.0 Universal](LICENSE) 许可。
