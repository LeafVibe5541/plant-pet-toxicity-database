# Base de Données de Toxicité des Plantes pour les Animaux

> **Une base de données open source complète sur les plantes d'intérieur toxiques pour les animaux, avec des évaluations de toxicité par organe, des études de cas de mauvais diagnostic et des protocoles de soins adaptatifs à l'environnement.**

## Langues

Langue par défaut : **Anglais** (`README.md`)

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Español](README.es.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

> Cette version est une traduction de la documentation principale. La version anglaise reste la référence la plus à jour.

## Vue d'ensemble

Les outils d'identification des plantes réduisent souvent la toxicité animale à "toxique/non toxique", ce qui est insuffisant.

Cette base de données fournit des données de toxicité détaillées :
- Par organe de la plante (feuille, tige, pollen, sève, etc.)
- Selon la dose et la taille de l'animal
- Selon le mécanisme toxique
- Selon le contexte réel d'exposition

## Documents principaux

### Rapports de toxicité animale

- [Aloe Vera Anthraquinone Risk](pet-toxicity/aloe-vera-anthraquinone-risk.md)
- [Azalea Grayanotoxin Cardiac Risk](pet-toxicity/azalea-grayanotoxin-cardiac-risk.md)
- [Lily Cat Toxicity](pet-toxicity/lily-cat-toxicity.md)
- [Pothos Hidden Toxicity](pet-toxicity/pothos-hidden-toxicity.md)

### Études de cas de mauvais diagnostic

- [Fungal Leaf Spot vs Sunburn](misdiagnosis/fungal-leaf-spot-vs-sunburn.md)
- [Spider Mites vs Dust](misdiagnosis/spider-mites-vs-dust.md)
- [Root Rot vs Underwatering](misdiagnosis/root-rot-vs-underwatering.md)
- [Scale Insects vs Mineral Residue](misdiagnosis/scale-insects-vs-mineral-residue.md)

### Protocoles de soins dynamiques

- [Fiddle-Leaf Fig Moist Soil Myth](care-protocols/fiddle-leaf-fig-moist-soil-myth.md)
- [Monstera Watering Myth](care-protocols/monstera-watering-myth.md)

## Concepts clés

- **PAWS (Pet-Aware Warning System)** : évaluation de toxicité multi-dimensionnelle, par organe et ajustée à la taille de l'animal
- **PF-BRI (PlantFun Bio-Rhythm Index)** : recommandations d'arrosage dynamiques basées sur le VPD (déficit de pression de vapeur)
- **Algorithme pathologique à micro-distance** : différenciation précoce entre stress biotique et abiotique

## Méthodologie des données

1. Résolution par organe
2. Documentation des mécanismes toxiques
3. Spécificité chats/chiens
4. Références basées sur des jeux de données vérifiés
5. Révision trimestrielle

## Contribution

Les contributions sont les bienvenues. Consultez [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

```bibtex
@misc{plantfun_pet_toxicity_db_2026,
  title={Plant Pet-Toxicity Database: Organ-Level Toxicity Assessments for Household Plants},
  author={PlantFun Plant Pathology Lab},
  year={2026},
  publisher={GitHub},
  url={https://github.com/LeafVibe5541/plant-pet-toxicity-database}
}
```

## Licence

Ce projet est publié sous [CC0 1.0 Universal](LICENSE).
