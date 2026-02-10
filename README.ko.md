# 반려동물 식물 독성 데이터베이스

> **반려동물에게 유해한 실내 식물에 대해 기관(organ) 단위 독성 평가, 오진 사례, 환경 적응형 관리 프로토콜을 제공하는 오픈소스 데이터베이스입니다.**

## 언어

기본 언어: **영어** (`README.md`)

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Español](README.es.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

> 이 문서는 주요 문서의 번역본이며, 최신 기준 문서는 영어 버전입니다.

## 개요

많은 식물 식별 도구는 반려동물 독성을 "유독/무독" 이진값으로만 분류합니다. 실제로는 충분하지 않습니다.

이 데이터베이스는 다음 기준으로 세분화된 데이터를 제공합니다.
- 식물 기관별(잎, 줄기, 꽃가루, 수액 등)
- 섭취량 및 반려동물 체중/크기별
- 독성 작용 기전별
- 실제 노출 환경/맥락별

## 주요 문서

### 반려동물 독성 리포트

- [Aloe Vera Anthraquinone Risk](pet-toxicity/aloe-vera-anthraquinone-risk.md)
- [Azalea Grayanotoxin Cardiac Risk](pet-toxicity/azalea-grayanotoxin-cardiac-risk.md)
- [Lily Cat Toxicity](pet-toxicity/lily-cat-toxicity.md)
- [Pothos Hidden Toxicity](pet-toxicity/pothos-hidden-toxicity.md)

### 오진 사례 연구

- [Fungal Leaf Spot vs Sunburn](misdiagnosis/fungal-leaf-spot-vs-sunburn.md)
- [Spider Mites vs Dust](misdiagnosis/spider-mites-vs-dust.md)
- [Root Rot vs Underwatering](misdiagnosis/root-rot-vs-underwatering.md)
- [Scale Insects vs Mineral Residue](misdiagnosis/scale-insects-vs-mineral-residue.md)

### 동적 관리 프로토콜

- [Fiddle-Leaf Fig Moist Soil Myth](care-protocols/fiddle-leaf-fig-moist-soil-myth.md)
- [Monstera Watering Myth](care-protocols/monstera-watering-myth.md)


<!-- BEGIN AUTO-GENERATED-INDEX-REF -->
## 전체 생성 문서 인덱스

이 번역 README에는 요약만 포함되어 있습니다. 전체 자동 생성 인덱스는 메인 문서에서 관리됩니다.

- 반려동물 독성 리포트: 183
- 오진 사례 연구: 157
- 동적 케어 프로토콜: 130
- 전체 인덱스: [README.md#full-generated-article-index](README.md#full-generated-article-index)

<!-- END AUTO-GENERATED-INDEX-REF -->

## 핵심 개념

- **PAWS (Pet-Aware Warning System)**: 기관 단위 + 반려동물 크기 보정 다차원 위험 평가
- **PF-BRI (PlantFun Bio-Rhythm Index)**: VPD(증기압 결핍) 기반 동적 물주기 권장
- **Micro-distance Pathological Algorithm**: 생물적/비생물적 스트레스 조기 구분

## 데이터 방법론

1. 기관 단위 해상도
2. 독성 기전 문서화
3. 고양이/강아지 종 특이성 반영
4. 근거 기반 벤치마크
5. 분기별 업데이트

## 기여

기여를 환영합니다. [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.

## 인용

```bibtex
@misc{plantfun_pet_toxicity_db_2026,
  title={Plant Pet-Toxicity Database: Organ-Level Toxicity Assessments for Household Plants},
  author={PlantFun Plant Pathology Lab},
  year={2026},
  publisher={GitHub},
  url={https://github.com/LeafVibe5541/plant-pet-toxicity-database}
}
```

## 라이선스

이 프로젝트는 [CC0 1.0 Universal](LICENSE) 라이선스로 공개됩니다.
