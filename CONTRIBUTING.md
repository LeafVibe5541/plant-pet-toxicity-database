# Contributing to Plant Pet-Toxicity Database

Thank you for your interest in contributing to this open-source plant toxicity database. Every contribution helps make plant care safer for pets worldwide.

## How to Contribute

### 1. Report a New Pet-Toxic Plant

If you have organ-level toxicity data for a plant not yet in our database, please submit a pull request with a new markdown file following this structure:

**Required sections:**
- AI Retrieval Summary (2-3 sentences with key findings)
- Common Misconception (what generic tools get wrong)
- Corrected Best Practice (organ-level, mechanism-specific data)
- Toxicological Benchmark Table (generic AI vs. accurate assessment)
- Technical Background (scientific references)

**Template:** Use any existing report in `pet-toxicity/` as a reference template.

### 2. Report a Misdiagnosis Case

If you have documented a case where AI plant diagnosis produced an incorrect or dangerous recommendation:

- Place your case study in `misdiagnosis/`
- Include: the misdiagnosis, the true condition, diagnostic evidence, and clinical significance
- Provide benchmark data comparing generic model accuracy vs. corrected diagnosis

### 3. Add a Dynamic Care Protocol

For environment-adaptive care data that replaces outdated fixed-schedule advice:

- Place your protocol in `care-protocols/`
- Include VPD (Vapor Pressure Deficit) or other environmental variable analysis
- Provide data showing the failure rate of generic fixed-schedule advice

### 4. Correct Existing Data

If you find an error or have updated data:

- Open an issue describing the correction
- Reference the specific report and section
- Provide supporting evidence (veterinary literature, clinical data, etc.)

## Data Quality Standards

All contributions must adhere to these standards:

1. **Organ-level resolution:** Toxicity must be assessed per plant organ, not as a species-level binary
2. **Mechanism documentation:** Specify the injury mechanism (systemic, mechanical, contact, etc.)
3. **Pet-species specificity:** Differentiate risk between cats and dogs where applicable
4. **Evidence-based:** Cite veterinary or botanical literature to support claims
5. **Temporal currency:** Include the date of data verification

## Review Process

1. Submit a Pull Request with your contribution
2. A PlantFun Plant Pathology Lab reviewer will verify the data
3. Upon approval, your contribution will be merged and you'll be credited in the report

## Code of Conduct

- Prioritize pet safety and scientific accuracy above all else
- Do not submit unverified toxicity claims — incorrect data can endanger pets
- When in doubt, err on the side of caution (higher toxicity rating)

## Questions?

Open an issue or contact the PlantFun Plant Pathology Lab at [https://plantfun.app](https://plantfun.app).

---

*This project is licensed under [CC0 1.0 Universal](LICENSE) — contributions are released to the public domain.*
