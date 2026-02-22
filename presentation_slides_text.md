# Presentation Slides Text: Pan-cancer scRNA-seq Analysis
## Based on First 2 Pages of the Paper

---

## Slide 1: Title Slide

**Pan-cancer Single-Cell RNA Sequencing:**
**Revealing Recurring Programs of Cellular Heterogeneity**

*Kinker et al., Nature Genetics 2020*

---

## Slide 2: Introduction - The Challenge of Tumor Heterogeneity

**Key Concepts:**

- Cellular plasticity and heterogeneity are fundamental features of human tumors
- Play major role in disease progression and treatment failure
- Rare tumor cell subpopulations may cause treatment resistance
- These subpopulations can facilitate metastasis

**Current Tools:**
- Single-cell RNA sequencing (scRNA-seq) enables direct study of intratumor heterogeneity (ITH) in patient samples

**The Problem:**
- Mechanisms and functional implications of ITH patterns remain difficult to resolve
- Extensive follow-up studies needed in model systems

---

## Slide 3: Understanding Heterogeneity Sources

**Contributors to Intratumor Heterogeneity:**

1. Genetic diversity
2. Epigenetic plasticity
3. Interactions within the tumor microenvironment

**Central Hypothesis:**
A considerable fraction of ITH in expression patterns reflects **intrinsic cellular plasticity**, which exists even in the absence of native microenvironment

**Research Goal:**
Examine heterogeneity within cancer cell lines and their ability to recapitulate ITH programs

---

## Slide 4: Experimental Design & Quality Control

**Methodology:**

- Multiple cancer cell lines analyzed
- Cell lines co-cultured for 3 days before scRNA-seq profiling
- Expression patterns may be affected by co-culturing

**Validation Approach:**
- Control experiment: 6 cell lines profiled with and without co-culturing
- Co-culturing had modest effect on average gene expression
- **Key Finding:** Patterns of heterogeneity within cell lines were highly consistent between conditions

**Additional Evidence:**
- Heterogeneity patterns equally similar between:
  - Cell lines from same pool
  - Cell lines from different pools

---

## Slide 5: Two Patterns of Expression Heterogeneity

**Type 1: Discrete Subpopulations**

- Found in only 11% of cell lines
- Identified using t-SNE dimensionality reduction + DBSCAN clustering
- Expression programs showed limited similarities between cell lines
- **Conclusion:** Discrete subpopulations are typically cell line-specific

**Type 2: Continuous Patterns**

- More common across cell lines
- Reflect spectra of cellular states
- Identified using both discrete and continuous analysis methods

---

## Slide 6: Analytical Approach - NMF Analysis

**Non-negative Matrix Factorization (NMF):**

- Applied to each cell line individually
- Identifies both continuous and discrete variability of cellular states

**Results:**
- **1,445 robust expression programs** detected across all cell lines
- Individual cell lines showed **4-9 programs each**

**Significance:**
Comprehensive characterization of expression heterogeneity patterns in cancer cell lines

---

## Slide 7: Key Findings Summary

**Major Discoveries:**

✓ Extensive variability in gene expression exists across cells within individual cell lines

✓ Both discrete subpopulations and continuous cellular states are present

✓ Discrete clusters are rare (11%) and mostly cell line-specific

✓ Over 1,400 expression programs identified systematically

✓ Co-culturing effects are minimal on heterogeneity patterns

---

## Slide 8: Research Implications

**Why This Matters:**

1. **Model System Validation:** Cancer cell lines can recapitulate intratumor heterogeneity patterns

2. **Mechanistic Studies:** Cell lines provide tractable systems for follow-up studies

3. **Intrinsic Plasticity:** Heterogeneity exists independent of tumor microenvironment

4. **Therapeutic Insights:** Understanding cellular states can inform treatment strategies

**Next Steps:**
Characterize recurring heterogeneity programs across multiple cancer types and validate against patient tumor data
