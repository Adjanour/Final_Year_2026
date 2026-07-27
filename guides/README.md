# DCA-Trie Learning Guides — Index

A step-by-step guide to understanding the DCA-Trie project, organized by PPT section.

## How to Use These Guides

Each guide covers one section of the presentation. Read them in order for a complete understanding, or jump to a specific section if you already know the basics.

**Each guide includes:**
- What this section covers
- Key concepts explained simply
- Equations with plain-English explanations
- Code references (where to find it in the codebase)
- Practice questions
- "If asked" one-liners for defense

## Guides

| # | Guide | PPT Section | Key Concept |
|---|-------|-------------|-------------|
| 1 | [Introduction](01_introduction.md) | Slides 3-4 | LLMs hallucinate, KGQA, permissiveness problem |
| 2 | [Problem Statement](02_problem_statement.md) | Slide 5 | Static trie, no question conditioning, no metric |
| 3 | [Objectives](03_objectives.md) | Slides 6-7 | SIR, TypeOracle, v1/v2, evaluation |
| 4 | [Tools & Facilities](04_tools_facilities.md) | Slides 8-9 | Python, PyTorch, marisa-trie, RTX 4090 |
| 5 | [Methodology](05_methodology.md) | Slide 10-11 | 4-layer architecture, entity linking → oracle → decoding → reasoning |
| 6 | [TypeOracle](06_type_oracle.md) | Slide 19 | Range gate + type gate, no embeddings |
| 7 | [SIR Metric](07_sir_metric.md) | Slide 20 | Semantic Irrelevance Ratio, first metric for constraint quality |
| 8 | [DCA-Trie v1](08_dca_v1.md) | Slide 21 | Static filtering, 85.5% SIR reduction |
| 9 | [DCA-Trie v2](09_dca_v2.md) | Slide 22 | Dynamic expansion, hop-by-hop |
| 10 | [Results](10_results.md) | Slides 23-25 | Non-monotone finding, 5.2pp drop |
| 11 | [Contributions](11_contributions.md) | Slide 27 | TypeOracle, SIR, non-monotone |
| 12 | [Conclusion](12_conclusion.md) | Slides 29-30 | Key takeaways, future work |

## Quick Reference — The Non-Monotone Result

| Metric | GCR | DCA-Trie v1 | Change |
|--------|-----|-------------|--------|
| SIR | 1.000 | 0.145 | -85.5% (better) |
| Hits@1 | 91.6% | 86.4% | -5.2pp (worse) |

**Key insight**: Tighter constraints improve constraint quality (SIR) but NOT answer accuracy (Hits@1).

## Quick Reference — The Three Contributions

1. **TypeOracle**: Symbolic constraint oracle with range + type gates, no embeddings
2. **SIR**: First metric to measure constraint quality independently of answer accuracy
3. **Non-monotone finding**: First empirical evidence that tighter constraints ≠ higher accuracy
