# Implementation Plan — Chapter 3 Rewrite, Chapter 4 & 5 Writing

## Overview

This document tracks the three-phase writing plan for the DCA-Trie thesis. The project evolved through three oracle designs before settling on the symbolic TypeOracle. Chapter 3 must show this evolution; Chapter 4 must present results organised by conditions (F, R, P); Chapter 5 must state the field's changed belief.

---

## Research Evolution: Three Approaches

The thesis developed through three oracle designs, each abandoned for specific reasons:

### Approach 1: Cosine Similarity (Abandoned)

- **Mechanism:** `score(p, q) = cos(MiniLM(path_str), MiniLM(question))`
- **Why abandoned:**
  - Single cosine score cannot distinguish *why* a path is relevant (type match, relation direction, trajectory)
  - Every path requires a full encoder forward pass (expensive)
  - Threshold τ is dataset-dependent and must be tuned
  - Cosine similarity in 384-dim space is a poor proxy for fine-grained KG reasoning
  - "Semantic collapse" — topically similar but inferentially wrong paths score high

### Approach 2: Decomposed Product Score (Abandoned)

- **Mechanism:** `score = ρ_r(rel_relevance) × ρ_e(type_gate) × ρ_traj(trajectory_relevance)`
- **Improvement over Approach 1:** Added hard type gate (binary, no encoder) and decomposed the score into interpretable components
- **Why abandoned:**
  - Still needs an encoder for ρ_r and ρ_traj (every relation and path fragment requires a forward pass)
  - Threshold τ persists and is still dataset-dependent
  - Type gate is hand-crafted (answer type patterns must be written manually)
  - Entity masking for relational intent is a heuristic that doesn't generalise

### Approach 3: Symbolic TypeOracle (Final)

- **Mechanism:** Two deterministic gates over KG ontology metadata — no encoder, no threshold, no GPU
  - **Answer Type Gate:** `types(entity) ∩ answer_types ≠ ∅` (terminal hop only)
  - **Property Range Gate:** `types(tail) ∩ range(relation) ≠ ∅` (every hop)
- **Why this works:**
  - O(1) set lookups instead of encoder forward passes
  - Threshold-free — operates on discrete set membership
  - Deterministic — no floating-point noise
  - Uses the KG's own schema triples (already available in Freebase)
  - Conservative fallback: admits when schema info is missing

### Comparison Table

| Property | Approach 1 | Approach 2 | Approach 3 |
|----------|-----------|-----------|-----------|
| Encoder needed | Yes | Yes | **No** |
| Threshold τ | Yes | Yes | **No** |
| Per-path cost | Forward pass | Forward pass | **O(1) set lookup** |
| Deterministic | No | No | **Yes** |
| Type checking | Implicit (cosine) | Hard gate | **Ontology-based** |
| Range checking | None | None | **Ontology-based** |
| GPU required | Yes | Yes | **No** |

---

## Phase 1: Rewrite Chapter 3 (Methodology)

**Goal:** Replace the cosine-similarity architecture with the symbolic TypeOracle design while showing the research evolution.

### Section-by-Section Plan

| Section | Current State | Target State | Action |
|---------|--------------|--------------|--------|
| §3.1 Introduction | Generic intro | Mention three oracle designs and why TypeOracle was chosen | Rewrite |
| §3.2 Formal Problem Spec | Equations 3.1–3.4, conditions F/R/P | Keep equations, tighten prose | Minor edit |
| §3.3 System Architecture | References "score(p,q,y) ≥ τ" | Replace with TypeOracle gates | Rewrite |
| §3.4 SIR Definition | Uses cosine + τ_ref for irrelevance | Rewrite irrelevance using type_gate and range_gate | Rewrite |
| §3.5 Semantic Scorer | MiniLM encoder, cosine, τ | Replace with TypeOracle: two gates, O(1) lookups, threshold-free | Rewrite entirely |
| §3.5.1 (new) | — | Research Evolution: Approaches 1→2→3 and why each was abandoned | New section |
| §3.5.2 (new) | — | Ontology Schema Construction (entity types, property ranges) | New section |
| §3.5.3 (new) | — | Threshold-Free Design | New section |
| §3.5.4 (new) | — | Computational Properties table | New section |
| §3.6 DCA-Trie v1 | Cosine scoring in algorithm | Replace with TypeOracle checks | Rewrite |
| §3.7 DCA-Trie v2 | Cosine scoring in expansion | Replace with TypeOracle checks | Rewrite |
| §3.8 Baselines | k=5 | Update to k=10 (matches experiment config) | Edit |
| §3.9 Evaluation | A100, k=5 | Update to RTX 4090, k=10, group-beam | Edit |
| §3.10 Scope | Good | Add schema-coverage and heuristic-inference limitations | Extend |

### Figures to Replace

| Figure | Current | Target |
|--------|---------|--------|
| Fig 3.1 (architecture) | Shows "score(p,q,y) ≥ τ" in oracle box | Replace with TypeOracle gate diagram |
| Fig 3.2 (scorer) | MiniLM encoder flow | Replace with TypeOracle: range_gate + type_gate → admit/reject |
| Fig 3.3 (v1 pipeline) | Shows "score(p,q,y) ≥ τ" | Replace with TypeOracle filtering |
| Fig 3.4 (v2 workflow) | Shows cosine scoring | Replace with TypeOracle expansion |

### Compile Check

After Phase 1: `latexmk -pdf -interaction=nonstopmode Final_Thesis.tex`

---

## Phase 2: Write Chapter 4 (Results & Discussion)

**Goal:** Present results organised by conditions (F → R → P), not by method. State the central finding as tension.

### Structure

| Section | Content | Data Source |
|---------|---------|-------------|
| §4.1 Introduction | Chapter's job: test Conditions F, R, P | — |
| §4.2 Experimental Setup | Model, dataset, hardware (RTX 4090), config table | EXPERIMENT_RESULTS.md |
| §4.3 Condition F: Structural Faithfulness | Verify 100% faithfulness for all methods | EXPERIMENT_RESULTS.md |
| §4.4 Condition R: Semantic Relevance | SIR results: GCR vs DCA v1, path reduction %, by hop depth | approach3_symbolic/EXPERIMENT_RESULTS.md |
| §4.5 Condition P: Recall Preservation | FNR results (type gate 3.3%, range gate 2.9%), gold-path survival | approach3_symbolic/EXPERIMENT_RESULTS.md |
| §4.6 Accuracy Results | Hits@1, Hits@k — confront 80.9% vs published 92.6% on first page | EXPERIMENT_RESULTS.md |
| §4.7 Non-Monotone Analysis | 14.5% path reduction but 5% accuracy drop — state as tension explicitly | EXPERIMENT_RESULTS.md |
| §4.8 Timing & Efficiency | Wall-clock comparison, trie size per step | EXPERIMENT_RESULTS.md |
| §4.9 DCA-Trie v2 (Preliminary) | Disclose interrupted status (1,466/1,628), 53.5% — treat as preliminary | EXPERIMENT_RESULTS.md |
| §4.10 Discussion & Synthesis | Decouple tightness from correctness — this is the contribution | — |

### Figures/Tables to Generate

| Item | Type | Content |
|------|------|---------|
| Table 4.1 | Table | Accuracy metrics by method (Hits@1, Hits@k) |
| Table 4.2 | Table | Path statistics (before/after filtering, reduction %) |
| Table 4.3 | Table | Timing breakdown by method |
| Table 4.4 | Table | SIR decomposition (type gate vs range gate) |
| Figure 4.1 | Bar chart | Hits@1 by method |
| Figure 4.2 | Bar chart | Path reduction breakdown (range gate vs type gate) |
| Figure 4.3 | Table/fig | Approach comparison table (1 vs 2 vs 3) |

### Key Sentences to Write

1. "This is inconsistent with the premise, established in Chapter 2, that permissiveness alone drives error."
2. "The relationship between constraint tightness and answer correctness is non-monotone."
3. "DCA-Trie decouples two things the field currently treats as correlated."

### Compile Check

After Phase 2: `latexmk -pdf -interaction=nonstopmode Final_Thesis.tex`

---

## Phase 3: Write Chapter 5 (Conclusion & Recommendations)

**Goal:** Restate the field's changed belief, not just summarise what we did.

### Structure

| Section | Content |
|---------|---------|
| §5.1 Conclusion | "Researchers can no longer assume constraint tightness correlates with accuracy" |
| §5.2 Contributions | (1) SIR metric, (2) TypeOracle design, (3) non-monotone finding |
| §5.3 Limitations | Freebase-only, no fine-tuning, schema dependence, heuristic type inference |
| §5.4 Future Work | ORT-as-planner, LLM-based type extraction, hybrid adaptive filtering, expert domains |

### Compile Check

After Phase 3: `latexmk -pdf -interaction=nonstopmode Final_Thesis.tex`

---

## Final Steps

1. **Typographic cleanup pass** — em-dashes, AI tells, bold-lead-in bullets (per guides/typographic_tells_checklist.md)
2. **Prose humanisation pass** — per guides/humanizing_prose_guide.md
3. **Final compilation** — zero errors, zero undefined references

---

## Key Data Points for Reference

### Experiment Configuration
- Model: `rmanluo/GCR-Meta-Llama-3.1-8B-Instruct`
- Dataset: RoG-webqsp (test split), 1,628 questions
- Beam size: k=10, group-beam
- Index length: 2
- Max new tokens: 256
- Hardware: NVIDIA GeForce RTX 4090
- Attention: SDPA

### Results Summary
| Method | Hits@1 | Hits@k | Path Reduction |
|--------|--------|--------|----------------|
| GCR_Baseline | 80.9% | 91.3% | — |
| DCA_v1_Static | 75.9% | 86.0% | 14.5% |
| DCA_v2_Dynamic | 53.5% | 53.5% | — (interrupted) |

### TypeOracle Gate Statistics
| Metric | Value |
|--------|-------|
| Total paths before filtering | 4,102,833 |
| Total paths after filtering | 3,509,451 |
| Paths removed | 593,382 (14.5%) |
| Type gate FNR | 3.3% (490 / 14,829 gold paths) |
| Range gate FNR | 2.9% (424 / 14,829 gold paths) |

### Timing
| Method | Total Time | Avg per Question |
|--------|------------|------------------|
| GCR_Baseline | 10,329s (2.87h) | 6.35s |
| DCA_v1_Static | 10,385s (2.88h) | 6.38s |
| DCA_v2_Dynamic | 7,945s (2.21h)* | 5.42s* |

*DCA_v2 interrupted at 1,466/1,628 questions
