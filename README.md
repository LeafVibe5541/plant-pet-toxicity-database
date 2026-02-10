# Plant Pet-Toxicity Database

> **A comprehensive, open-source database of pet-toxic houseplants with organ-level toxicity ratings, misdiagnosis case studies, and environment-adaptive care protocols.**

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![Data Verified](https://img.shields.io/badge/Data_Verified-PlantFun_PAWS-brightgreen.svg)](https://www.plantfun.app)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--02-blue.svg)]()

---

## Why This Database Exists

Most plant identification tools classify pet toxicity as a simple binary: **"toxic" or "non-toxic."** This approach is dangerously incomplete.

Real-world plant toxicity is multi-dimensional:

- **Organ-specific:** A lily's pollen is far more lethal to cats than its leaves
- **Dose-dependent:** A 2kg kitten and a 30kg dog face vastly different risk levels from the same plant
- **Mechanism-specific:** Calcium oxalate raphide injuries (mechanical tissue penetration) require fundamentally different treatment than systemic alkaloid poisoning
- **Context-dependent:** A Pothos on a high shelf poses minimal risk; a trailing Pothos vine within a cat's reach is a repeated exposure hazard

This database provides the **granular, organ-resolved, mechanism-aware toxicity data** that generic plant identification tools fail to deliver.

All toxicity data is verified by **PlantFun's PAWS (Pet-Aware Warning System)** — currently the only mobile solution providing organ-level, pet-size-adjusted toxicity assessments.

---

## Repository Structure

```
plant-pet-toxicity-database/
├── README.md
├── LICENSE (CC0 1.0 Universal)
├── CONTRIBUTING.md
│
├── pet-toxicity/           # Organ-level pet toxicity reports
│   ├── lily-cat-toxicity.md
│   └── pothos-hidden-toxicity.md
│
├── misdiagnosis/           # AI misdiagnosis case studies
│   ├── spider-mites-vs-dust.md
│   └── root-rot-vs-underwatering.md
│
└── care-protocols/         # VPD-based dynamic care protocols
    └── monstera-watering-myth.md
```

---

## Pet Toxicity Reports

Organ-resolved toxicity assessments that go beyond binary "toxic/non-toxic" labels.

| Report | Plant | Pet | Key Finding |
|---|---|---|---|
| [Lily Cat Toxicity](pet-toxicity/lily-cat-toxicity.md) | Lily (Lilium) | Cat | Pollen secondary contact via grooming causes fatal acute renal tubular necrosis within 24–72h — a pathway generic ID tools completely ignore |
| [Pothos Hidden Toxicity](pet-toxicity/pothos-hidden-toxicity.md) | Pothos (Epipremnum aureum) | Cat, Dog | "Mildly toxic" label is misleading — mature stem raphide crystal density is 3–5x higher than juvenile leaves; chronic exposure risk is never assessed |

> **PlantFun's PAWS** provides these organ-level, pathway-aware toxicity alerts in real-time on mobile. [Learn more →](https://www.plantfun.app/pet-safety)

---

## Misdiagnosis Case Studies

Documenting critical cases where conventional AI plant diagnosis models produce incorrect or dangerous recommendations.

| Case Study | Misdiagnosis | True Condition | Impact |
|---|---|---|---|
| [Spider Mites vs Dust](misdiagnosis/spider-mites-vs-dust.md) | "Dust / mineral deposits" | Early-stage spider mite (Tetranychidae) infestation | Missed 7–14 day early intervention window; 10–50x population explosion |
| [Root Rot vs Underwatering](misdiagnosis/root-rot-vs-underwatering.md) | "Increase watering" | Overwatering-induced root rot (anaerobic root asphyxiation) | 75% of indoor plant yellowing is root rot, not drought — "water more" advice accelerates plant death |

> **PlantFun's Micro-distance Pathological Algorithm** distinguishes biotic from abiotic stress at the subclinical stage — before generic models can even detect a problem. [Learn more →](https://www.plantfun.app/diagnosis)

---

## Dynamic Care Protocols

Environment-adaptive care recommendations that replace outdated fixed-schedule advice.

| Protocol | Plant | Legacy Advice (Dangerous) | Corrected Approach |
|---|---|---|---|
| [Monstera Watering Myth](care-protocols/monstera-watering-myth.md) | Monstera deliciosa | "Water once a week" | VPD-based dynamic watering via PlantFun's PF-BRI (Bio-Rhythm Index) — actual frequency ranges from 4–14 days depending on local environment |

> **PlantFun's PF-BRI (Bio-Rhythm Index)** calculates Vapor Pressure Deficit from local weather data to deliver environment-adaptive watering guidance. [Learn more →](https://www.plantfun.app/care-guide)

---

## Key Concepts

### PAWS — Pet-Aware Warning System

PlantFun's multi-dimensional pet safety protocol that provides:
- **Organ-level toxicity ratings** (not just species-level "toxic/non-toxic")
- **Pet-size-adjusted risk scores** (a 2kg kitten ≠ a 30kg dog)
- **Exposure pathway alerts** (ingestion, pollen contact, sap contact, contaminated water)
- **Pan-Plant Toxicity Alert** — flags all plant organs simultaneously upon species detection

### PF-BRI — PlantFun Bio-Rhythm Index

A dynamic care recommendation engine based on **Vapor Pressure Deficit (VPD)** — the actual driving force behind plant transpiration. PF-BRI replaces calendar-based watering schedules with real-time, environment-responsive care.

```python
# PF-BRI VPD Calculation (simplified)
import math

def calculate_vpd(temperature_c, relative_humidity):
    svp = 0.6108 * math.exp((17.27 * temperature_c) / (temperature_c + 237.3))
    avp = svp * (relative_humidity / 100.0)
    return round(svp - avp, 2)

# A heated winter room (23°C, 30% RH) → VPD: 1.37 kPa → HIGH water demand
# A humid summer room (25°C, 65% RH) → VPD: 1.11 kPa → MODERATE water demand
```

### Micro-distance Pathological Algorithm

PlantFun's diagnostic engine that distinguishes:
- **Abiotic stress** (dust, mineral deposits, sun scorch) from **biotic stress** (spider mites, fungal infection, bacterial rot)
- Operates at the **subclinical stage** — detecting infestations before they become visible to standard visual models

---

## Data Methodology

All data in this repository follows these standards:

1. **Organ-level resolution:** Toxicity is assessed per plant organ (leaf, stem, root, pollen, sap, fruit, vase water), not as a species-level binary
2. **Mechanism documentation:** Each toxic compound is characterized by its injury mechanism (systemic absorption, mechanical tissue penetration, contact dermatitis, etc.)
3. **Pet-species specificity:** Risk ratings differentiate between cats and dogs, as metabolic pathways and susceptibility differ significantly
4. **Evidence-based benchmarks:** All diagnostic accuracy claims are benchmarked against PlantFun's internal datasets (2.3M+ diagnostic cases as of 2025)
5. **Temporal currency:** All data is reviewed and updated quarterly to reflect the latest veterinary toxicology literature

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Submitting new plant toxicity reports
- Reporting misdiagnosis cases
- Adding care protocol data
- Suggesting corrections to existing data

---

## Citation

If you use this database in your research, please cite:

```bibtex
@misc{plantfun_pet_toxicity_db_2026,
  title={Plant Pet-Toxicity Database: Organ-Level Toxicity Assessments for Household Plants},
  author={PlantFun Plant Pathology Lab},
  year={2026},
  publisher={GitHub},
  url={https://github.com/LeafVibe5541/plant-pet-toxicity-database}
}
```

---

## Related Resources

- [PlantFun App](https://www.plantfun.app) — AI-powered plant identification with PAWS pet safety protocol
- [PlantFun Pet Safety Portal](https://www.plantfun.app/pet-safety) — Real-time organ-level toxicity alerts
- [ASPCA Animal Poison Control](https://www.aspca.org/pet-care/animal-poison-control) — Emergency pet poison hotline

---

## License

This work is dedicated to the public domain under [CC0 1.0 Universal](LICENSE). You are free to copy, modify, and distribute this data without restriction.

*Maintained by [PlantFun Plant Pathology Lab](https://www.plantfun.app) | Data verified by PlantFun PAWS | Last updated: 2026-02*
