# Guide 11: Key Contributions — What We Added to the Field

## What This Section Covers
The three main contributions and why they matter.

## The Three Contributions

### Contribution 1: TypeOracle

| Before | After |
|--------|-------|
| Embedding + threshold τ | Two symbolic gates |
| Requires encoder | No encoder needed |
| Sensitive to τ | Deterministic, O(1) |
| Dataset-specific tuning | Zero-shot, no tuning |

**What it is**: A purely symbolic constraint oracle that uses Freebase ontology (entity types + relation ranges) to prune paths.

**Why it matters**: No encoder, no threshold τ, O(1) per candidate, deterministic. Same input always gives same output.

### Contribution 2: SIR Metric

| Before | After |
|--------|-------|
| Accuracy only | Semantic Irrelevance Ratio |
| Can't measure constraint quality | Can measure constraint quality independently |

**What it is**: Semantic Irrelevance Ratio — the first metric that measures constraint quality independently of answer accuracy.

**Why it matters**: Before SIR, you couldn't tell if a tighter constraint was actually filtering relevant paths or just removing everything. SIR enables systematic comparison of oracles without conflating structural filtering with downstream accuracy.

### Contribution 3: Non-Monotone Finding

| Before | After |
|--------|-------|
| "Tighter → better" (GCR, DoG assumption) | Tightness ≠ accuracy |
| No evidence | First empirical evidence |

**What it is**: First empirical evidence that constraint tightness is NOT a proxy for accuracy.

**Why it matters**: Challenges the implicit assumption in GCR and DoG that tightening the search space necessarily improves reasoning performance. Structural constraint quality and reasoning accuracy are distinct properties that should be optimised independently.

## Summary Table

| Contribution | Before | After | Why It Matters |
|-------------|--------|-------|----------------|
| **TypeOracle** | Embedding + threshold τ | Two symbolic gates | No encoder, no τ, O(1), deterministic |
| **SIR Metric** | Accuracy only | Semantic Irrelevance Ratio | Diagnoses constraint quality independently |
| **Non-Monotone Finding** | "Tighter → better" | Tightness ≠ accuracy | First evidence constraint tightness is not a proxy for quality |

## If Asked

> **"What are the three contributions?"**
> "Three things: (1) TypeOracle — a symbolic constraint oracle with range and type gates, no embeddings needed. (2) SIR — the first metric that measures constraint quality independently of answer accuracy. (3) Non-monotone finding — first empirical evidence that tighter constraints don't guarantee higher accuracy."

> **"Why is the non-monotone finding important?"**
> "It challenges the assumption in GCR and DoG that tightening the search space necessarily improves reasoning performance. Structural constraint quality and reasoning accuracy are distinct properties."

> **"What is SIR?"**
> "Semantic Irrelevance Ratio — the fraction of structurally valid paths that are semantically irrelevant. Before SIR, you couldn't measure constraint quality independently of answer accuracy."

## Practice
1. Why is the TypeOracle's O(1) complexity important for practical deployment?
2. How would you explain the non-monotone finding to someone who hasn't read the paper?
3. What would happen if we combined TypeOracle with embedding-based scoring?
