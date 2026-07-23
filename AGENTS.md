# AGENTS.md — DCA-Trie Thesis Project

## Project Overview

This is an undergraduate thesis for the University of Mines and Technology (UMaT), Tarkwa, Ghana. Title: **"Dynamic Context-Aware Tries for Knowledge Graph-Constrained Large Language Model Generation"**. The thesis introduces DCA-Trie, a method that adjusts valid knowledge graph paths during LLM decoding rather than fixing them at the start.

**Authors:** Bernard Kirk Adjanor Katamanso, Erica Amonor, Joseph Osei Nyarko, Jessica Afua Etornam Nsafuah
**Supervisor:** Dr. Eric Affum

## Repository Structure

```
FINAL_PROJECT/
├── Final_Thesis.tex                  # Main LaTeX document
├── Final_Thesis.pdf                  # Compiled PDF
├── UMaT_Undergrauate_Report_Template_Configurations.cls  # Custom class file
├── references.bib                    # Bibliography database
├── chapters/                         # Chapter source files
│   ├── Chapter1_Introduction.tex
│   ├── Chapter2_Literature_Review.tex
│   ├── Chapter3_Methodology.tex
│   ├── Chapter4_Results_and_Discussion.tex  # Stub
│   └── Chapter5_Conclusion_and_Recommendations.tex  # Stub
├── Appendices/
│   ├── AppendixA_Questionnaires_and_Evaluation.tex
│   └── AppendixB_Guardian_PWA_Screenshots.tex
├── Figures/                          # Image assets
├── guides/                           # Writing and revision guides
│   ├── REVISED_METHODOLOGY_CH3_FULL.md
│   ├── humanizing_prose_guide.md
│   ├── typographic_tells_checklist.md
│   ├── Chapter2_revision_notes.md
│   ├── mcenerney_rubric_dca_trie.md
│   └── Implementation Plan.md
├── papers/                           # Reference PDFs (~113 papers)
├── content/                          # Experiment results and technical docs
│   ├── EXPERIMENT_RESULTS.md
│   ├── TECHNICAL_REFERENCE.md
│   └── approach{1,2,3}_*/            # Three approach variants
└── AGENTS.md                         # This file
```

## Codebase (GCR)

The upstream codebase lives at `/home/bernard/research/projects/graph-constrained-reasoning`. Key components:

| Directory | Purpose |
|-----------|---------|
| `src/trie.py` | MarisaTrie implementation (C-backed prefix trie) |
| `src/graph_constrained_decoding.py` | Constrained decoding callback (prefix_allowed_tokens_fn) |
| `src/llms/` | Model loading registry (GPT, HfCausal, GCR, Proxy) |
| `workflow/predict_paths_and_answers.py` | Stage 1: constrained path generation |
| `workflow/predict_final_answer.py` | Stage 2: inductive reasoning over paths |
| `workflow/predict_symbolic_dca_trie.py` | DCA-Trie v1/v2 with TypeOracle |
| `experiments/type_oracle_full/` | Full experiment harness (baseline vs v1 vs v2) |
| `approach3_symbolic/type_oracle.py` | TypeOracle implementation (canonical) |

## Build & Compile

### LaTeX compilation
```bash
latexmk -pdf -interaction=nonstopmode Final_Thesis.tex
```

### Dependencies
- TeX Live 2026 with pdflatex, biber, latexmk
- Packages: biblatex (biber backend), tikz, pgfgantt, algorithm, caption, hyperref

## Writing Conventions

### Document formatting
- 12pt, one-and-a-half spacing, Times New Roman (newtxtext/newtxmath)
- A4 paper: top=1in, bottom=1in, left=1.2in, right=1in
- No paragraph indentation; paragraph skip of 1em
- Author-year citation style (biblatex with natbib=true)

### File naming
- Chapters: `Chapter{N}_{Descriptive_Name}.tex`
- Appendices: `Appendix{Letter}_{Descriptive_Name}.tex`
- Main file: `Final_Thesis.tex`

### Citation style
- Use `\citep{key}` for parenthetical citations, `\citet{key}` for textual
- BibTeX keys follow pattern: `author2024keyword`
- Max 3 names in citation, all names in bibliography

## Writing Style Rules

### From guides/humanizing_prose_guide.md
- **No triadic lists** — vary list lengths (2, 4, or trailing into subordinate clauses)
- **No hedge-then-assert rhythm** — real hedging is uneven; sometimes just assert
- **No stock transitions** — avoid "Furthermore, Moreover, Additionally" clusters
- **No empty intensifiers** — replace "plays a crucial role" with the actual mechanism
- **No uniform paragraph shape** — mix 2-sentence and long paragraphs
- **No summary restates** — last sentence must advance, not restate the first

### From guides/mcenerney_rubric_dca_trie.md
- Every paragraph must pass: "Would a GCR/DoG researcher stop to read this?"
- Organize around **instability**, not definition or cataloguing
- Each objective must map 1:1 to a specific unresolved tension
- Results chapter follows conditions (F, R, P), not experiment log order
- Tables/figures must have prose explaining what they **prove**, not just what they show

### From guides/Chapter2_revision_notes.md
- Never use "Its limitation is" / "The limitation is" as a paragraph ending
- Group papers by shared insight, not one paragraph per paper
- After every complex sentence, add a short one (under 12 words) with the implication
- Search and remove: "It is worth noting that", "significantly", "in practice"

### From guides/typographic_tells_checklist.md
- Em-dashes: max 2-3 per page in flowing prose
- No bolded lead-in bullets in body prose (Chapters 1-4)
- No decorative Unicode symbols (arrows, checkmarks) in prose paragraphs
- Search and strip `\u00A0` and `\u200B` before submission
- Semicolons: no more than one per page

## Experiment Results

| Method | Hits@1 | Hits@k | Path Reduction |
|--------|--------|--------|----------------|
| GCR_Baseline | 80.9% | 91.3% | — |
| DCA_v1_Static | 75.9% | 86.0% | 14.5% |
| DCA_v2_Dynamic | 53.5% | 53.5% | — (interrupted) |

Configuration: `rmanluo/GCR-Meta-Llama-3.1-8B-Instruct`, RoG-webqsp test, beam=10, group-beam, index_length=2, max_new_tokens=256, NVIDIA RTX 4090.

## Key Equations

- Oracle specification: `W_val^DCA(t) = f(G, E_q, q, y^{<t})`
- SIR definition: `SIR = (1/|Q|) * SUM_q (1/L_q) SUM_{t=1}^{L_q} SIR(q,t)`
- TypeOracle: `is_admissible(r, e', answer_types, hop, max_hop) = type_gate AND range_gate`

## Implementation Plan

See [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for the full chapter-by-chapter writing plan, including the research evolution from Approach 1 (cosine) → Approach 2 (decomposed) → Approach 3 (symbolic TypeOracle), section-by-section rewrite targets, and figure generation plan.

## Research Evolution: Three Oracle Designs

The thesis developed through three oracle designs before settling on the symbolic TypeOracle. Chapter 3 must show this evolution.

| | Approach 1 (Cosine) | Approach 2 (Decomposed) | Approach 3 (TypeOracle) |
|---|---|---|---|
| **Status** | Abandoned | Abandoned | **Final** |
| **Mechanism** | `cos(MiniLM(path), MiniLM(q))` | `ρ_r × ρ_e × ρ_traj` | Two ontology gates |
| **Encoder needed** | Yes | Yes | **No** |
| **Threshold τ** | Yes | Yes | **No** |
| **Per-path cost** | Forward pass | Forward pass | **O(1) set lookup** |
| **Why abandoned** | Single score can't distinguish type match from topical overlap; expensive | Still needs encoder; threshold persists | — |

Source code and READMEs for each approach: `content/approach{1,2,3}_*/`

## Scope Boundaries

1. Freebase-based KGQA only (WebQSP, CWQ)
2. No model fine-tuning — changes reflect oracle design only
3. Schema-dependent: TypeOracle relies on KG ontology metadata
4. Conservative admission when schema info is missing
5. Heuristic question-type inference (pattern matching)
