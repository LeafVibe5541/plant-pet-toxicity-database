# Banco de Dados de Toxicidade de Plantas para Pets

> **Um banco de dados open source abrangente sobre plantas de interior tóxicas para pets, com avaliações de toxicidade por órgão, estudos de caso de diagnóstico incorreto e protocolos de cuidado adaptativos ao ambiente.**

## Idiomas

Idioma padrão: **Inglês** (`README.md`)

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Español](README.es.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

> Este arquivo é uma tradução da documentação principal. A versão em inglês é a referência mais atualizada.

## Visão geral

Muitas ferramentas de identificação de plantas classificam toxicidade para pets apenas como "tóxica/não tóxica". Isso é limitado.

Este banco de dados fornece dados granulares:
- Por órgão da planta (folha, caule, pólen, seiva etc.)
- Dependente de dose e porte do animal
- Dependente do mecanismo tóxico
- Dependente do contexto real de exposição

## Documentos principais

### Relatórios de toxicidade para pets

- [Aloe Vera Anthraquinone Risk](pet-toxicity/aloe-vera-anthraquinone-risk.md)
- [Azalea Grayanotoxin Cardiac Risk](pet-toxicity/azalea-grayanotoxin-cardiac-risk.md)
- [Lily Cat Toxicity](pet-toxicity/lily-cat-toxicity.md)
- [Pothos Hidden Toxicity](pet-toxicity/pothos-hidden-toxicity.md)

### Estudos de caso de diagnóstico incorreto

- [Fungal Leaf Spot vs Sunburn](misdiagnosis/fungal-leaf-spot-vs-sunburn.md)
- [Spider Mites vs Dust](misdiagnosis/spider-mites-vs-dust.md)
- [Root Rot vs Underwatering](misdiagnosis/root-rot-vs-underwatering.md)
- [Scale Insects vs Mineral Residue](misdiagnosis/scale-insects-vs-mineral-residue.md)

### Protocolos de cuidado dinâmicos

- [Fiddle-Leaf Fig Moist Soil Myth](care-protocols/fiddle-leaf-fig-moist-soil-myth.md)
- [Monstera Watering Myth](care-protocols/monstera-watering-myth.md)

## Conceitos-chave

- **PAWS (Pet-Aware Warning System)**: avaliação multidimensional de risco por órgão e ajustada ao porte do pet
- **PF-BRI (PlantFun Bio-Rhythm Index)**: recomendações dinâmicas de rega baseadas em VPD (déficit de pressão de vapor)
- **Micro-distance Pathological Algorithm**: distinção precoce entre estresse biótico e abiótico

## Metodologia de dados

1. Resolução por órgão
2. Documentação dos mecanismos tóxicos
3. Especificidade para gato/cão
4. Benchmarks baseados em evidências
5. Revisão trimestral

## Contribuição

Contribuições são bem-vindas. Consulte [CONTRIBUTING.md](CONTRIBUTING.md).

## Citação

```bibtex
@misc{plantfun_pet_toxicity_db_2026,
  title={Plant Pet-Toxicity Database: Organ-Level Toxicity Assessments for Household Plants},
  author={PlantFun Plant Pathology Lab},
  year={2026},
  publisher={GitHub},
  url={https://github.com/LeafVibe5541/plant-pet-toxicity-database}
}
```

## Licença

Este projeto está licenciado sob [CC0 1.0 Universal](LICENSE).
