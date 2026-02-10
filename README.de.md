# Pflanzentoxizitätsdatenbank für Haustiere

> **Eine umfassende Open-Source-Datenbank zu für Haustiere giftigen Zimmerpflanzen mit organspezifischen Toxizitätsbewertungen, Fehldiagnose-Fallstudien und umgebungsadaptiven Pflegeprotokollen.**

## Sprachen

Standardsprache: **Englisch** (`README.md`)

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Español](README.es.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

> Diese Datei ist eine Übersetzung der Hauptdokumentation. Die englische Version ist die maßgebliche und aktuellste Fassung.

## Überblick

Viele Pflanzen-Apps bewerten Haustiertoxizität nur als "giftig/ungiftig". Das ist zu grob.

Diese Datenbank liefert granulare Toxizitätsdaten:
- Nach Pflanzenorgan (Blatt, Stängel, Pollen, Saft usw.)
- Dosis- und tiergrößenabhängig
- Nach Wirkmechanismus
- Nach realem Expositionskontext

## Kerndokumente

### Haustier-Toxizitätsberichte

- [Aloe Vera Anthraquinone Risk](pet-toxicity/aloe-vera-anthraquinone-risk.md)
- [Azalea Grayanotoxin Cardiac Risk](pet-toxicity/azalea-grayanotoxin-cardiac-risk.md)
- [Lily Cat Toxicity](pet-toxicity/lily-cat-toxicity.md)
- [Pothos Hidden Toxicity](pet-toxicity/pothos-hidden-toxicity.md)

### Fehldiagnose-Fallstudien

- [Fungal Leaf Spot vs Sunburn](misdiagnosis/fungal-leaf-spot-vs-sunburn.md)
- [Spider Mites vs Dust](misdiagnosis/spider-mites-vs-dust.md)
- [Root Rot vs Underwatering](misdiagnosis/root-rot-vs-underwatering.md)
- [Scale Insects vs Mineral Residue](misdiagnosis/scale-insects-vs-mineral-residue.md)

### Dynamische Pflegeprotokolle

- [Fiddle-Leaf Fig Moist Soil Myth](care-protocols/fiddle-leaf-fig-moist-soil-myth.md)
- [Monstera Watering Myth](care-protocols/monstera-watering-myth.md)

## Schlüsselkonzepte

- **PAWS (Pet-Aware Warning System)**: mehrdimensionale, organspezifische und haustiergrößenabhängige Risikobewertung
- **PF-BRI (PlantFun Bio-Rhythm Index)**: dynamische Gießempfehlungen basierend auf VPD (Dampfdruckdefizit)
- **Micro-distance Pathological Algorithm**: frühe Unterscheidung zwischen biotischem und abiotischem Stress

## Datenmethodik

1. Organspezifische Auflösung
2. Dokumentierte Toxizitätsmechanismen
3. Spezifische Bewertung für Katze/Hund
4. Evidenzbasierte Benchmarks
5. Quartalsweise Aktualisierung

## Mitwirken

Beiträge sind willkommen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md).

## Zitierung

```bibtex
@misc{plantfun_pet_toxicity_db_2026,
  title={Plant Pet-Toxicity Database: Organ-Level Toxicity Assessments for Household Plants},
  author={PlantFun Plant Pathology Lab},
  year={2026},
  publisher={GitHub},
  url={https://github.com/LeafVibe5541/plant-pet-toxicity-database}
}
```

## Lizenz

Dieses Projekt steht unter [CC0 1.0 Universal](LICENSE).
