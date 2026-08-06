# Guide 3: Objectives — What We Set Out to Do

## What This Section Covers

The four project objectives and how they map to the thesis chapters.

## The Four Objectives

### Objective 1: Characterize the Permissiveness Problem

- **Goal**: Measure SIR of GCR's static KG-Tries on WebQSP
- **What is SIR?** Semantic Irrelevance Ratio — the fraction of structurally valid paths that are semantically irrelevant
- **How**: For each question, enumerate all paths in the trie, then score each path for semantic relevance to the question
- **Expected result**: GCR should have high SIR (most paths are irrelevant)

### Objective 2: Design the TypeOracle

- **Goal**: Create a symbolic constraint oracle with range and type gates
- **Key design choices**:
  - No embeddings (avoids threshold sensitivity)
  - No encoder (O(1) per candidate triple)
  - Deterministic (same input → same output)
- **Two gates**:
  - Range gate: checks if tail entity type matches relation's range
  - Type gate: checks if terminal entity matches inferred answer type

### Objective 3: Implement DCA-Trie v1 and v2

- **v1 (static)**: Filter paths at construction time, FNR < 5%
  - Enumerate all paths → apply TypeOracle gates → build trie from survivors
- **v2 (dynamic)**: Expand trie step-by-step as entities are committed
  - At each hop: enumerate gated paths from current head → build per-beam trie → generate one hop

### Objective 4: Evaluate Against GCR Baseline

- **Metrics**: Hits@1, F1, structural faithfulness, SIR, trie size
- **Datasets**: WebQSP (1,628 test queries) and CWQ (3,531 samples)
- **Baseline**: GCR with Llama-3.1-8B, beam search k=10

## How Objectives Map to Chapters

| Objective | Chapter | Section |
| ----------- | --------- | --------- |
| 1. Characterize permissiveness | Ch. 4 | SIR measurement |
| 2. Design TypeOracle | Ch. 3 | TypeOracle architecture |
| 3. Implement v1 and v2 | Ch. 3 | Implementation details |
| 4. Evaluate | Ch. 4 | Results and discussion |

## If Asked

> **"What are the project objectives?"**
> "Four things: (1) measure how permissive GCR's constraint is using a new metric called SIR, (2) design a symbolic TypeOracle with range and type gates, (3) implement static v1 and dynamic v2 variants, and (4) evaluate both against GCR on WebQSP and CWQ."

> **"Why is SIR important?"**
> "It's the first metric that measures constraint quality independently of answer accuracy. Before SIR, you couldn't tell if a tighter constraint was actually filtering relevant paths or just removing everything."

## Practice

1. Why did we choose symbolic gates instead of embedding-based scoring?
2. What is the difference between v1 and v2 in terms of when filtering happens?
3. Why do we need both WebQSP and CWQ for evaluation?
